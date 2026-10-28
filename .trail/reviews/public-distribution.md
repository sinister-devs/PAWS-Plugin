# Public release checkpoint

Scope: only public plugin, catalogs, documentation, asset and package checks. Fresh repository; no pre-existing dirty files. App/backend/Core and private Git history excluded.

Authority: operator requested public distribution, cross-host installation and immediate integration of verified changes. Publishing this repo is authorized; production app deployment is separate. Follow the share-agent and verification-before-completion workflows.

Acceptance: anonymous repository download; only allowed public content; host manifests resolve; Codex installation and profile evidence; clear recipient prompts. Windows/Linux and Claude native OAuth remain separate user walkthrough checks.

Progress: source assembled from current released plugin; source version 0.2.2. Publication and installation evidence is retained in the delivery report outside the runtime package.

Craft matrix: P = static pass, N/A = non-skill procedural/discovery checks do not apply. Behavior remains separately unverified unless observed.

| File | C1 | C2 | C3 | C4 | C5 | C6 | C7 | Evidence |
|---|---|---|---|---|---|---|---|---|
| plugins/paws-app/skills/setup/SKILL.md | P | P | P | P | P | P | P | Steps 1–3 and completion bound; corrected browser origin; new-chat fallback; real profile required. |
| plugins/paws-app/skills/investigate/SKILL.md | P | P | P | P | P | P | P | Steps 1–6 and completion bound; evidence and human decision boundaries preserved. |
| plugins/paws-app/plugin.json | N/A | P | N/A | P | P | P | P | Existing portable manifest; aligned version and resolved onboarding/icon paths. |
| plugins/paws-app/.codex-plugin/plugin.json | N/A | P | N/A | P | P | P | P | Existing compatibility manifest; local loader checked separately. |
| plugins/paws-app/.claude-plugin/plugin.json | N/A | P | N/A | P | P | P | P | Existing host branch preserved; native invocation not claimed. |
| plugins/paws-app/mcp.json | N/A | P | N/A | P | N/A | P | P | Remote endpoint only; no command/env/headers. |
| plugins/paws-app/.codex-mcp.json | N/A | P | N/A | P | N/A | P | P | Same endpoint; host-specific http type. |
| plugins/paws-app/.mcp.json | N/A | P | N/A | P | N/A | P | P | Same endpoint; host-specific http type. |
| plugins/paws-app/assets/icon.png | N/A | N/A | N/A | P | N/A | N/A | P | Approved asset, exact hash checked. |
| plugins/paws-app/README.md | P | P | P | P | N/A | P | P | Package-specific guide; host installation authority is root docs. |
| .agents/plugins/marketplace.json | N/A | P | N/A | P | P | P | P | Relative source, one plugin, existing policies. |
| .claude-plugin/marketplace.json | N/A | P | N/A | P | P | P | P | Same package and identity. |
| README.md | P | P | P | P | N/A | P | P | Primary recipient route and separate source/live checks. |
| INSTALL_PROMPT_RU.md | P | P | P | P | N/A | P | P | Current-host branch; prerequisite and failure stops; no secrets requested. |
| docs/INSTALLATION.md | P | P | P | P | N/A | P | P | Exact IDs and current official references; limits explicit. |
| docs/SECURITY.md | N/A | N/A | P | P | N/A | P | P | Public data flow and access boundary; no overclaimed security proof. |
| tests/test_package.py | P | P | N/A | P | N/A | P | P | Safety and package invariants; not a behavioral evaluation. |
| .github/workflows/package.yml | P | P | N/A | P | N/A | P | P | Independent OS matrix, no private dependencies. |
| .gitignore | N/A | N/A | N/A | P | N/A | P | P | Only generated Python/macOS artifacts excluded. |
| .trail/entries/001-public-distribution.md | N/A | P | P | P | N/A | P | P | Decisions attributed; no private request or personal data copied. |
| .trail/reviews/public-distribution.md | P | P | P | P | N/A | P | P | Scope, gates and next action recoverable. |

Cuts: replaced old ZIP/private-source recipient instructions with one public installation route. Unchanged investigation rules preserved to avoid altering the evidence contract. Setup retains explicit consent and successful-profile gate.

Next: run package checks, audit the complete tracked tree, publish and verify anonymous retrieval. Keep live-client results separate from this static matrix.
