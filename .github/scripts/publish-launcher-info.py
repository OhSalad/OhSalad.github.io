import datetime
import pathlib
import sys
from launcher_announcements import merge, read_json

snapshot = read_json(pathlib.Path(sys.argv[1]))
editorial = read_json(pathlib.Path("launcher/announcements.json"))
result = merge(snapshot, editorial, datetime.datetime.now(datetime.timezone.utc))
import json
pathlib.Path("launcher/server-info.json").write_text(json.dumps(result, indent=2, allow_nan=False) + "\n")
