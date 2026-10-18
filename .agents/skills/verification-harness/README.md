# verification-harness

A single-file skill that forces an evidence-gated workflow on any code-writing agent:
pin acceptance criteria → implement → adversarial tests designed from the spec → dry-run
traces of every critical path → execute real test/lint/typecheck/build → bounded repair loop
that never weakens tests → PASS only with fresh passing output, otherwise an honest
NOT VERIFIED.

## How to use (human instructions)

Drop the zip (or this folder) into any coding-agent session and say:

> Unzip this, read INSTALL.md, install the skill into your own harness, and follow it from
> now on. 

That's it. The agent reads `INSTALL.md`, figures out where its own harness keeps skills or
persistent instructions, installs `SKILL.md` there, verifies, and starts applying it. No
paths to look up — the agent knows its own setup.

Files:
- `SKILL.md` — the harness itself; the only file that ever goes into agent context.
- `INSTALL.md` — one-time bootstrap instructions, addressed to the agent.
- `README.md` — this file, for humans; never paste it into prompts.

License: MIT
