import datetime
import json
import pathlib
import sys

source = pathlib.Path(sys.argv[1])
if source.stat().st_size > 65536:
    raise ValueError("Server snapshot is too large")
snapshot = json.loads(source.read_text())
if snapshot["schema_version"] != 1 or snapshot["gate_address"] != "82.38.139.13":
    raise ValueError("Unexpected server snapshot")
sampled = datetime.datetime.fromisoformat(snapshot["sampled_at_utc"].replace("Z", "+00:00"))
now = datetime.datetime.now(datetime.timezone.utc)
if abs((sampled - now).total_seconds()) > 120:
    raise ValueError("Collector timestamp is not current")
players = snapshot["online_players"]
if players is not None and (type(players) is not int or not 0 <= players <= 1000000):
    raise ValueError("Invalid aggregate player count")
for value in snapshot["rates"].values():
    if value is not None and (type(value) not in (int, float) or not 0.01 <= value <= 1000):
        raise ValueError("Invalid server rate")
announcements = json.loads(pathlib.Path("launcher/announcements.json").read_text())
if len(announcements["notice"]) > 400 or len(announcements["events"]) > 20:
    raise ValueError("Announcement limits exceeded")
for event in announcements["events"]:
    if len(event["title"]) > 80 or len(event["description"]) > 400:
        raise ValueError("Event text limits exceeded")
    starts = datetime.datetime.fromisoformat(event["starts_at_utc"].replace("Z", "+00:00"))
    ends = datetime.datetime.fromisoformat(event["ends_at_utc"].replace("Z", "+00:00"))
    if starts.tzinfo is None or ends.tzinfo is None or ends <= starts:
        raise ValueError("Invalid event time range")
snapshot["notice"] = announcements["notice"]
snapshot["events"] = announcements["events"]
pathlib.Path("launcher/server-info.json").write_text(json.dumps(snapshot, indent=2, allow_nan=False) + "\n")
