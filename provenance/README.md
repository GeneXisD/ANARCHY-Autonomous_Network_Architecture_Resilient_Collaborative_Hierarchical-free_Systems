# Software Provenance

Software provenance answers questions such as:

- Where did this artifact originate?
- Which repository contained it?
- Which revision produced it?
- Who authored the revision?
- What is its cryptographic identity?
- What license governs it?
- What copyright notices accompany it?
- What derivative relationship exists?
- Was it migrated between hosting platforms?

Potential provenance chain:

SOURCE
  ↓
PROJECT
  ↓
FILE
  ↓
COMMIT
  ↓
OBJECT HASH
  ↓
LICENSE
  ↓
DERIVATIVE
  ↓
DISTRIBUTION

Relevant systems:

- Git
- GitHub
- GitHub Archive
- Google Code Archive
- SPDX
- SBOM
- reproducible builds
- signed commits
- cryptographic hashes
