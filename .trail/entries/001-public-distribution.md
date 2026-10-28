# PAWS public distribution

## Task
Prepare a separate public plugin repository and simple Russian onboarding for Codex and Claude Code across desktop operating systems.

## Decisions
- DECIDED [operator]: Publish only the application plugin; keep application, server, Core, credentials and product internals private. GitHub membership must not be required.
- DECIDED [operator]: Access to PAWS is granted by the existing PAWS account and role, with user approval in the browser.
- DECIDED [agent]: Start new Git history from an explicit file allowlist, preserving paws-app@paws-app identity and host-specific manifests.
- DECIDED [agent]: Use version 0.2.2 for corrected setup guidance and separate distribution. No new server permissions or runtime code are introduced.

## Rejected
- REJECTED: Forking the private app history — unnecessary risk of publishing unrelated source or secrets.
- REJECTED: Embedded credentials, local server installers or duplicate manual MCP registration — contradicts the account-based setup and makes support harder.

## Assumed
- ASSUMED: Users have a supported AI client and permitted PAWS staff account; otherwise onboarding stops at the missing prerequisite.

## Not done
- Real Windows/Linux OAuth and Claude Code user walkthroughs require separate verification. Static package checks do not establish those results.
