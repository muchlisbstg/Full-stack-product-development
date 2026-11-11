# HIG-01 F02 — Least-Privilege Execution Policy

**Source:** `higgsfield-ai/skills@27000402070db19d958789d05b3b52b6f4718d7c`  
**Scope:** all nine skill instruction files in this pinned release.  
**Disposition:** proposed remediation overlay; host-level enforcement and runtime behavior still require verification.

## Source finding

All nine tracked `*/SKILL.md` files explicitly declared `allowed-tools: Bash` in frontmatter. This grants a broad shell tool allowance at skill activation time rather than a task-scoped, command-scoped permission. The skills also include shell command examples, installation steps, and local helper-script references.

## Remediation

1. Remove the explicit `allowed-tools: Bash` grant from all nine skill frontmatter blocks.
2. Add an execution approval boundary to each skill: command examples are reference-only; the agent must not infer permission to run them.
3. Require explicit, current-task approval for the exact command, working directory, expected filesystem effects, network access, and charge implications.
4. Prohibit implicit sudo, system path writes, package installation, shell startup changes, destructive/bulk filesystem operations, and execution of unreviewed repository scripts.
5. Prefer inert file inspection. If the host cannot enforce sandboxing and approval, stop and provide manual instructions.

## Why not add a narrow Bash allowlist?

The pinned source contains multiple different command families and helper scripts across generation, brandkit, video assembly, website/game builds and deployment. A single static allowlist would be incomplete and could create a false security boundary. The remediation therefore removes the skill-level Bash grant and delegates any execution to the host's explicit per-action approval/sandbox controls.

## Acceptance criteria

- All nine skill frontmatter blocks contain no `allowed-tools: Bash` or equivalent Bash grant.
- All nine contain the execution approval boundary.
- No candidate skill may treat embedded command examples as authorization to execute.
- Privileged/destructive actions require separate explicit approval and exact path/command scope.
- Candidate scripts remain unexecuted during this static validation.
- Host-level Codex/Claude/Cursor permission behavior is separately verified before runtime acceptance.

## Test strategy

- Parse frontmatter delimiters and check the absence of Bash grants.
- Check required approval clauses in every skill file.
- Negative fixtures prove that a reintroduced Bash grant or missing approval clause fails validation.
- These tests verify source policy text only. They do not prove that the host application enforces the policy.
