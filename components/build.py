import mistune
import os
import shutil
import re

from pathlib import Path


def id_from_title(title: str) -> str:
    return title.lower().replace(" ", "_")



class Root(mistune.HTMLRenderer):
    heading_classes = {
        1: ["main"],
        2: ["main_infobox"]
    }

    def __init__(self):
        super().__init__()

        self._heading_stack = []

    def heading(self, text: str, level: int, **attrs) -> str:
        current = self._heading_stack[-1]
        if level <= current:
            out = "</div>\n" * (current - level)
            self._heading_stack.pop()

        else:
            out = ""
            self._heading_stack.append(level)

        out += f"<div id={id_from_title(text)}"

        if level in self.heading_classes:
            out += f"class={self.heading_classes.get(level)} "

        return f"{out}>\n{super().header(text, level, **attrs)}"

    def block_math(self, text) -> str:
        return f"\\[ {text} \\]"

    def inline_math(self, text) -> str:
        return f"\\( {text} \\)"



# Create output directory
OUT_DIR = Path("dist")
os.mkdir(OUT_DIR)


# Get HTML template
with open("template.html") as infile:
    template = infile.read()
    
    



# Get a widget from a local file
def get_widget(path):
    try:
        return Path(path).with_suffix(".html").read_text(encoding="utf-8")
        
    except FileNotFoundError:
        return f"Could not load widget: {path}"


# Build a single page
def build_page(path):
    with open(path, encoding="utf-8") as infile:
        lines = infile.readlines()

        # Get signature
        title = next(line for line in lines if line.strip()).strip("# ")
        title = re.sub(r"\[(.*?)\]\(.*?\)", lambda match: match[1], title)
        
        signature = re.search(r"(?P<length>\d+)\s*:\s*\((?P<items>.*?)\)", title)
        
        if signature is None:
            print(title)
            signature = "5, [1,0,0,1,0]"
            
        else:
            signature = "{length}, [{items}]".format(**signature.groupdict())
            
            
        # Prepare page
        page = "\n".join(lines)
        
        # LaTeX syntax
        page = re.sub(r"\$\$(.*?)\$\$", lambda match: f"\\[{match[1]}\\]", page)
        page = re.sub(r"\$(.*?)\$", lambda match: f"\\({match[1]}\\)", page)
        page = page.replace("\\", "\\\\")
        
        # Build page
        md.reset()
        params = {"filename": Path(path).with_suffix("").name,
                  "title": title,
                  "signature": signature,
                  "page": md.convert(page)}
        
        with open(OUT_DIR.joinpath(path).with_suffix(".html"), "w+", encoding="utf-8", errors="xmlcharrefreplace") as outfile:
            content = template.format(**params)
            
            # Process widgets
            content = re.sub(r"!!(\w+)", lambda match: get_widget(match[1].lower()).format(**params), content)
            
            outfile.write(content)
    


# Build all pages in a directory
def process_directory(path=None):
    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith(".") and entry.name != OUT_DIR.name:
                if entry.is_file():
                    if entry.name.endswith(".md"):
                        # Markdown: render the page
                        build_page(entry.path)
                        
                    else:
                        # Anything else: just copy it over
                        shutil.copyfile(entry.path, OUT_DIR.joinpath(entry.path))
                        
                elif entry.is_dir():
                    # Recurse down subdirectories
                    os.mkdir(OUT_DIR.joinpath(entry.path))
                    process_directory(entry.path)


process_directory()
