# ANARCHY Slackware-First Build Foundation

**Status:** PROPOSED EXECUTION BASELINE  
**Priority:** Slackware first  
**Last reviewed:** 2026-11-04

## Purpose

This document records the current implementation order for ANARCHY's GNU/Linux foundation. The immediate platform priority is Slackware. Dyne:bolic and its SDK lineage are to be inspected and integrated only after the Slackware base has been inventoried and stabilized.

This is a build-order decision, not a claim that the complete system already builds or that any particular Slackware release has been selected.

## Execution order

1. **Slackware base**
   - Inspect the actual installed release, architecture, kernel, boot mode, storage layout, package database, repositories, compiler, libc, init/service configuration, network interfaces, and available build space.
   - Record the baseline before changing packages or boot configuration.
   - Verify package integrity and retain the exact package/version inventory.
   - Establish a clean, repeatable native build environment.
2. **Dyne:bolic source and SDK lineage**
   - Preserve the historical Dyne:bolic sources and manual as separate evidence.
   - Compare the historical `GeneXisD/dynebolic` fork with `dyne/dynebolic-upstream`.
   - Identify the exact SDK generation, scripts, base distribution assumptions, toolchain, package inputs, and licenses before building.
3. **Dyne integration**
   - Determine which components can be built natively on Slackware and which require a separately isolated, documented build root or a port of upstream build scripts.
   - Do not silently replace Slackware with Debian, Devuan, or Ubuntu.
   - Record every compatibility patch as an ANARCHY-authored modification, with upstream commit, patch, build log, and resulting hashes.
4. **ANARCHY services and networking**
   - Add the selected networking and orchestration components only after the base and Dyne build stages are reproducible.
   - Current design notes include Netsukuku, Tokyo Cabinet/B+ tree indexing, I2P, and Node-RED as an I2P control/orchestration interface. These are planned integration areas, not claims of an already working deployment.
5. **Multi-machine integration**
   - Assign machine roles only after each host has a verified baseline and a reproducible provisioning record.
   - Keep node identity, authorization, network membership, service control, and data custody as separate concerns.

## Dyne:bolic primary references

### Historical user manual

- Source: https://distro.ibiblio.org/dynebolic/dynebolic-manual.txt
- Title: *Dyne:II GNU/Linux User's Guide*
- Author/copyright: Denis Rojo, aka Jaromil; 2003–2007.
- Manual license: GNU Free Documentation License 1.2 or later, with the stated Introductory and Colophon invariant sections and front-/back-cover attribution text requirements.
- The manual separately states Dyne:bolic software is GPL version 2 or later.

The manual documents live boot, docking, persistent nests, modular `.dyne` applications, PXE/DHCP/TFTP network boot, cluster computer farms, and development tools. It is historical evidence and must not be treated as a current build recipe without validating each command and dependency.

### Historical fork / SDK

- Repository: https://github.com/GeneXisD/dynebolic
- Observed SDK path: `dyneIV/SDK/`
- Its README describes `download.sh`, `setup.sh`, and a chroot workflow.
- Its `build.sh` identifies Devuan Beowulf as the build base and requests `zsh` and `debootstrap`.
- Its `config` identifies the Beowulf blend and version `3.0.0`.

This fork is a historical source line. Preserve its content and commit history; do not overwrite it with upstream files.

### Current upstream source line

- Repository: https://github.com/dyne/dynebolic-upstream
- SDK path: `dyneIV/`
- Its `README.md` says to use Devuan or Debian and not Ubuntu.
- Its Makefile uses `apt-get` for development dependencies and defines build, module, ISO, QEMU, snapshot, and USB-burn targets.
- The inspected Makefile identifies its source license as GNU GPL version 3 or later.

**Compatibility finding:** the inspected Dyne:bolic IV SDK workflows are Debian/Devuan-oriented. They are not demonstrated to run natively on Slackware. This is the first integration gate to resolve. Slackware remains the selected host foundation; any Debian/Devuan build root, if later required, must be isolated, documented, and subordinate to that decision rather than silently becoming the host platform.

## Required baseline record

Before package installation, removal, partition changes, or bootloader changes, capture:

| Field | Required evidence |
|---|---|
| Slackware release | Exact release/version and installation source |
| Architecture | Machine architecture and target architecture |
| Kernel | Running kernel, available kernel sources/headers, config where available |
| Boot | BIOS/UEFI mode, bootloader, boot entries |
| Storage | Device/partition/filesystem map; no destructive changes during inventory |
| Packages | Installed package list and repository/source metadata |
| Toolchain | Compiler, assembler, linker, make, scripting runtimes, libc |
| Services | Init system, enabled services, network configuration |
| Build capacity | Free space, RAM, CPU, and required build dependencies |
| Provenance | Source URLs, versions/commits, license files, notices, SHA-256 hashes |

Unknown values remain **UNVERIFIED** until inspected on the actual Slackware host.

## Build and release gates

- **Gate A — Baseline captured:** no platform changes until the current host state is recorded.
- **Gate B — Slackware base validated:** native compiler and package environment are reproducible.
- **Gate C — Dyne SDK compatibility decided:** native port or isolated build root is selected with evidence.
- **Gate D — Build reproduced:** scripts, inputs, versions, and outputs are captured.
- **Gate E — Distribution reviewed:** SBOM, source correspondence, notices, licenses, hashes, and trademark requirements are checked before redistribution.

## Provenance and licensing rules

- Keep the manual's GFDL terms separate from software licenses.
- Keep the historical Dyne:bolic GPL-2.0-or-later statement separate from the current upstream Dyne:IV Makefile's GPL-3.0-or-later header.
- Do not infer that every component in a distribution has the same license.
- Preserve upstream copyright notices and license texts.
- Identify ANARCHY modifications and authorship without claiming ownership of upstream code.
- A magazine, manual, ISO, or archive record is historical evidence; it does not replace the corresponding upstream source required for a source-code distribution.

## Immediate next action

Run a read-only inventory of the actual Slackware environment and use the results to complete the baseline table. Do not install, remove, repartition, reformat, or rewrite boot configuration during this first pass.
