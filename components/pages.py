import os
import re

from .renderers import *
from pathlib import Path


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
        
        # Render body
        self.renderer = self._renderer()
        self.body = mistune.create_markdown(renderer=self.renderer, plugins=PLUGINS)(page)
        self.body += closing_tags(self.body)
        
        # Layout info
        self.headings = self.renderer.headings
        self.title = self.headings[0].plaintext.replace(" ", "_")
        
    def __build__(self):
        self.sidebar = local_path("sidebar.html").read_text(encoding="utf-8")
        self.header = local_path("header.html").read_text(encoding="utf-8")
        self.footer = local_path("footer.html").read_text(encoding="utf-8")
        
        # Widgets
        self.content = local_path(self._parent).with_suffix(".html").read_text(encoding="utf-8").format(**vars(self))
        self.content = re.sub(r"!!(\w+)", lambda match: build_widget(match[1]).format(**vars(self)), self.content)
        
        # Math
        self.content = re.sub(r"\$\$(.*?)\$\$", lambda match: rf"\[{match[1]}\]", self.content)
        self.content = re.sub(r"\$([^$].*?)\$", lambda match: rf"\({match[1]}\)", self.content)
        
    def __class_getitem__(cls, item):
        return cls._page_types[item]
        
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._page_types[cls._parent] = cls
        
        
class InfoPage(RRSDBPage):
    _parent = "pages"
    _renderer = RRSDBRenderer


class IdentityPage(RRSDBPage):
    _parent = "identities"
    _renderer = IdentityRenderer
    
    def __init__(self, filename: str, page: str):
        super().__init__(filename, page)
        
        signature = re.search(r"(?P<length>\d+)\s*:\s*\((?P<items>.*?)\)", self.title)
        if signature is None:
            self.signature = "5, [1,0,0,1,0]"

        else:
            self.signature = "{length}, [{items}]".format(**signature.groupdict())
