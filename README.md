# Documentation

## Important files

* **style.css** contains style common to all pages (some special pages also contain custom style), including colors, margin sizes, font sizes, and so forth. Changes here effect **every article's appearance**, but not the html structure.
* **sidebar.html** and **sidebar.js** contain respectively the html structure of the sidebar and the javascript code to load the sidebar. Changes made to sidebar.html **effect every article**.

## Rogers-Ramanujan type identity articles
To write a Rogers-Ramanujan type identity article, start by copying the file [identities/template.html](https://rrsdb.github.io/identities/template.html). Change nothing from the part you copy (unless you know what you are doing), and add additional html as needed.

### Rules that should be followed
* All added html should be **inside** the ``div`` tag with the id ``main``.
* All identity articles go in the directory ``identities``.
* Use links like ``<a href="article.html>`` rather than ``<a href="https://rrsdb.github.io/identities/article.html">`` since, if the domain ever changes, **all** links would need to be manually rewritten. If you need to link to a page in a different directory, you can generally use the same rules that Linux/Mac use, for instance ``<a href="../article.html">`` to access an article from the root directory of the repository.
