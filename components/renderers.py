import mistune
import regex

from collections import namedtuple
from mistune.directives import FencedDirective
from mistune.directives import Image, Figure


# Close all open HTML tags (really awful)
def closing_tags(text: str) -> str:
    out = []
    for tag in regex.findall(r"<(/?\w+)", text):
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
    return regex.sub(r"<.*?>", "", text, flags=regex.DOTALL)


# Math plugin
def math(md):
    block_pattern = r'^\s*\$\$\s*(?P<math_text>[\s\S]+?)\s*\$\$\s*$'
    inline_pattern = r'\$\s*(?P<math_text>.+?)\s*\$'

    def parse_block_math(block, match, state) -> int:
        text = match['math_text']
        state.append_token({"type": "block_math", "raw": text})
        return match.end() + 1

    def parse_inline_math(inline, match, state) -> int:
        text = match['math_text']
        state.append_token({"type": "inline_math", "raw": text})
        return match.end()


    md.block.register('block_math', block_pattern, parse_block_math, before='list')
    md.block.insert_rule(md.block.list_rules, 'block_math', before='list')
    md.inline.register('inline_math', inline_pattern, parse_inline_math, before='link')

    if md.renderer and md.renderer.NAME == 'html':
        md.renderer.register('block_math', lambda renderer, text: rf"\[{text}\]")
        md.renderer.register('inline_math', lambda renderer, text: rf"\({text}\)")


PLUGINS = [
    "strikethrough",
    "footnotes",
    "table",
    "def_list",
    "abbr",
    "mark",

    math,

    FencedDirective([
        Image(),
        Figure()
    ])
]


Heading = namedtuple("Heading", ["level", "id", "plaintext", "rendered"])


class RRSDBRenderer(mistune.HTMLRenderer):
    # Wrap headings
    heading_tags = {
        "h2": '<div class="main_infobox_header">',
        "h3": '<div class="main_infobox_header">'
    }

    # Wrap the entire block, with the heading
    inclusive_block_tags = {
        "h1": '<div id="main">',
        "h2": '<div class="main_infobox" id="">',
        "h3": '<div class="main_infobox" id="">'
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

        if "{#" in text:
            text, heading_id = text.rstrip().split("{#")
            heading_id = f'id="{heading_id.rstrip("}")}"'

        else:
            heading_id = ""

        def should_close_heading():
            adjacent_infoboxes = all("main_infobox" in self.heading_tags.get(f"h{l}", "")
                                     for l in [level, self._heading_stack[-1].level])

            return adjacent_infoboxes or level <= self._heading_stack[-1].level

        rendered = ""
        while should_close_heading():
            previous = self._heading_stack.pop()
            rendered += closing_tags(previous.rendered)

        key = f"h{level}"
        rendered += self.inclusive_block_tags.get(key, "").replace('id=""', heading_id)
        rendered += wrap(super().heading(text, level, **attrs), self.heading_tags.get(key, ""))
        rendered += self.exclusive_block_tags.get(key, "")

        heading = Heading(level, heading_id, plaintext(text), rendered)
        self.headings.append(heading)
        self._heading_stack.append(heading)

        return rendered

    def emphasis(self, text: str) -> str:
        return f"<i>{text}</i>"

    def strong(self, text: str) -> str:
        return f"<b>{text}</b>"

    def list_item(self, text: str) -> str:
        return f"<li><p>{super().list_item(text)[4:-6]}</p></li>\n"


class IdentityRenderer(RRSDBRenderer):
    heading_tags = {}

    inclusive_block_tags = {
        "h1": '<div id="main">'
              '<div class="main_infobox" id="">',
        "h2": '<div class="identity_container">'
    }
