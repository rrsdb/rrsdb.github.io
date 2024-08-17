import mistune
import re

from collections import namedtuple


PLUGINS = [
    "strikethrough",
    "footnotes",
    "table",
    "def_list",
    "abbr",
    "mark"
]


# Close all open HTML tags
def closing_tags(text: str) -> str:
    return "\n".join(f"</{tag}>" for tag in re.findall(r"<(\w+)(?!.*</\1>)", text))


# Wrap some content in tags
def wrap(text: str, tags: str) -> str:
    return f"{tags}\n{text}\n{closing_tags(tags)}"


class TextRenderer(mistune.HTMLRenderer):
    # Really hacky tbh
    def __getattribute__(self, item):
        try:
            if item in object.__getattribute__(self, "__methods") and getattr(type(self), item) == getattr(mistune.HTMLRenderer, item):
                return lambda text, *args, **kwargs: text
            
        except AttributeError:
            pass
        
        return object.__getattribute__(self, item)
    

plaintext = mistune.create_markdown(renderer=TextRenderer(), plugins=PLUGINS)
    
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


class IdentityRenderer(RRSDBRenderer):
    inclusive_block_tags = {
        "h1": '<div id="main">'
              '<div class="main_infobox">',
        "h2": '<div class="identity_container">'
    }
