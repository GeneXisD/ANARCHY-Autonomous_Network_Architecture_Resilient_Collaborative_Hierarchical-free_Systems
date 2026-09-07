# ANARCHY Apple Restore Architecture

## Objective

ANARCHY investigates how to reproduce the **observable, open-source host-side restore workflow** around Apple devices using legitimately obtained software, firmware and documented interfaces.

This is an engineering/research architecture, not a proposal to bypass Apple security controls.

## Pipeline

```text
device identification
        ↓
firmware/image acquisition
        ↓
IPSW extraction
        ↓
manifest + component discovery
        ↓
partition/GPT analysis
        ↓
recovery/restore transport
        ↓
filesystem/image handling
        ↓
kernel + module toolchain
        ↓
integrity/signature verification
        ↓
restore
        ↓
post-restore validation
        ↓
provenance record
        ↓
local RitualMesh/ANARCHY distribution
```

## Open-source host-side components

The principal ecosystem to inventory is:

- usbmuxd
- libimobiledevice
- libimobiledevice-glue
- libirecovery
- idevicerestore
- libplist
- libtatsu where applicable to the current upstream workflow

For each component record upstream URL, release/commit, license, dependencies, build requirements, patch set, build hash, and resulting artifact hashes.

## Build layer

```text
upstream source
      ↓
license/provenance scan
      ↓
crosstool-NG or native toolchain
      ↓
configured build
      ↓
tests
      ↓
package
      ↓
SBOM + notices + hashes
```

## Provisioning layer

ANARCHY should be able to represent a restore environment as a declarative manifest. The openSUSE YMP/One Click Install model and XAMPP's installer/build model are architectural precedents.

Example future manifest:

```yaml
name: anarchy-apple-restore
version: 0.1
host:
  os: linux
components:
  - name: libimobiledevice
    source: upstream
  - name: libirecovery
    source: upstream
  - name: idevicerestore
    source: upstream
toolchain:
  provider: crosstool-ng
provenance:
  sbom: required
  hashes: required
  notices: required
validation:
  host_tools: required
```

## Security boundary

ANARCHY may analyze restore protocols, images, manifests, partition layouts, open-source code, logs, and legitimate firmware. It must not implement or document mechanisms intended to defeat Activation Lock, FRP, secure boot, proprietary signing, or device authorization.

## Android/Qualcomm distinction

AOSP, Qualcomm Sahara/EDL, Motorola recovery tooling, and Android flashing systems are adjacent research areas. They should share provenance/build infrastructure but remain distinct restore backends rather than being treated as the Apple restore protocol.

## Provenance requirement

Every generated restore artifact should be traceable:

```text
source → revision → patch → toolchain → build → hash → package → manifest → deployment/test
```
