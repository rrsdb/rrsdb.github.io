import os
import regex

from .renderers import *
from fnmatch import fnmatch
from pathlib import Path
from urllib.parse import quote


# Get file relative to CWD
def local_path(path: str) -> Path:
    return Path(os.path.dirname(__file__)).joinpath(path)


# Get widget content; will eventually use build scripts
def build_widget(path: str) -> str:
    return local_path("widgets").joinpath(path, "template.html").read_text()

VAR_PATTERN = r"!!(?P<var>\w+)(!!)?"


# Metaclass for building after __init__
class Built(type):
    def __call__(cls, *args, **kwargs):
        new = type.__call__(cls, *args, **kwargs)
        new.__build__()
        return new


class RRSDBPage(metaclass=Built):
    _page_types = {}
    _path = "*"

    _template = "page"
    _renderer = None

    def __init__(self, path: Path, page: str):
        # Just copy non-Markdown
        self.path = path
        self.filename = path.stem
        self.content = page
        self.section = "The Rogers–Ramanujan–Slater Data Base"

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        RRSDBPage._page_types[cls._path] = cls
        RRSDBPage._page_types[RRSDBPage._path] = RRSDBPage

    def __build__(self):
        pass

    @classmethod
    def create(cls, path: Path, page: str):
        # Match class glob, respecting directory level
        matches = [value for key, value in cls._page_types.items()
                   if fnmatch(str(path), key) and (key.count("/") == 0 or len(path.parts) == len(key.split("/")))]

        # Find the match with no children
        leaves = [value for value in matches if
                  not any(issubclass(child, value) for child in matches if value != child)]

        if len(leaves) != 1:
            raise ValueError(f"missing or multiple matches for path '{path}': {leaves}")

        return leaves[0](path, page)

    # Replace vars in a file (!! shouldn't conflict with other syntax)
    def replace_vars(self, content: str) -> str:
        return regex.sub(VAR_PATTERN, lambda match: vars(self)[match['var']], content)


class MarkdownPage(RRSDBPage):
    _path = "*.md"

    _renderer = RRSDBRenderer

    def __init__(self, path: Path, page: str):
        super().__init__(path, page)

        # URL Escaping
        page = regex.sub(r"]\((?P<url>\S+)\)", lambda match: f"]({quote(match['url'], safe=':/#')})", page)

        # Render body
        self.renderer = self._renderer()
        self.body = mistune.create_markdown(renderer=self.renderer, plugins=PLUGINS)(page)
        self.body += closing_tags(self.body)

        # Layout info
        self.headings = self.renderer.headings
        self.title = self.headings[0].plaintext if self.headings else ""

        # References
        auth = r"[\p{Lu}\p{Lt}]\w+"
        pattern = rf"(?P<authors>({auth}|(?:{auth}, )*{auth},? (?:and|&) {auth}|)) \((?P<year>\d{{4}})(?:, (?P<details>(?:\(.*?\)|.)*?))?\)"
        self.references = [*regex.finditer(pattern, page)]
        self.references = [(regex.split(r" and |, and | & |, ", match['authors']), match['year'], match['details'])
                           for match in self.references]

    def __build__(self):
        self.sidebar = self.replace_vars(local_path("sidebar.html").read_text(encoding="utf-8"))
        self.header = self.replace_vars(local_path("header.html").read_text(encoding="utf-8"))
        self.footer = self.replace_vars(local_path("footer.html").read_text(encoding="utf-8"))

        self.content = self.replace_vars(local_path(self._template).with_suffix(".html").read_text(encoding="utf-8"))

        # Widgets
        self.content = regex.sub(VAR_PATTERN, lambda match: self.replace_vars(build_widget(match['var'])), self.content)


class InfoPage(MarkdownPage):
    _path = "pages/*.md"

    def __init__(self, path: Path, page: str):
        super().__init__(path, page)

        self.section = "Definitions and Preliminaries"


class IdentitiesPage(RRSDBPage):
    _path = "pages/identities_by_product.html"

    def __init__(self, path: Path, page: str):
        super().__init__(path, page)

        self.section = "Rogers–Ramanujan type identities"

    def __build__(self):
        # Make missing pages red
        identities = [entry.name for entry in os.scandir("pages/identities")]

        for row in regex.findall(r"<tr>(.*?)</tr>", self.content, flags=regex.DOTALL):
            if "<th>" in row:
                continue

            cols = regex.findall(r"<td>(.*?)</td>", row, flags=regex.DOTALL)
            identity = regex.search(r"identities/([0-9.]+)\.html", cols[0])

            if identity is None:
                continue

            identity = identity[1]
            if f"{identity}.md" not in identities:
                # Color equation red
                self.content = regex.sub(rf'(?<=<a href="identities/{identity}\.html">)(.*?)\\\((.*?)\\\)',
                                         lambda match: f"{match[1]}\\({{\\color{{red}} {match[2]} }}\\)",
                                         self.content, flags=regex.DOTALL)

                # Color entire row red
                self.content = regex.sub(rf'<tr>(?=\s*<td>\s*<a href="identities/{identity}\.html">)',
                                         '<tr style="color:red">',
                                         self.content)


class ToolsPage(RRSDBPage):
    _path = "pages/series_factorization_tool.html"

    def __init__(self, path: Path, page: str):
        super().__init__(path, page)

        self.section = "Tools"


class IdentityPage(MarkdownPage):
    _path = "pages/identities/*.md"

    _template = "identity"
    _renderer = IdentityRenderer

    def __init__(self, path: Path, page: str):
        super().__init__(path, page)

        self.section = "Rogers–Ramanujan type identities"

        # Determine sequence signature
        signature = regex.search(r"(?P<length>\d+)\s*:\s*\((?P<items>.*?)\)", self.title)
        if signature is None:
            self.signature = "5, [1,0,0,1,0]"

        else:
            self.signature = f"{signature['length']}, [{signature['items']}]"


    def __build__(self):
        super().__build__()

        # Bailey links
        self.content = regex.sub(r"(?<!\$\s*)[A-Z]\(\d{,3}\)(?!\s*\$)",
                                 lambda match: f'<a href="../Bailey_pair_tables.html#{match[0]}">{match[0]}</a>',
                                 self.content)
