# ANARCHY Build-Block Workflow

**Purpose:** Make the current work visible so collaborators can tell whether a build block is active, paused, blocked, awaiting review, or complete. A quiet chat or lack of messages must not be interpreted as inactivity when the repository status shows current work.

## 1. Public status sources

Use three linked records:

1. **BUILD_STATUS.md** — one current, public snapshot. This is the first place a collaborator checks.
2. **GitHub build-block issue** — discussion, questions, handoffs, and event history for a specific block.
3. **Git commits / pull requests** — durable evidence of changes to source, documentation, tests, and build records.

The status page is a snapshot, not a substitute for commit history or test evidence. Update it when a material state change occurs.

## 2. Status vocabulary

| Status | Meaning |
|---|---|
| NOT STARTED | Planned, but work has not begun |
| READY | Prerequisites are available; ready to start |
| IN PROGRESS | Work is actively being performed |
| PAUSED | Work has intentionally stopped; preserve the next action |
| BLOCKED | A specific dependency, permission, defect, or decision prevents progress |
| WAITING | Work is complete on the user's side and awaits another person, system, or review |
| VALIDATING | Implementation exists and is undergoing tests or independent review |
| COMPLETE | Acceptance criteria are met and evidence is linked |
| CANCELLED | Explicitly stopped; reason recorded |

Do not use COMPLETE for an untested design, a proposed architecture, or a command that has not returned a verified result.

## 3. Required fields for every build block

Each block must identify:

- **Block ID:** stable identifier, e.g. AN-H1 or AN-NODE-02.
- **Title:** one concrete outcome.
- **Owner:** responsible person or agent.
- **Node:** machine ID or environment; use a sanitized node ID in public records.
- **Status:** one value from the table above.
- **Phase:** research, design, setup, build, test, release, or recovery.
- **Current step:** what is being done now.
- **Last verified action:** a result actually observed, with date and evidence.
- **Next action:** one actionable next step.
- **Blocker:** exact missing item, or NONE.
- **Acceptance criteria:** objective conditions for completion.
- **Evidence:** commit, issue, log, test report, hash, or artifact reference.
- **Updated:** date/time with timezone where available.

## 4. Update cadence

Publish a status update when:

- starting a block;
- finishing a meaningful step;
- pausing for a break or switching machines;
- discovering a blocker;
- clearing a blocker;
- handing work to another person or agent;
- beginning validation;
- completing or cancelling a block.

A short update is sufficient. It is better to say "PAUSED — next action is verify Git installation" than to leave the status ambiguous.

For long-running work, update at the end of each work session. Do not fabricate progress to make a dashboard look active.

## 5. Build-block issue format

Use the GitHub Issue template named **Build block update**. If the template is unavailable, use this format in an issue or comment:

    Block ID:
    Title:
    Owner:
    Node:
    Status:
    Phase:
    Current step:
    Last verified action:
    Next action:
    Blocker:
    Acceptance criteria:
    Evidence:
    Updated:

Keep one issue per substantial build block. Use comments for incremental progress; link the issue from BUILD_STATUS.md when it becomes the active block.

## 6. Suggested project-board columns

- Backlog
- Ready
- In progress
- Paused
- Blocked
- Validating
- Complete

A card moves only when the status and evidence are updated. Paused and Blocked are visible states, not failures or reasons to hide work.

## 7. Handoffs between people and AI agents

A handoff must include:

1. task ID and objective;
2. current branch and commit;
3. exact files or artifacts involved;
4. commands already run and their actual outputs;
5. verified facts versus assumptions;
6. permissions granted and prohibited actions;
7. next action and acceptance criteria.

The receiving agent must inspect the repository and evidence before changing files. It must not assume that a prior command succeeded merely because it was suggested or entered.

## 8. Public/private information boundary

The public dashboard and issue tracker may contain sanitized progress, node IDs, software versions, non-sensitive errors, commit links, and test outcomes.

Never publish:
- passwords, tokens, private keys, recovery phrases, or session cookies;
- private IP addresses, private hostnames, serial numbers, or precise physical locations;
- private user data or unredacted logs;
- exploitable vulnerability details before coordinated disclosure;
- proprietary material or third-party data without permission.

Store sensitive operational inventory locally in an access-controlled location. Link to a sanitized evidence summary rather than exposing the raw record.

## 9. Completion rule

A block is COMPLETE only when:
- its acceptance criteria are met;
- tests and results are recorded;
- relevant artifacts have hashes and provenance;
- license and redistribution status are resolved for any published artifact;
- the status snapshot and issue are updated;
- the next block is identified.

This workflow is intended to make progress legible, not to create reporting overhead. A concise, truthful update is enough.
