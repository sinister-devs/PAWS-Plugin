# Account setup completion

- DECIDED [operator]: Show a PAWS completion screen and wait for Ready or a problem report before continuing setup.
- DECIDED [agent]: Keep the native client OAuth callback; open the PAWS completion screen only after the client confirms success. Callback HTML is client-owned.
- DECIDED [agent]: Version 0.2.3 isolates revised setup instructions from the installed 0.2.2 cache; no credentials or executable runtime added.
- REJECTED: Replace or proxy authorization-code handling to style the callback; unnecessary security and support surface.
- ASSUMED: The host exposes a question/wait capability; otherwise setup must report that limitation rather than simulate waiting.

Validation: seven public package checks passed. Real active-wait behavior with native OAuth remains a recipient check. The web completion route is delivered by the application deployment; the existing native confirmation remains usable before that deployment.
