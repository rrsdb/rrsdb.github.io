# Documentation

## Important files

* ``style.css`` contains style common to all pages (some special pages also contain custom style), including colors, margin sizes, font sizes, and so forth. Changes here effect **every article's appearance**, but not the html structure.
* ``sidebar.html`` and ``sidebar.js`` contain respectively the html structure of the sidebar and the javascript code to load the sidebar. Changes made to sidebar.html **effect every article**.
* ``rrsdb_math.js`` contains the code for power series expansion.

## Rogers-Ramanujan type identity articles
To write a Rogers-Ramanujan type identity article, start by copying the file [identities/template.html](https://rrsdb.github.io/identities/template.html).

### Rules that should be followed
* All added html should be **inside** the ``div`` tag with the id ``main``.
* All identity articles go in the directory ``identities``.
* The first time any definition is mentioned, link to the relevent article. For example, the first time the word partition is used, replace ``partition`` with ``<a href="../partitions.html">partition</a>``.
* Use links like ``<a href="article.html>`` rather than ``<a href="https://rrsdb.github.io/identities/article.html">`` since, if the domain ever changes, **all** links would need to be manually rewritten. If you need to link to a page in a different directory, you can generally use the same rules that Linux/Mac use, for instance ``<a href="../article.html">`` to access an article from the root directory of the repository.
* Indend with 2 spaces whenever you enter a new ``div``. This helps keep the file readable. For example:
```html
<div>
  <p>content</p>
  <div>
    <p>more content</p>
  </div>
</div>
```
* Avoid [deprecated html](https://www.w3schools.com/tags/), like the tag ``<center>``. There are much better ways to implement such behaviors.
* To add additional style to an element, add ``style=""`` to the tag. For example, in the html code below the word "text" will have the color blue. Only do this in special cases as needed, a style change that is present in all articles should be added to ``style.css``.
```html
<p>Example <span style="color: blue">text</span> here</p>
```
* All commits should have at least some description. If we ever need to revert to an older version, this will help track where the issue was introduced.
* Use ``<h1>`` only for the title of the page, and ``<h2>`` for all other headers.

### Useful facts about the html structure
* Large sections of article all go in a ``div`` with the class ``main_infobox``. If you give the ``div`` an id ``arbitrary_name_here``, you can link to it like ``<a href="article.html#arbitrary_name_here">`` and the contents of the ``div`` will be highlighted with a darkened background whenever the page is reached using this link. Only do this if you give such a link **elsewhere**, otherwise this serves no purpose. Also, make sure every id is unique! For example:

Your article ``article.html``:
```html
<div id="main">
  .
  .
  .
  <div class="main_infobox" id="arbitrary_name_here">
    <h2>small header</h2>
    <p>content</p>
  </div>
  .
  .
  .
</div>
```
some other article:
```html
<div id="main">
  .
  .
  .
  <div class="main_infobox">
    <h2>small header</h2>
    <p> ... for example, see <a href="article.html#arbitrary_name_here">for more</a>.</p>
  </div>
  .
  .
  .
</div>
```
