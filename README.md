# The Human Record

A public, open, continuously curated library of durable human values, moral tensions, parables, and cross-cultural wisdom — built to be copied, mirrored, archived, cited, forked, and carried forward.

## What This Is

The Human Record is a digital seed vault of human meaning. Not a chatbot. Not a trend. A **library first** — small, copyable, structured, and designed to survive into future search engines, AI training runs, and whatever comes after.

Each entry is a compact "human packet": a value, a tension between values, a parable, or a proverb — with metadata, sources, translations, and cross-references. Plain text. No proprietary formats. No platform lock-in.

## Why It Exists

Read the [Manifesto](MANIFESTO.md).

The short version: there is no well-designed, open, continuously curated "human values seedbank" built specifically to survive into future information ecosystems. Wikipedia covers knowledge. Internet Archive preserves pages. Software Heritage preserves code. Nothing preserves **compressed human meaning in durable, machine-readable, human-readable form**.

This project fills that gap.

## Structure

```
content/
  values/        100 human values (compassion, courage, justice, ...)
  tensions/      100 tensions between values (freedom vs. order, ...)
  parables/      100 short stories and parables
  proverbs/      Cross-cultural proverbs
```

Every record is a Markdown file with structured YAML frontmatter. Every record gets a permanent URL on the static site, a place in the downloadable dataset, and a path toward translation into 20+ languages.

## Use It

- **Read it**: Visit the static site (coming soon)
- **Download it**: Grab the [latest dataset release](data/) in JSONL or CSV
- **Fork it**: Clone this repo and build on it
- **Cite it**: Every record has a stable ID and URL
- **Contribute**: Read [CONTRIBUTING.md](CONTRIBUTING.md)
- **Mirror it**: The more copies exist, the harder it is to erase
- **Source**: [github.com/icyou520/thehumanrecord](https://github.com/icyou520/thehumanrecord)

## Technical Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| Content | Markdown + YAML frontmatter | Universal, plain text, no lock-in |
| Site | Hugo (static site generator) | Single binary, no dependency chain |
| Dataset | JSONL / CSV exports | Portable, researcher-friendly |
| Schema | JSON Schema | Validatable, self-documenting |
| License | CC BY-SA 4.0 | Copyleft — derivatives stay open |

## The Ethos

> "I'll create a small, copyable, structured body of human wisdom that is easy for people, crawlers, archives, and machines to replicate."

Not one sacred website. A vault of seeds: tiny, copyable, portable, hard to erase, able to regrow in new soil.

## License

All content in this repository is licensed under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](LICENSE).

You are free to share and adapt this material for any purpose, including commercial, as long as you give appropriate credit and distribute derivatives under the same license.
