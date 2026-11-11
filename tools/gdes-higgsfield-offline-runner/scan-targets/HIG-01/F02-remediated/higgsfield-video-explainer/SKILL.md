---
version: 0.14.0
name: higgsfield-video-explainer
description: |
  Compatibility entry for the former video explainer skill. Use when: the user explicitly invokes higgsfield-video-explainer or continues its existing workflow. NOT for: new generic explainer requests, ads, single clips, or unrelated video edits.
argument-hint: "[topic or source files] [duration] [language] [aspect ratio]"
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



# Video explainer

Use the `higgsfield-faceless-video` skill for this request and select its illustrated explainer workflow. Preserve the user's inputs and choices. If that skill is not installed, ask the user to update or install the current Higgsfield skills package before generating any assets. Do not use `explainer_video` or `video_explainer`.
