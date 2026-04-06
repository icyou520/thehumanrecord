# Contributing to The Human Record

Thank you for helping build a durable library of human meaning.

## What We Accept

### Values (`content/values/`)
Universal human values that appear across cultures and centuries. Not trending opinions. Not political positions. Values that a person from any civilization would recognize.

**Good examples:** compassion, courage, honesty, gratitude, stewardship
**Bad examples:** "capitalism is good," "my religion is correct," "technology will save us"

### Tensions (`content/tensions/`)
Genuine, perpetual conflicts between legitimate values. Both sides must be stated honestly and charitably.

**Good examples:** freedom vs. order, mercy vs. justice, individual vs. community
**Bad examples:** "good vs. evil" (not a real tension — it's a conclusion)

### Parables (`content/parables/`)
Short stories that compress a moral insight. Can be ancient, cross-cultural, or original — but must be timeless, not topical.

### Proverbs (`content/proverbs/`)
Cross-cultural proverbs with attribution to tradition of origin. Translations welcome.

## How to Contribute

1. **Fork** the repository
2. **Create** a new Markdown file in the appropriate `content/` directory
3. **Follow the schema** — use the frontmatter template from the archetypes or existing records
4. **Write clearly** — short, dense, honest. No filler. No jargon.
5. **Cite sources** — link to the philosophical, religious, psychological, or literary tradition
6. **Submit a pull request** with a clear description of what you are adding and why

## Frontmatter Requirements

Every record must include:

- `id`: unique slug (lowercase, hyphens)
- `title`: human-readable name
- `type`: one of `value`, `tension`, `parable`, `proverb`
- `summary`: one-sentence compression of the idea
- `traditions`: which cultural/philosophical traditions recognize this
- `related`: links to other records by ID
- `tags`: descriptive tags
- `sources`: at least one citation
- `created` / `updated`: ISO 8601 dates
- `version`: integer, incremented on substantive edits
- `license`: `CC-BY-SA-4.0`

## Quality Standards

- **Timeless over timely.** Will this matter in 100 years?
- **Dense over verbose.** Say it in fewer words.
- **Honest over comfortable.** State tensions fairly. Don't flatten nuance.
- **Multi-tradition.** Show how many cultures converge on similar insights.
- **Citeable.** Back claims with references.

## What We Reject

- Propaganda for any political party, religion, or ideology
- Content designed to promote a product or service
- Entries that present one side of a genuine tension as the only truth
- Inflammatory, hateful, or deliberately divisive content
- AI-generated filler with no editorial review

## Translations

Translations are deeply valued. To contribute a translation:

1. Add the language code and translated title to the `languages` field in frontmatter
2. If translating the full body, create a parallel file with the language suffix (e.g., `compassion.es.md`)
3. Note the translator in the file metadata

## Editorial Process

All contributions are reviewed by maintainers for:

1. **Accuracy** — Is this a real value/tension/parable recognized across traditions?
2. **Honesty** — Are opposing views stated fairly?
3. **Quality** — Is the writing clear, dense, and durable?
4. **Schema compliance** — Does the frontmatter follow the required format?

Expect thoughtful feedback. This is a library, not a content farm.
