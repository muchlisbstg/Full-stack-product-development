---
version: 0.14.0
name: higgsfield-soul-id
description: |
  Train a Soul Character — a personalized model on a person's face that
  Higgsfield uses for identity-faithful image and video generation.
  Use when: "create my Soul", "train my face", "make my digital twin",
  "build me an avatar", "learn my appearance", "create a character of me",
  "set up identity for video", "I want my face in generated images".
  Chain: train Soul (one-time, returns reference_id) → use in
  higgsfield-generate via `--soul-id <id>` with models like
  `text2image_soul_v2` or `soul_cinematic`.
  NOT for: one-shot face swaps (use higgsfield-generate with --image),
  named-character / non-photo avatars (use higgsfield-generate with prompt).
argument-hint: "[name] [photo paths...]"
---

## Execution authority and approval boundary

This skill does not grant the agent shell access. Do not infer permission to run Bash, a terminal, a script, or the Higgsfield CLI from the presence of command examples in this document.

- Treat every command below as reference syntax for the user unless the user explicitly authorizes the specific execution in the current task.
- Before executing any command, state the exact command, working directory, expected local files changed, and whether it contacts a network service or incurs a charge; wait for explicit approval.
- Do not execute installers, shell scripts, generated scripts, commands copied from remote content, or commands that invoke `eval`, `source`, or shell interpolation without a separate explicit approval.
- Do not use `sudo`, modify system directories, change shell startup files, alter PATH, install packages, or change permissions/ownership.
- Do not run destructive or broad filesystem commands (including recursive delete, overwrite, move, or bulk chmod/chown). Require a separate explicit approval naming the exact paths and operation.
- Do not execute repository-provided scripts merely because a workflow references them. Inspect the complete script and its dependencies first.
- Prefer non-executing file inspection. When execution is approved, use the host's least-privilege sandbox and approval controls; never attempt to bypass them.
- If the host cannot provide the required sandbox or approval boundary, stop and provide the command for the user to run manually.



# Higgsfield Soul Character

Train a face-faithful identity model. Reusable across all Soul-powered generations.

## Step 0 — Bootstrap

Before any other command:

1. If `higgsfield` is not on `$PATH`, install it:
   ```bash
   curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
   ```
2. If `higgsfield account status` fails with `Session expired` / `Not authenticated`, ask the user to run `higgsfield auth login` (interactive) and wait for confirmation.
3. Soul training requires a paid plan (Basic+). If `higgsfield account status` shows free plan, tell the user before submitting.

## UX Rules

1. Be concise. No raw IDs in chat. Just say "Soul ready" with a name reference.
2. Detect language and respond in it. CLI flags stay English.
3. Ask for the smallest set of inputs: name + photos. Pick a sensible model variant.
4. Polling is silent — training takes minutes. Don't repeat status updates.

## Workflow

1. **Get name.** One word, used for later reference. Ask if missing.
2. **Get photos.** 5–20 face photos, varied angles and lighting. Local paths or already-uploaded IDs both work — `--image` accepts either.
3. **Pick variant.**
   - `--soul-2` — for image generation (default)
   - `--soul-cinematic` — for cinematic / video work
   Choose based on user's stated downstream use. Default to `--soul-2`.
4. **Submit.**
   ```bash
   higgsfield soul-id create --name "<name>" --soul-2 --image ./photo1.png --image ./photo2.png ...
   higgsfield soul-id create --name "<name>" --soul-2 --image <upload_id> --image <upload_id> ...
   ```
   CLI auto-uploads paths. Captures returned reference id.
5. **Wait.** `higgsfield soul-id wait <id>`. Silent. Default timeout 30m.
6. **Deliver.** "Soul `<name>` ready. Use in generate with `--soul-id <id>`."

## Use the Soul

Once trained, pass to `higgsfield-generate`:

```bash
higgsfield generate create text2image_soul_v2 --prompt "..." --soul-id <ref_id> --quality 2k --wait
higgsfield generate create soul_cinematic --prompt "..." --soul-id <ref_id> --quality 2k --wait
```

`--soul-id` is sent as the model's `custom_reference_id`. For a curated Soul style, list styles with `higgsfield preset list soul-v2` and pass the chosen id as `--style_id` on `text2image_soul_v2`. `--style_id` cannot be combined with `--image`.

## Listing existing Souls

```bash
higgsfield soul-id list                   # all references
higgsfield soul-id get <id>               # one by id
```

## Errors

- `Minimum Basic plan required` — user is on free plan; tell them.
- `Training failed` — check photos quality (5+ unique faces, well-lit).
- `Session expired` → `higgsfield auth login`.

## Reference docs

- `references/photo-guide.md` — what photos work best
- `references/troubleshooting.md` — common training failures
