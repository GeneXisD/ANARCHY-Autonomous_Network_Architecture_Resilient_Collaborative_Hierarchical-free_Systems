# ANARCHY — START HERE

## For a new ChatGPT/agent session

Read these files in this order:

1. `ANARCHY_CONTEXT.md` — canonical project context, current execution priority, and continuation directive.
2. `docs/platform/slackware-first-build.md` — active Slackware-first build sequence, Dyne SDK compatibility findings, and baseline checklist.
3. `docs/provenance/one-click-provisioning.md` — build, package, provenance, and one-click provisioning model.
4. `docs/licensing/evidence-status.md` — verified versus unresolved licensing and source evidence.
5. `README.md` — broader research corpus and project history.

When working specifically on the Apple restore research stream, also read:

- `docs/architecture/ANARCHY-APPLE-RESTORE.md`

## Continuation phrase

Use:

> **Open `ANARCHY_CONTEXT.md` and continue from the canonical ANARCHY context. Slackware first.**

The assistant/agent should inspect the current repository state and continue from what is implemented, proposed, verified, blocked, or unresolved. Do not make the user restate the architecture.

## Evidence rule

Keep unresolved items marked **UNVERIFIED** until their primary artifacts are inspected. In particular, do not infer the installed Slackware release or host configuration, do not assume the Dyne:bolic IV SDK builds natively on Slackware, and do not convert an archival reference into proof of a current implementation.

## Working rule

Substantial changes should use a topic branch and pull request. Keep `main` stable. Preserve historical upstream source lines and their commit histories; do not overwrite one with another.
