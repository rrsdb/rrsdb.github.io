import os
import regex

from .renderers import *
from pathlib import Path
from urllib.parse import quote


# Get file relative to CWD
def local_path(path: str) -> Path:
    return Path(os.path.dirname(__file__)).joinpath(path)


# Get widget content; will eventually use build scripts
def build_widget(path: str) -> str:
    return local_path("widgets").joinpath(path, "template.html").read_text()
    

# Metaclass for building after __init__
class Built(type):
    def __call__(cls, *args, **kwargs):
      new = type.__call__(cls, *args, **kwargs)
      new.__build__()
      return new
        
        
class RRSDBPage(metaclass=Built):
    _page_types = {}
    
    _parent = None
    _renderer = None
    
    def __init__(self, filename: str, page: str):
        self.filename = filename
        
        # Math spacing
        page = regex.sub(r"\$\$\s*(.*?)\s*\$\$", lambda match: f"$$\n{match[1]}\n$$", page)
        page = regex.sub(r"\$\s*(.*?)\s*\$", lambda match: f"${match[1]}$", page)

        # URL Escaping
        page = regex.sub(r"]\((\S+)\)", lambda match: f"]({quote(match[1], safe=':/#')})", page)

        # Render body
        self.renderer = self._renderer()
        self.body = mistune.create_markdown(renderer=self.renderer, plugins=PLUGINS)(page)
        self.body += closing_tags(self.body)
        
        # Layout info
        self.headings = self.renderer.headings
        self.title = self.headings[0].plaintext if self.headings else ""

        # References
        self.bailey_links = regex.findall(r"[A-Z]\(\d{,2}\)", page)

        auth = r"[\p{Lu}\p{Lt}]\w+"
        details = r"\((\d{4})(?:, ((?:\(.*?\)|.)*?))?\)"
        self.references = regex.findall(rf"({auth}|(?:{auth}, )*{auth},? (?:and|&) {auth}|) {details}", page)
        
    def __build__(self):
        self.sidebar = self.replace_vars(local_path("sidebar.html").read_text(encoding="utf-8"))
        self.header = self.replace_vars(local_path("header.html").read_text(encoding="utf-8"))
        self.footer = self.replace_vars(local_path("footer.html").read_text(encoding="utf-8"))

        self.content = self.replace_vars(local_path(self._parent).with_suffix(".html").read_text(encoding="utf-8"))

        # Widgets
        self.content = regex.sub(r"!!(\w+)(!!)?", lambda match: self.replace_vars(build_widget(match[1])), self.content)
        
    def __class_getitem__(cls, item):
        return cls._page_types[item]
        
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._page_types[cls._parent] = cls

    # Replace vars in a file (!! shouldn't conflict with other syntax)
    def replace_vars(self, content: str) -> str:
        return regex.sub(r"!!(\w+)(!!)?", lambda match: vars(self)[match[1]], content)
        
        
class InfoPage(RRSDBPage):
    _parent = "pages"
    _renderer = RRSDBRenderer

    def __init__(self, filename: str, page: str):
        super().__init__(filename, page)

        # Maybe don't hardcode this in the future?
        self.section = "Tools" if filename == "series_factorization_tool.html" else "Definitions and Preliminaries"


class IdentityPage(RRSDBPage):
    _parent = "identities"
    _renderer = IdentityRenderer
    
    def __init__(self, filename: str, page: str):
        super().__init__(filename, page)
        
        signature = regex.search(r"(?P<length>\d+)\s*:\s*\((?P<items>.*?)\)", self.title)
        if signature is None:
            self.signature = "5, [1,0,0,1,0]"

        else:
            self.signature = "{length}, [{items}]".format(**signature.groupdict())

        self.section = "Rogers—Ramanujan type identities"
