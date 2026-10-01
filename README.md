# Tales of Pirates DX client distribution

This repository hosts public client installers and signed content updates.

Client downloads: https://github.com/OhSalad/OhSalad.github.io/releases

Website: https://ohsalad.github.io/

The first qualified client release is being prepared. No installer is available yet.

## Update feed

The managed launcher will read these exact HTTPS URLs:

- https://ohsalad.github.io/updater/status.json
- https://ohsalad.github.io/updater/status.sig.json

Only reviewed, signed status documents describing a qualified active server may be published. Empty or unsigned placeholder status documents must not be used.

Installers and patch ZIPs belong in immutable GitHub Releases, outside the Pages tree. Private source code, server packages, signing keys, and credentials must never be uploaded here.
