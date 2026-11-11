# Install for Agents

You are an AI coding agent. The user asked you to install Higgsfield skills. Follow this exactly.

## Step 1 — Install Higgsfield CLI

```bash
curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
```

The script asks for sudo password to write to `/usr/local/bin/`. If sudo isn't available, install to home:

```bash
curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh -s -- --prefix=$HOME/.local
```

Verify: `higgsfield version`. Expect `higgsfield v0.1.X (...) built ...`.

## Step 2 — Authenticate

Ask the user to run:

```bash
higgsfield auth login
```

This opens a browser for OAuth. Wait for them to confirm.

Verify: `higgsfield account status`. Expect `<email> — <plan> plan, <N> credits`.

## Step 3 — Install the skills

**Claude Code** — install the plugin, then ask the user to restart Claude Code:

```bash
claude plugin marketplace add higgsfield-ai/skills
claude plugin install higgsfield@higgsfield
```

If the plugin install is unavailable, clone the repo anywhere and run `./setup --host claude`, which links each skill into `~/.claude/skills/<skill-name>`. Do not clone the repo into `~/.claude/skills/higgsfield`: Claude Code looks for each skill one level down and finds none there.

**Other agents** — clone into the agent's plugin directory:

| Agent | Path |
|---|---|
| Cursor | `~/.cursor/plugins/higgsfield` |
| Codex | `~/.codex/plugins/higgsfield` |
| Other | `~/.<agent>/skills/higgsfield` |

Clone:

```bash
git clone https://github.com/higgsfield-ai/skills.git <path>
```

## Step 4 — Verify

Ask the agent (yourself):

> "Generate a tiny test image with Higgsfield."

Run `higgsfield generate create z_image --prompt "test" --wait`. The `--wait` flag blocks until the job finishes; confirm a URL is printed on stdout.

If anything fails:
- 401 / `Session expired` → repeat Step 2
- 4xx → check the error message; read `higgsfield-generate/references/troubleshooting.md`
- Network error → user's connectivity issue

## Step 5 — Done

Report to the user: "Skills installed. Try generating media, creating a complete brand identity, making a narrated explainer or YouTube thumbnail, building a browser game, or training a Soul Character."

Do NOT explain the internals (skill paths, file structure). Just confirm install + give starter prompts.
