import mistune
import re

from collections import namedtuple
from mistune.directives import FencedDirective
from mistune.directives import Image, Figure

PLUGINS = [
    "strikethrough",
    "footnotes",
    "table",
    "def_list",
    "abbr",
    "mark",
    "math",
    FencedDirective([
        Image(),
        Figure()
    ])
]


# Close all open HTML tags (really awful)
def closing_tags(text: str) -> str:
    out = []
    for tag in re.findall(r"<(/?\w+)", text):
        if "/" in tag:
            try:
                out.remove(f"<{tag}>")

            except ValueError:
                pass

        else:
            out.insert(0, f"</{tag}>")

    return "\n".join(out[::-1])


# Wrap some content in tags
def wrap(text: str, tags: str) -> str:
    return f"{tags}\n{text}\n{closing_tags(tags)}"


# Strip all tags
def plaintext(text: str) -> str:
    return re.sub(r"<.*?>", "", text, flags=re.DOTALL)


Heading = namedtuple("Heading", ["level", "id", "plaintext", "rendered"])


class RRSDBRenderer(mistune.HTMLRenderer):
    # Wrap headings
    heading_tags = {}

    # Wrap the entire block, with the heading
    inclusive_block_tags = {
        "h1": '<div id="main">',
        "h2": '<div class="main_infobox">'
    }
    
    # Wrap the entire block, without the heading
    exclusive_block_tags = {}
    
    def __init__(self):
        super().__init__()

        self.headings = []
        self._heading_stack = [Heading(0, "", "", "")]
        
    def heading(self, text: str, level: int, **attrs) -> str:
        if not text:
            return "<br>"

        text, heading_id = re.search(r"(.+)\s*(?:\{#(.+)})?", text).groups()

        rendered = ""
        while level <= self._heading_stack[-1].level:
            previous = self._heading_stack.pop()
            rendered += closing_tags(previous.rendered)
        
        key = f"h{level}"
        rendered += self.inclusive_block_tags.get(key, "")
        rendered += wrap(super().heading(text, level, id=heading_id, **attrs), self.heading_tags.get(key, ""))
        rendered += self.exclusive_block_tags.get(key, "")
        
        heading = Heading(level, heading_id, plaintext(text), rendered)
        self.headings.append(heading)
        self._heading_stack.append(heading)
        
        return rendered
    
    def emphasis(self, text: str) -> str:
        return f"<i>{text}</i>"

    def strong(self, text: str) -> str:
        return f"<b>{text}</b>"

    def block_math(self, text: str) -> str:
        return rf"\[{text}\]"

    def inline_math(self, text: str) -> str:
        return rf"\({text}\)"

    def list_item(self, text: str) -> str:
        return f"<li><p>{super().list_item(text)[4:-6]}</p></li>\n"


class IdentityRenderer(RRSDBRenderer):
    inclusive_block_tags = {
        "h1": '<div id="main">'
              '<div class="main_infobox">',
        "h2": '<div class="identity_container">'
    }
