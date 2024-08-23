# Documentation

## Important files

* ``style.css`` contains style common to all pages (some special pages also contain custom style), including colors, margin sizes, font sizes, and so forth. Changes here effect **every article's appearance**, but not the html structure.
* ``sidebar.html`` and ``sidebar.js`` contain respectively the html structure of the sidebar and the javascript code to load the sidebar. Changes made to sidebar.html **effect every article**.
* ``rrsdb_math.js`` contains the code for power series expansion.

## Rogers-Ramanujan type identity articles
To write a Rogers-Ramanujan type identity article, start by copying the file [identities/template.md](https://rrsdb.github.io/identities/template.md).

### Markdown Cheatsheet

The identities template demonstrates how each of the important Markdown elements are used. A cheatsheet is also provided below and in the [Markdown Guide](https://www.markdownguide.org/cheat-sheet/).

#### Inline elements

| Element    | Markdown Syntax  |
|------------|------------------|
| Title      | `# Title`        |
| Heading    | `## Heading`     |
| Subheading | `### Subheading` |
| Bold       | `**bold**`       |
| Italics    | `_italics_`      |
| Highlight  | `==highlight==`  |
| Math       | `$LaTeX$`        |
| Quote      | `> Quote`        |
| Link       | `[text](url)`    |
| Image      | `![text](url)`   |
| Line Break | `<br>`           |

When linking to other pages, use relative links (`../partitions.html`) rather than absolute links (`rrsdb.github.io/partitions.html`). Any `.md` file you can view on GitHub has a corresponding `.html` page.

#### Block Elements

```md
# Ordered List
1. First
2. Second
3. Third

# Unordered List
- First
- Second
- Third

# Block Math
$$ LaTeX $$

# Definition
term
: definition

# Footnote
Sentence. [^1]
[^1]: Footnote

# Table
| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
| Data 3   | Data 4   |

# Raw HTML
<p>HTML</p>
```

#### Widgets

Widgets are elements generated using page and identity information after the rest of the page is written to HTML. Widgets are inserted via `!!name`; do not change the location of widgets already provided in the template.

- `!!graphs`: Graph(s) of the function
- `!!power_series`: Calculator for power series coefficients
