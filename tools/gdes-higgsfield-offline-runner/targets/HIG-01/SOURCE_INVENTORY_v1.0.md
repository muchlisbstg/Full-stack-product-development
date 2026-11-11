# HIG-01 Pinned Source Inventory v1.0

**Repository:** `higgsfield-ai/skills`  
**Commit:** `27000402070db19d958789d05b3b52b6f4718d7c`  
**Tree:** `recursive Git tree, complete (truncated=false)`  
**Total tracked blobs:** 161  
**Inventory type:** path + Git blob SHA + risk mapping; not a complete byte-for-byte source archive.  
**Purpose:** identify the exact source paths requiring review/remediation for HIG-01 F02–F08.

## Confirmed scope from pinned tree

## Plugin manifests and agent policy

| Path | Git blob SHA |
|---|---|
| `.claude-plugin/plugin.json` | `1a9fa8e08f60c70c2875a02e1afe9e8108e22ffc` |
| `.codex-plugin/plugin.json` | `c861a0fba07ac9d829e71d4fcc4ab62324e23aa2` |
| `.cursor-plugin/plugin.json` | `c9ea573425467e695ca2344d20d091befc5aee24` |
| `CLAUDE.md` | `cc69a7e5677de73ebcd86a71c44749002e2bbbec` |
| `INSTALL_FOR_AGENTS.md` | `84ece725c6a896bfa9c8f5d4588913d1d2318a29` |
| `higgsfield-brandkit/agents/openai.yaml` | `4e91e1cd9a20be93881062c4fa94a6e9b48ba63f` |
| `higgsfield-youtube-thumbnail/agents/openai.yaml` | `bb40f59ae8e14acc98a706c773940f2d54d6c296` |

## Skill instructions / tool authority

| Path | Git blob SHA |
|---|---|
| `higgsfield-brandkit/SKILL.md` | `594a88c38c3ed79b3677be27a79b800f7f616b0a` |
| `higgsfield-faceless-video/SKILL.md` | `c6863c475687a29440eb376c27ddba9adb7362dc` |
| `higgsfield-generate/SKILL.md` | `3094e15be8934f077277636fd0f478d15644f252` |
| `higgsfield-marketplace-cards/SKILL.md` | `f6c2f27a587364388fbbdcfe0e2cf30342975fa0` |
| `higgsfield-product-photoshoot/SKILL.md` | `b5673d7fd76a0c422c6c54e32044261aee0767eb` |
| `higgsfield-soul-id/SKILL.md` | `d14cfc002f05e635a1c44600884a62592fdc0d0c` |
| `higgsfield-video-explainer/SKILL.md` | `662c9b7f0d8b64a9dc1cfec5324dc481da461953` |
| `higgsfield-websites/SKILL.md` | `c47acd761506555fe77732e40a2b52ed681dc7b7` |
| `higgsfield-youtube-thumbnail/SKILL.md` | `c8ccbee4217c38517c14a05b42118c5fa0863287` |

## Executable scripts

| Path | Git blob SHA |
|---|---|
| `higgsfield-brandkit/scripts/brandkit.py` | `d0f5c9a0f2386d0b2593d1e04e53574289e367a5` |
| `higgsfield-brandkit/scripts/build_brandbook.py` | `bcef68db6f3125c7a5ee40b0b12275b0da74a955` |
| `higgsfield-brandkit/scripts/render_brandbook_pdf.py` | `de83cca10ae9d733cda45a4ed693804e36f3630e` |
| `higgsfield-faceless-video/scripts/assemble_blocks.sh` | `341f908c815bbcf31e886dfb11f3f9e11a0808bd` |
| `higgsfield-faceless-video/scripts/assemble_final.sh` | `7689665685b6a245786e85f436e88a7164cc1425` |
| `higgsfield-faceless-video/scripts/assemble_partial_edit.sh` | `a92d57a39239e44829c3fa76e14556bcd1d7c5cd` |
| `higgsfield-faceless-video/scripts/assemble_slides.sh` | `8170936b412c852e3d908e3fc4b802e20020f14b` |
| `higgsfield-faceless-video/scripts/audio_to_captions.py` | `d9ccf71f72fe74899db22b38ec5b9778a96d479a` |
| `higgsfield-faceless-video/scripts/bind_scene_frame_results.py` | `bbb759dbaf381cce263a9c6f5c46bcb8eb837f9c` |
| `higgsfield-faceless-video/scripts/build_scene_timeline.py` | `32d49a13e11d9a479c7ed9c50d3e22645a8ea0d7` |
| `higgsfield-faceless-video/scripts/burn_captions.sh` | `4ac9e511c5069f4e6a0ed94830ba8303ee41b985` |
| `higgsfield-faceless-video/scripts/check_voice.sh` | `c322712ef82b75848073d392852c82bd57c4bf04` |
| `higgsfield-faceless-video/scripts/measure_narration_takes.py` | `10abc8f906eddc204536f23c83354b97192eff54` |
| `higgsfield-faceless-video/scripts/presenter_composite.sh` | `86ea01800310ab2ae97711a7a6f077aadd90f39c` |
| `higgsfield-faceless-video/scripts/speech_metrics.sh` | `fc02d0a6682524093e7c4ba1ce1607048b8fb31a` |
| `higgsfield-faceless-video/scripts/tests/test_assembly.py` | `713d6844cffe32d556eea73c06af6ea17f2d8b10` |
| `higgsfield-faceless-video/scripts/tests/test_captions.py` | `1490ae73af57356fa5e3e08fbb8d6518bc00d28b` |
| `higgsfield-faceless-video/scripts/tests/test_channel.py` | `32ab3953a24c9ee29c6962e48a852fb04b9ebb7f` |
| `higgsfield-faceless-video/scripts/tests/test_modes.py` | `8a45db4d3bf25b15e71d2ebd3c01d913a5b69c00` |
| `higgsfield-faceless-video/scripts/tests/test_song.py` | `47580411d4e203555fc889e2f36ad1c21a92fdd6` |
| `higgsfield-faceless-video/scripts/tests/test_timeline.py` | `aa761761ff5f0bc85c93651222b3d1b069390244` |
| `higgsfield-faceless-video/scripts/trim_static_head.sh` | `81204eb9395dbdf858ba8468aa5b7878464d4d4a` |
| `higgsfield-faceless-video/scripts/validate_motion_script.py` | `12a6e5d8b1813ae269152dcd5bec5d02b1bf598d` |
| `higgsfield-faceless-video/scripts/validate_song_prompt.py` | `a7dccc7f51718c7ac0d34cd4c6016437e3353770` |
| `higgsfield-websites/scripts/fbx2glb.py` | `6ab4467100ecbc36b4f86f576155f52e01ba6985` |
| `higgsfield-websites/scripts/glb_inspect.py` | `f332d3d50e46afa28a27ac040d383de8c5637599` |
| `higgsfield-websites/scripts/glb_merge_anims.py` | `abb4e8034537782b0fd473739ae7a634fef557bd` |
| `higgsfield-websites/scripts/glb_patch.py` | `34d1d34f2e7fdbadb41a1c17ca552c88621fd17a` |
| `higgsfield-websites/scripts/merge_anim_glbs.py` | `93709e4ba8854a84396b03551f6077706d3399f0` |
| `higgsfield-websites/scripts/pipeline.py` | `dc673100e5c691ee3a7ca39d785fe3c89c22a80c` |
| `higgsfield-websites/scripts/proc_anim_dragon.py` | `6c7bb9cc0c9bd2c1a85721b11dba3f2ef8973fff` |
| `higgsfield-websites/scripts/proc_rig_dragon.py` | `fe429f10c3bd3630f8e76399fec33809c1298fe8` |
| `higgsfield-websites/scripts/proc_weights.py` | `610238fcb8f61525f60413ab62dbafbdb6b4f2ef` |
| `higgsfield-websites/scripts/rig_transfer.py` | `3390d7a78360f24ca6b9c879077833242bb2b71e` |
| `higgsfield-websites/scripts/seamless.py` | `5e1ab746aaeb2423d9dd324eae475d67c8f6b906` |
| `scripts/update-check.sh` | `1e6f2496e3fce4217ea2d7dd5c67e5af77d6ac4b` |
| `setup` | `b8ff4a0f658a99d524c4fe6b4d5a020b7b864934` |

## Network, SSRF, upload, Meshy and security references

| Path | Git blob SHA |
|---|---|
| `higgsfield-generate/references/marketing-products.md` | `2ef1624bfad5e48fe3ec6a76807a41752e778732` |
| `higgsfield-generate/references/marketing-setup-items.md` | `dee2c0fed982e008495f562a23109677c4b05952` |
| `higgsfield-generate/references/media-inputs.md` | `4fc6eee5ace0a377b5bcf0b86a732dcc46f7c779` |
| `higgsfield-generate/references/workflows.md` | `a09d2b644f1376930b2eb3b3f79f0c615f4982f3` |
| `higgsfield-websites/references/auth.md` | `ecf612d544dcd20b969672e8ff46b0697fccf055` |
| `higgsfield-websites/references/game-meshy-api.md` | `60e6c147b57ad218144543de2c2b0959493cafc0` |
| `higgsfield-websites/references/game-meshy-input-rules.md` | `1b5ad773917b47d59c09c86c0b9fd239b5610fb1` |
| `higgsfield-websites/references/runtime-and-infra.md` | `4e0f3d2cb09a4f23d4f803b234800fb9bd382748` |
| `higgsfield-websites/references/security.md` | `ebee091263ad1a04ef765707f7ada488fa1807ad` |
| `higgsfield-websites/references/website-flow.md` | `ea8ae48fab9ea11b474c2dea9465a40d35e0e3bc` |

## SVG and asset parsing

| Path | Git blob SHA |
|---|---|
| `assets/icon.svg` | `d78a91803bcab850ade83e6833daeb3eaff8710e` |
| `higgsfield-brandkit/scripts/brandkit.py` | `d0f5c9a0f2386d0b2593d1e04e53574289e367a5` |
| `higgsfield-websites/scripts/glb_inspect.py` | `f332d3d50e46afa28a27ac040d383de8c5637599` |
| `higgsfield-websites/scripts/glb_merge_anims.py` | `abb4e8034537782b0fd473739ae7a634fef557bd` |
| `higgsfield-websites/scripts/glb_patch.py` | `34d1d34f2e7fdbadb41a1c17ca552c88621fd17a` |
| `higgsfield-websites/scripts/pipeline.py` | `dc673100e5c691ee3a7ca39d785fe3c89c22a80c` |

## Evaluation and validation

| Path | Git blob SHA |
|---|---|
| `.github/workflows/validate-skills.yml` | `38813b6834b40b3da96aeb4afdb7aa3f72882d07` |
| `evals/README.md` | `4e5c93023f1855e508790b182add261e606f7762` |
| `evals/scenarios.md` | `e1e0d2df5af7140187cc89465341d1e701e2da3d` |
| `higgsfield-faceless-video/scripts/tests/test_assembly.py` | `713d6844cffe32d556eea73c06af6ea17f2d8b10` |
| `higgsfield-faceless-video/scripts/tests/test_captions.py` | `1490ae73af57356fa5e3e08fbb8d6518bc00d28b` |
| `higgsfield-faceless-video/scripts/tests/test_channel.py` | `32ab3953a24c9ee29c6962e48a852fb04b9ebb7f` |
| `higgsfield-faceless-video/scripts/tests/test_modes.py` | `8a45db4d3bf25b15e71d2ebd3c01d913a5b69c00` |
| `higgsfield-faceless-video/scripts/tests/test_song.py` | `47580411d4e203555fc889e2f36ad1c21a92fdd6` |
| `higgsfield-faceless-video/scripts/tests/test_timeline.py` | `aa761761ff5f0bc85c93651222b3d1b069390244` |

## Finding-to-source mapping

### F02 — Agent tool authority / Bash scope
- All eight `*/SKILL.md` files must be reviewed for `allowed-tools`, Bash grants, shell execution instructions, and escalation boundaries.
- Agent/plugin metadata: `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.cursor-plugin/plugin.json`, `higgsfield-brandkit/agents/openai.yaml`, `higgsfield-youtube-thumbnail/agents/openai.yaml`, `CLAUDE.md`, `INSTALL_FOR_AGENTS.md`.
- Executable surface includes every shell/Python script under `higgsfield-*/scripts/`, root `setup`, and `scripts/update-check.sh`.

### F03 — Network/provider side effects and consent
- `higgsfield-generate/SKILL.md`, `higgsfield-product-photoshoot/SKILL.md`, `higgsfield-marketplace-cards/SKILL.md`, `higgsfield-soul-id/SKILL.md`, `higgsfield-youtube-thumbnail/SKILL.md`, `higgsfield-websites/SKILL.md`.
- `higgsfield-faceless-video/scripts/assemble_blocks.sh` (remote URL fetch via curl), `higgsfield-websites/references/game-meshy-api.md` (Meshy API polling/upload workflow), plus all scripts listed above for subprocess/network side effects.
- Installer commands recur in multiple skill instructions, not just root `setup`: the source contains mutable `curl ... cli/main/install.sh | sh` patterns in generate, marketplace-cards, product-photoshoot, soul-id, websites and youtube-thumbnail instructions.

### F04 — URL fetch / SSRF / DNS rebinding
- `higgsfield-websites/references/security.md` includes outbound fetch/SSRF threat model and examples.
- `higgsfield-websites/SKILL.md`, `higgsfield-generate/SKILL.md`, `higgsfield-websites/references/game-meshy-api.md`, `higgsfield-faceless-video/scripts/assemble_blocks.sh`, `higgsfield-faceless-video/scripts/assemble_slides.sh`, and all URL-taking scripts/flows need call-site inventory.
- The current pinned tree has no obvious standalone server-side URL-fetch implementation in the skill scripts; the runtime platform may own some fetch behavior. Do not claim DNS pinning remediation until the actual fetch implementation is identified.

### F05 — Reproducible evaluation
- `evals/README.md`, `evals/scenarios.md`, `.github/workflows/validate-skills.yml`, and `*/scripts/tests/`.
- Existing eval scenarios are instructions/scenarios, not by themselves a hermetic security test harness.

### F06 — Meshy integration and secret/cost controls
- `higgsfield-websites/references/game-meshy-api.md` is the primary Meshy API workflow reference.
- `higgsfield-websites/references/game-meshy-input-rules.md` defines request inputs.
- `higgsfield-websites/SKILL.md` links to the Meshy workflow.
- Search all script and instruction paths for `MESHY_API_KEY`, `api.meshy.ai`, `Authorization: Bearer`, and task POST/GET/DELETE operations before closing.

### F07 — SVG/XML parsing
- Tracked asset: `assets/icon.svg`.
- Relevant candidate source includes `higgsfield-brandkit/scripts/brandkit.py`, `higgsfield-brandkit/scripts/build_brandbook.py`, `higgsfield-brandkit/scripts/render_brandbook_pdf.py`, `higgsfield-websites/scripts/pipeline.py`, `higgsfield-websites/scripts/glb_inspect.py`, and all scripts that ingest or emit SVG/GLB/HTML/XML.
- Current evidence does not yet establish a concrete untrusted SVG/XML parser entry point. Identify imports and parse callsites before proposing a parser-specific patch; do not add a generic dependency without a confirmed parser surface.

### F08 — Skill count / metadata parity
- `README.md`, `INSTALL.md`, `CLAUDE.md`, `INSTALL_FOR_AGENTS.md`, plugin manifests, `VERSION`, `CONTRIBUTING.md`, and actual top-level `higgsfield-*/SKILL.md` directories.
- Reconcile declared skill count against actual tracked skill directories and plugin manifest registrations.

## Evidence and limitations

- Git blob SHA values are copied from the pinned commit's recursive tree. They identify the exact Git objects but are not SHA-256 file digests.
- This inventory records all 161 tracked file paths and hashes from the pinned tree, but does not yet archive all 161 file bodies into the isolated runner.
- Source-level claims above are initial triage mappings based on the pinned tree and selected source reads. Full callsite review remains open.
- Binary assets (e.g. `assets/logo.png`) are identified by tree entry only; the text-only runner must not attempt to parse them as UTF-8.
- Do not execute any candidate source. Continue using inert text-only scans and synthetic tests.
