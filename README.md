# Tales of Pirates DX client distribution

[Download the full online client 1.1.2](https://github.com/OhSalad/OhSalad.github.io/releases/download/online-client-1-1-2/TOPDX-Online-Setup-1.1.2.exe), or visit [the download page](https://ohsalad.github.io/).

This installer includes the current revision-11 game files and managed launcher 1.1.2, pinned to 82.38.139.13:1973. Install into its separate Tales of Pirates DX Live folder, then open the launcher. The first full integrity check can take a few minutes.

The installer embeds a signed revision-11 baseline. Older releases retain signed patch manifests, signatures, and ZIP bundles required by existing installations; those updater assets must remain available.

The live signed release catalog is served without caching at https://82.38.139.13/updater/client-v2/status.json and its status.sig.json pair. The launcher uses retained production signing keys, verifies update bytes and persists monotonic receipts. Future qualified client and launcher updates install automatically.

Public rates and account counts remain display-only information at https://82.38.139.13/launcher/server-info.json. Edit launcher/announcements.json for notices and dated events. Server samples are collected from the VPS independently; announcements do not change gameplay rewards.
