# Spike: Zed git panel capabilities and GitHub auth flow — 2026-07-12

**Purpose:** Session X moves students from browser notebooks to local
development (uv + Zed + git + GitHub, working in pairs on a project repo).
The course teaches git primarily through **Zed's git panel**, with terminal
equivalents shown alongside. Before the lecture deck and
`general/git-basics.qmd` state anything about "click X in Zed to push to
GitHub," this spike verifies, from current Zed docs and a local check, what
Zed's git panel actually supports and how a push authenticates — so the
downstream materials state verified facts, not guesses.

## Findings — Zed git panel operations (July 2026)

Source: [Zed Editor Git integration documentation](https://zed.dev/docs/git)
(fetched 2026-07-12) and [Zed all-actions reference](https://zed.dev/docs/all-actions)
(fetched 2026-07-12). The `/docs/git` page's own "Action Reference" table is a
curated subset; the full `/docs/all-actions` page is the authoritative list of
every `git::*` action and was cross-checked for anything the curated table
omitted.

| Operation | Supported in Zed's git panel? | Notes |
|---|---|---|
| Stage / unstage (file or hunk) | **Yes** | `git: stage all`, `git: stage and next`, per-hunk staging in Project Diff (`ctrl-g d`). |
| Commit | **Yes** | `git: commit` (`cmd-enter`/`ctrl-enter`), AI-generated commit messages optional. "Uncommit" button runs `git reset HEAD^ --soft`. |
| Push | **Yes** | `git: push` (`ctrl-g up`), `git: force push`. Respects `pushRemote`/`remote.pushDefault`/tracking remote, same order as plain `git push`. |
| Pull | **Yes** | `git: pull` (`ctrl-g down`), `git: pull rebase`. |
| Fetch | **Yes** | `git: fetch` (`ctrl-g ctrl-g`), `git: fetch from` (specific remote). |
| Branch (create/switch/delete) | **Yes** | `git: branch`, `git: switch`, `git: checkout branch`. Cannot delete the currently checked-out branch. |
| Clone | **Yes, but not in the curated docs table** | `git::Clone` action exists (`git: clone` in the command palette), listed only on `/docs/all-actions`. Added by [PR #35606](https://github.com/zed-industries/zed/pull/35606), merged 2025-08-11 ("git: Add ability to clone remote repositories from Zed"). Confirmed via [Discussion #26513](https://github.com/zed-industries/zed/discussions/26513): a maintainer confirmed "Zed has the ability to clone repositories." |
| Init | **Yes, but not in the curated docs table** | `git::Init` action exists ("Initializes a new git repository"), listed only on `/docs/all-actions`. |
| Create remote | **Yes** | `git::CreateRemote` ("Create a git remote") — needed after `git: init` + `git: clone`-free local start, since `git: init` alone doesn't attach a GitHub remote. |
| Create pull request | **Yes** | `git::CreatePullRequest` ("Creates a pull request for the current branch"). |
| "Publish to GitHub" (VS-Code-style one-click: create the remote repo on GitHub + push) | **No** | No such action exists in `/docs/all-actions` (searched for "publish", "create repository", "new repository" — no matches). Creating the GitHub-side repo is not a Zed action; students must create the repo on github.com (or via `gh repo create`) and then `git: create remote` + `git: push` from Zed. |
| Worktrees, stash, merge-conflict UI | Yes (out of scope for this course but exist) | Not relevant to Session X. |

**Implication for Session X:** `git: init` and `git: clone` exist as Zed
actions, so a pure-Zed workflow is technically possible for both "start a new
repo" and "clone an existing repo." But there is no in-Zed action that
creates the GitHub-side repository — that step happens on github.com (or via
`gh repo create` in the terminal) regardless of which git client is used
afterward.

## Findings — GitHub authentication for push

Source: [Authenticate with Zed](https://zed.dev/docs/authentication) (fetched
2026-07-12).

Zed's built-in "Sign In" (`client: sign in`, GitHub OAuth) is **explicitly
scoped to two features only**: real-time collaboration, and Zed-hosted LLM
features. Quoting the doc directly:

> "What Features Require Signing In? All real-time collaboration features.
> LLM-powered features, if you are using Zed as the provider of your LLM
> models."
>
> "Zed uses GitHub's OAuth flow to authenticate users, requiring only the
> `read:user` GitHub scope, which grants read-only access to your GitHub
> profile information."

`read:user` is read-only profile access — it cannot authorize `git push`,
which needs GitHub's `repo` scope (or SSH key / PAT with write access) applied
to *git itself*, not to the Zed app. Git operations in the git panel are not
listed among the sign-in-gated features at all: **Zed's git panel works, and
is documented to work, without ever signing in to Zed.** This means Zed's
account sign-in and git's push/pull authentication are two independent
systems — signing in to Zed does **not** configure git's credential helper or
otherwise authorize pushes.

This is corroborated by real-world reports on Zed's own GitHub repo:

- [Issue #52218 — "Getting prompted for GitHub login despite having
  git-credential-manager etc."](https://github.com/zed-industries/zed/issues/52218)
  (fetched 2026-07-12): a user who was signed into Zed via GitHub OAuth *and*
  had `git-credential-manager` configured still hit HTTPS credential prompts
  on push — i.e., being signed in to Zed's account did not substitute for a
  working git credential helper. Closed "not planned" (no fix), confirming
  this is expected behavior, not a bug that will be resolved before the
  course runs.
- [Discussion #50145 — "Automatic Sharing of GitHub CLI credentials or Git
  Credentials Manager credentials"](https://github.com/zed-industries/zed/discussions/50145)
  (fetched 2026-07-12): confirms Zed does not auto-share local git credentials
  even across its own remote-development feature, reinforcing that git
  credential setup is the user's/system's responsibility, separate from the
  Zed app account.

**Verdict: push authentication is entirely a system-git-credentials problem,
not a Zed problem.** A fresh Zed install, even signed in with GitHub, cannot
push until the machine's git is configured with a credential helper (HTTPS)
or an SSH key registered on GitHub. The standard, low-friction way to get a
working HTTPS credential helper on a fresh machine is `gh auth login`
followed by `gh auth setup-git`, per [GitHub CLI's own
docs](https://cli.github.com/manual/gh_auth_login) and [GitHub's "Caching
your GitHub credentials in
Git"](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git)
(both general web knowledge, not independently re-fetched in this spike —
flagged below for a link-rot check before semester).

## Local check — does `uv init` create a git repo?

Ran in `/private/tmp` (outside the course repo), deleted afterward:

```
$ uv --version
uv 0.11.25 (Homebrew 2026-06-26 aarch64-apple-darwin)

$ uv init spike-test
Initialized project `spike-test` at `/private/tmp/spike-test`

$ ls -a spike-test
.git/
.gitignore  109B
.python-version  5B
README.md  0B
main.py  88B
pyproject.toml  156B
```

**Verdict: yes — `uv init <dir>` initializes a git repository by default**
(a `.git/` directory is created alongside `.gitignore`, `.python-version`,
`README.md`, `main.py`, `pyproject.toml`). This was tested with the Homebrew
build of uv 0.11.25 on 2026-07-12; it is `uv`'s own documented default
behavior (`uv init` runs `git init` unless `--no-workspace`/`--vcs none` is
passed or the directory is already inside a repo), not a Zed feature.

**Implication for Session X:** the course's Session X flow does **not** need
a separate `git: init` / `git init` step for the "start a new project"
branch — running `uv init <project>` already produces a git repo. `git: init`
in Zed (or `git init` in the terminal) is only needed for the (rarer in this
course) case of turning an *existing*, non-uv, non-git directory into a repo.
The "clone an existing repo" branch (partner already created the GitHub repo)
still uses `git: clone` / `git clone`, not `uv init`.

## Decision

The primary auth path for students is **`gh auth login` run once per machine
during setup**, before any Zed git panel use. Rationale, per the "prefer the
robust path" instruction: Zed's own GitHub sign-in verifiably does not cover
git push auth (scoped to `read:user` only, per Zed's docs, and independently
confirmed as a real friction point in issue #52218 even for a user signed
into Zed). `gh auth login` is a single terminal command, works identically on
macOS/Windows/Linux, configures git's HTTPS credential helper
(`gh auth setup-git`, which `gh auth login` offers to run automatically), and
is the credential path GitHub's own docs recommend for HTTPS. SSH key setup
was not adopted as the primary path because it requires generating a keypair
and pasting a public key into GitHub's settings — more steps for a
business-student audience with no prior dev-tooling experience than the
`gh auth login` browser-code flow.

## Copy for authors

Use this verbatim as the basis for the git-basics guide's "GitHub setup &
auth" section and the lecture's setup bullet. It is self-contained — no need
to re-read the Findings above to write correct student-facing instructions.

**One-time machine setup, before first use of Zed's git panel:**

1. Install the GitHub CLI (`gh`) if not already present.
2. Run `gh auth login` in a terminal. Choose GitHub.com, HTTPS as the
   preferred protocol, and authenticate via the browser (device code) flow.
   When asked "Authenticate Git with your GitHub credentials?", answer yes —
   this runs `gh auth setup-git` for you and configures git's HTTPS
   credential helper.
3. Confirm with `gh auth status` — it should show "Logged in to github.com"
   and "Git operations for github.com configured to use https protocol."
4. Separately, sign in to the Zed app itself (`client: sign in` in the
   command palette, or the Sign In button) if collaboration or Zed-hosted AI
   features are wanted. **This sign-in is unrelated to git push
   authentication and does not need to happen for git operations to work** —
   do not present it as a git auth step.

**Starting a project (two cases):**

- New project: `uv init <project-name>` in a terminal (this already creates
  a `.git/` repo — no separate `git init` needed). Then create an empty
  repository on github.com (or `gh repo create`), and in Zed use
  `git: create remote` to point the local repo at it, then `git: push`
  (first push needs `-u`/upstream tracking set — Zed's push handles this,
  but if using the terminal instead, `git push -u origin main`).
- Joining a partner's existing repo: use Zed's command palette `git: clone`
  (or terminal `git clone <url>`) with the HTTPS URL of the GitHub repo. No
  `uv init` or `git init` needed — the clone brings the existing project and
  its `.git/` history.

**Day-to-day work, entirely inside Zed's git panel:** stage (`git: stage
all` or per-file checkboxes), commit (`git: commit`, `cmd/ctrl-enter`), pull
before starting work (`git: pull`), push when done (`git: push`). Terminal
equivalents (`git add`, `git commit`, `git pull`, `git push`) should be shown
alongside each, since Zed's panel is a UI over the same operations and
students will see both in videos/screenshots from other sources.

**If a push is rejected with a credential prompt or fails silently:** this
means step 2 above (`gh auth login` / `gh auth setup-git`) was not completed
correctly on that machine — re-run `gh auth login`, not the Zed sign-in.

## Verify-live-before-semester list

These items either came from secondary sources (community wiki/GitHub
discussion summaries rather than primary docs text I read myself), or are
time-sensitive UI details that could drift before the course runs. Re-check
close to semester start:

- **Exact button/menu wording and location** for `git: create remote` and
  `git: push` in the Zed git panel UI (I confirmed the actions exist and
  their descriptions via `/docs/all-actions`, but did not have a live Zed
  install to screenshot the actual panel buttons/menus for this spike).
- **`gh auth login` and `gh auth setup-git` exact prompts/wording** — cited
  from general knowledge of the GitHub CLI flow and search-result summaries
  of `cli.github.com/manual/gh_auth_login`, not a fresh fetch-and-read of
  that manual page's full text in this spike.
- **Whether Zed's first push from a freshly-`git: create remote`d repo
  auto-sets the upstream tracking branch**, or whether students need an
  extra "set upstream" step/prompt the first time — not explicitly stated in
  the `/docs/git` page text captured here.
- **`uv init` default VCS behavior across uv versions** — this spike used uv
  0.11.25 (Homebrew, 2026-07-12 install). If the course's documented uv
  install path (e.g., the official installer script vs. Homebrew) pins a
  different version, re-run the `uv init spike-test && ls -a spike-test`
  check with that exact install.
- **Corporate/campus network firewall behavior** for `zed.dev`/`collab.zed.dev`
  (mentioned in Zed's auth docs as a known blocker on some corporate
  networks) and for `github.com`'s OAuth device-code flow used by
  `gh auth login` — worth a quick check on the university's network before
  the lab session, per the existing corporate-firewall caveat in Zed's own
  docs.
