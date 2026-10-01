"""Validate display-only editorial content before publication."""
import datetime
import json
import math

MAX_BYTES = 65536


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("Duplicate JSON field")
            result[key] = value
        return result
    with open(path, "rb") as source:
        raw = source.read(MAX_BYTES + 1)
    if not raw or len(raw) > MAX_BYTES:
        raise ValueError("Display document exceeds its byte limit")
    return json.loads(raw, object_pairs_hook=unique,
                      parse_constant=lambda _: (_ for _ in ()).throw(ValueError("Non-finite JSON number")))


def text(value, maximum):
    if not isinstance(value, str) or len(value.encode("utf-16-le")) // 2 > maximum:
        raise ValueError("Display text exceeds its limit")
    if any((ord(c) < 32 or 127 <= ord(c) <= 159) and c not in "\r\n" for c in value):
        raise ValueError("Display text contains control characters")
    return value


def timestamp(value):
    if not isinstance(value, str) or len(value) > 40 or not value.endswith("Z"):
        raise ValueError("Display timestamps must be UTC")
    result = datetime.datetime.fromisoformat(value[:-1] + "+00:00")
    if result.utcoffset() != datetime.timedelta(0):
        raise ValueError("Display timestamp has an invalid offset")
    return result


def validate_announcements(value):
    if not isinstance(value, dict) or set(value) != {"notice", "events"}:
        raise ValueError("Unexpected announcement fields")
    text(value["notice"], 400)
    events = value["events"]
    if not isinstance(events, list) or len(events) > 20:
        raise ValueError("Too many announcements")
    for event in events:
        if not isinstance(event, dict) or set(event) != {
                "title", "description", "starts_at_utc", "ends_at_utc"}:
            raise ValueError("Unexpected event fields")
        text(event["title"], 80)
        text(event["description"], 400)
        if timestamp(event["ends_at_utc"]) <= timestamp(event["starts_at_utc"]):
            raise ValueError("Event must end after it starts")
    return value


def merge(snapshot, editorial, now):
    if not isinstance(snapshot, dict) or set(snapshot) != {
            "schema_version", "gate_address", "sampled_at_utc", "online_players",
            "rates", "notice", "events"}:
        raise ValueError("Unexpected collector fields")
    if type(snapshot["schema_version"]) is not int or snapshot["schema_version"] != 1 or snapshot["gate_address"] != "82.38.139.13":
        raise ValueError("Unexpected collector identity")
    if abs((timestamp(snapshot["sampled_at_utc"]) - now).total_seconds()) > 120:
        raise ValueError("Collector sample is stale")
    players = snapshot["online_players"]
    if players is not None and (type(players) is not int or not 0 <= players <= 1000000):
        raise ValueError("Invalid aggregate account count")
    rates = snapshot["rates"]
    if not isinstance(rates, dict) or set(rates) != {"xp", "team_xp", "drop"}:
        raise ValueError("Unexpected rate fields")
    for value in rates.values():
        if value is not None and (type(value) not in (int, float) or not math.isfinite(value) or not 0.01 <= value <= 1000):
            raise ValueError("Invalid server multiplier")
    validate_announcements(editorial)
    result = dict(snapshot, notice=editorial["notice"], events=editorial["events"])
    if len(json.dumps(result, ensure_ascii=False).encode("utf-8")) > MAX_BYTES:
        raise ValueError("Merged display document exceeds its limit")
    return result


if __name__ == "__main__":
    import argparse
    import sys
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args()
    try:
        validate_announcements(read_json(args.path))
        print("Announcement document validated.")
    except (OSError, ValueError, RecursionError) as error:
        print("Announcement validation failed type=" + type(error).__name__, file=sys.stderr)
        sys.exit(1)
