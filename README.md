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
./install            # copies to ~/.claude/skills/cdpi and ~/.agents/skills/cdpi, then syncs sources
```

## CLI

```bash
bin/cdpi status                      # sources and commands
bin/cdpi route "review this PR that adds a central user DB"
bin/cdpi search "honeypot central database"
bin/cdpi show the-dpi-wiki/first-use-case-for-dpi.md
bin/cdpi show dpi-payments --section QR
bin/cdpi sync [--check]              # fetch pinned sources / compare pins with upstream
```

## Sources and licences

`sources.json` pins [centre-for-dpi/docs](https://github.com/centre-for-dpi/docs) (CC-BY-SA-4.0) and
[centre-for-dpi/ai-skills](https://github.com/centre-for-dpi/ai-skills) (no licence published). `sync` fetches
both into `~/.cache/cdpi`, and neither is committed here. The cards in `reference/` adapt the wiki and are CC-BY-SA-4.0
(see `reference/LICENSE.md`). The code is MIT.

## Test

```bash
python3 -m unittest discover -s tests
```
