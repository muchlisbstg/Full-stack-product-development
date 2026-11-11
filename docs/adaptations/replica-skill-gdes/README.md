# GDES-controlled Replica Skill adaptation overlay

**Status: evaluation-only. Not installed. Not approved for adoption.**

Upstream source is pinned to `Jakeschincariol/replica-skill` commit
`77c9436fb3d18c3d58169efb8caf4fe906b0dc51`. Files in this folder are
GDES-controlled adapted copies for review; they do not modify the upstream
repository and are not copied into a GDES product workspace.

## 1. Adapted skill files

| Skill | GDES adaptation |
|---|---|
| `replica-backend` | Adds Claude Code `disable-model-invocation: true` and a GDES manual-authorization gate |
| `replica-deploy` | Adds Claude Code `disable-model-invocation: true` and a GDES manual-authorization gate |
| `replica-design` | Routes contrast helper through the GDES resolver |
| `replica-diff` | Routes parity and image-diff helpers through the GDES resolver |
| `replica-entrepreneur` | Routes reviews helper through the GDES resolver |
| `replica-brand` | Routes sweep and contrast helpers through the GDES resolver |
| `replica-launch` | Routes listing helper through the GDES resolver |

The four remaining skills have no Python helper path or high-impact backend /
deployment operation requiring an overlay in this patchset:
`replica-recon`, `replica-architect`, `replica-build`, and
`replica-test`. Their upstream copies remain unchanged.

## 2. Helper path contract

The adapted skill instructions call one repository-root resolver:

```sh
python3 scripts/gdes/replica_skill_tool.py replica-design contrast.py replica/design/tokens.json
```

Set `GDES_REPLICA_SKILLS_ROOT` to the absolute root directory of the pinned
upstream checkout (the directory containing all `replica-*/` folders).

POSIX shell:

```sh
export GDES_REPLICA_SKILLS_ROOT="/absolute/path/to/replica-skill"
```

PowerShell:

```powershell
$env:GDES_REPLICA_SKILLS_ROOT = "C:\\absolute\\path\\to\\replica-skill"
```

The resolver allowlists the skill/helper pair, resolves the path from the
configured root rather than the current directory, rejects path traversal,
and runs the selected helper in-process. It does not grant permission for
the helper's own file operations. Use disposable fixtures and explicit
authorization before invoking a helper that writes output.

Validate helper presence without executing any helper:

```sh
python3 scripts/gdes/replica_skill_tool.py --check /absolute/path/to/replica-skill
```

## 3. Invocation gate

The adapted `replica-backend` and `replica-deploy` add
`disable-model-invocation: true` for Claude Code and explicit policy text
requiring a direct user authorization naming the action, target environment
and scope. The default behavior is to prepare a plan, not execute operations.

This frontmatter control is Claude Code-specific. It is not evidence that
Codex or VS Code enforces the same invocation gate. Their runtime policy
configuration and negative invocation tests remain outstanding. A sentence
inside a skill is not a substitute for platform-enforced authorization.

No migrations, live payments, account creation, DNS changes, infrastructure
provisioning, releases, deployments or production writes are authorized.

## 4. Validation boundary

The updated GitHub Actions workflow:
- validates all 11 upstream skill metadata files;
- simulates the three documented discovery directory layouts in a temporary
  directory (33 static copies);
- validates the 7 GDES adaptation overlays and resolver;
- checks the resolver's allowlisted helper inventory;
- runs the upstream standard-library unit test suite;
- retains logs and a summary as a 30-day GitHub Actions artifact.

It does **not** launch Claude Code, Codex, VS Code, Copilot, or any other
agent runtime. The 33 directory copies are packaging/layout tests, not skill
load or invocation tests.

## 5. Acceptance status

- Upstream unit tests: prior run 57/57 PASS; rerun with retained artifact pending.
- Native discovery layout simulation: pending updated workflow run.
- GDES invocation overlays: implemented in this branch; static validation pending.
- Helper resolver: implemented; static validation pending.
- Claude Code runtime: NOT TESTED.
- Codex runtime: NOT TESTED.
- VS Code/Copilot runtime: NOT TESTED.
- Adoption: NOT APPROVED; Standards Owner decision required.
