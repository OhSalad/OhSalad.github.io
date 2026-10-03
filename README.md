# Tales of Pirates DX client distribution

[Download the full online client 1.0.1](https://github.com/OhSalad/OhSalad.github.io/releases/download/online-client-1-0-1/TOPDX-Online-Setup-1.0.1.exe), or visit [the download page](https://ohsalad.github.io/).

This installer includes the complete qualified game client and managed launcher 1.0.1, pinned to 82.38.139.13:1973. Open the launcher after installation to receive the signed HUD and item update automatically. No separate upgrader is required.

The current release also contains the signed manifest and ZIP required by the automatic updater. All current patch files are packaged in this release; older GitHub releases are unnecessary.

The live signed release catalog is served without caching at https://82.38.139.13/updater/client-v2/status.json and its status.sig.json pair. The launcher uses retained production signing keys, verifies update bytes and persists monotonic receipts. Future qualified client and launcher updates install automatically.

Public rates and account counts remain display-only information at https://82.38.139.13/launcher/server-info.json. Edit launcher/announcements.json for notices and dated events. Server samples are collected from the VPS independently; announcements do not change gameplay rewards.
