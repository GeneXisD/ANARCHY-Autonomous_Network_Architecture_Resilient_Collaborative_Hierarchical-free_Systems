# ANARCHY — START HERE

## For a new ChatGPT/agent session

Read these files in this order:

1. `ANARCHY_CONTEXT.md` — canonical project context and continuation directive.
2. `docs/architecture/ANARCHY-APPLE-RESTORE.md` — current Apple restore architecture and security boundary.
3. `docs/provenance/one-click-provisioning.md` — build, package, provenance and one-click provisioning model.
4. `docs/licensing/evidence-status.md` — what is verified versus still awaiting primary evidence.
5. `README.md` — broader research corpus and project history.

### Continuation phrase

Use:

> **Open `ANARCHY_CONTEXT.md` and continue from the canonical ANARCHY context.**

The assistant/agent should then inspect the current repository state and continue from what is implemented, proposed, verified, blocked, or unresolved. Do not make the user restate the architecture.

## Evidence rule

The context file deliberately records unresolved items such as the actual DC219 policy, Linux&C Vol. 39 and exact FunkyMios source. Those items must remain marked **UNVERIFIED** until their primary artifacts are inspected.

## Working rule

Substantial changes should use a topic branch and pull request. Keep `main` stable. GitHub recommends branches and pull requests for isolated development and protected important branches.
