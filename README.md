# Tales of Pirates DX client distribution

This repository hosts public client installers and signed content updates.

Client downloads: https://github.com/OhSalad/OhSalad.github.io/releases

Website: https://ohsalad.github.io/

An online installer/updater test prerelease is available, pinned to 82.38.139.13:1973. Its test feed expires on 2026-10-08 at 17:40 UTC and supersedes the earlier local test feed. The first production client release is still being prepared.

## Update feed

The managed launcher will read these exact HTTPS URLs:

- https://ohsalad.github.io/updater/status.json
- https://ohsalad.github.io/updater/status.sig.json

The current feed is a signed **test-channel fixture**, trusted only by the online test installer. It changes an unused probe asset and does not establish actual live server compatibility or production activation. A production feed requires qualification and production signatures; empty or unsigned placeholders must not be used.

Installers and patch ZIPs belong in immutable GitHub Releases, outside the Pages tree. Private source code, server packages, signing keys, and credentials must never be uploaded here.

## Launcher dashboard

Installer 0.1.1 adds server-configured XP/team XP/drop rates, sampled logged-in account counts, events, maintenance notices, and file-check progress. Display information is fetched from https://ohsalad.github.io/launcher/server-info.json. It is separate from signed update authorization. Rates are read from the VPS configuration; they are not hardcoded in the launcher.

Edit launcher/announcements.json for notices and dated events. A VPS systemd timer publishes actual server samples every five minutes, including while the operator PC is off. GitHub Pages builds and caching can delay visibility. The GitHub publisher workflow also runs after announcement edits and supports manual refreshes. The launcher shows sample time and unavailable/stale states. Events are display announcements; they do not change gameplay rewards.

Installer 0.2.0 adds Discord/support/log links, visible versions, and clearer failure messages. It supports verified launcher-only upgrades of installations with the same signed baseline, preserving game files and updater state; different baselines or damaged/pending updates are rejected. Launcher self-updating is not included. The currently distributed test installer still uses signed-status Play admission and its October 8 expiration remains in effect.
