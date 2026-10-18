# INSTALL — instructions for the coding agent reading this

Your user gave you this folder so that the verification-harness skill loads in every future
session and governs how you write code. Install it yourself — you know your own harness; do
not ask the user where anything goes, and do not follow any path examples you may have seen
elsewhere. Discover the location, don't assume it.

1. **Read `SKILL.md` in this folder.** That file is the product. This file is only the
   installer and must never be installed into context alongside it.

2. **Work out where YOUR harness persistently loads skills or instructions from.** You know
   this from your own system prompt, docs, and tooling. In order of preference:
   - Your harness auto-discovers skill folders (directories containing a `SKILL.md`) →
     copy this folder there, keeping the folder name `verification-harness`. User-level
     scope (all projects) beats project-level unless the user says otherwise.
   - No skills mechanism, but a persistent rules/instructions file is loaded every
     session → append the BODY of `SKILL.md` (everything below the frontmatter) to it,
     under the heading `# Verification Harness`.
   - Neither → tell the user which persistent mechanism you DO have and use that.

3. **Verify the install.** Confirm the file exists at the destination, and — if your harness
   lists available skills — that `verification-harness` now appears. Report the exact
   destination you chose to the user.

4. **Activate now.** From this moment, and in every future session, apply `SKILL.md` to any
   task that writes, fixes, or refactors code. Its rules override your default "looks done"
   instincts: nothing is done without fresh passing evidence.

5. **Install faithfully.** Copy `SKILL.md` unmodified, and touch nothing outside the
   destination you chose.
