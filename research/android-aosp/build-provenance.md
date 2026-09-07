# AOSP build, manifests, and provenance

AOSP is also important as a **large-scale source federation/build-system case study**.

## Research targets

- Git repositories and repository manifests
- `repo` multi-project source management
- Gerrit review and contribution workflows
- Soong
- Blueprint
- Ninja build graph generation
- product/device configuration
- generated artifacts
- signing
- reproducible-build considerations
- source-to-artifact provenance

## ANARCHY relevance

ANARCHY should be able to describe a software component without assuming that its source lives in one monolithic repository. A useful artifact record should include:

```text
artifact hash
source repository
commit/revision
manifest or dependency lock
build recipe
compiler/toolchain identity
configuration
inputs
signing identity
build timestamp
provenance/evidence links
```

This connects directly to ANARCHY's research into Git, package ecosystems, Portage/emerge, Cygwin, open-source distribution, and federated infrastructure.

## Important distinction

AOSP's Gerrit/repo workflow is an example of federation **inside an organized project**. ANARCHY should investigate how equivalent provenance can survive when repositories, build hosts, mirrors, and maintainers are independently operated.
