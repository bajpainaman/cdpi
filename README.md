# cdpi

A lightweight skill that applies [Centre for DPI](https://docs.cdpi.dev/) thinking to **how software is built**,
for any system: protocols, contracts, APIs, apps, agents. It asks whether you are building rails others can build on,
or an end-to-end app.

Six playbooks, one router, and one standard-library Python CLI. No server, no dependencies.

| Command | Does |
|---|---|
| `lens` | Review a design, PR or schema against the five DPI principles |
| `unbundle` | Split a monolith into minimal blocks joined by open specs |
| `plus-one` | The smallest open, signed interface that makes an existing system reusable |
| `rails-check` | Rate how far a system is from infrastructure, as a maturity stage and not yes or no |
| `spec-first` | Write the protocol and schema contract before the code |
| `explain` | Rails vs apps, DPG vs DPI, the myths, execution habits |

## Install

```bash
npx skills add bajpainaman/cdpi
```

That uses the [skills CLI](https://github.com/vercel-labs/skills), which supports Claude Code, Codex, Amp, Cursor and 70+ other agents.
Add `-g` for a global install or `-a claude-code` to pick an agent.

Without Node:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/bajpainaman/cdpi/main/install)
```

The installer finds each agent's config folder on this machine (`~/.claude`, `~/.codex` or `~/.agents`, `~/.config/amp`,
`~/.cursor`, `~/.gemini` and others) and copies the skill into its skills folder. Then it fetches the pinned CDPI sources once.
Options: `--project` (install into `./.agents/skills` and `./.claude/skills`), `--list`, `--dry-run`, `--uninstall`.

After an npx install, run `cdpi sync` once from the skill's `bin/` folder, or just let the skill do it: it runs
`cdpi status` at session start and syncs when the sources are missing.

## CLI

```bash
skills/cdpi/bin/cdpi status                      # sources and commands
skills/cdpi/bin/cdpi route "review this PR that adds a central user DB"
skills/cdpi/bin/cdpi search "honeypot central database"
skills/cdpi/bin/cdpi show the-dpi-wiki/first-use-case-for-dpi.md
skills/cdpi/bin/cdpi show dpi-payments --section QR
skills/cdpi/bin/cdpi sync [--check]              # fetch pinned sources / compare pins with upstream
```

## Sources and licences

`sources.json` pins [centre-for-dpi/docs](https://github.com/centre-for-dpi/docs) (CC-BY-SA-4.0) and
[centre-for-dpi/ai-skills](https://github.com/centre-for-dpi/ai-skills) (no licence published). `sync` fetches
both into `~/.cache/cdpi`, and neither is committed here. The cards in `skills/cdpi/reference/` adapt the wiki and are CC-BY-SA-4.0
(see `skills/cdpi/reference/LICENSE.md`). The code is MIT.

## Test

```bash
python3 -m unittest discover -s tests
```
