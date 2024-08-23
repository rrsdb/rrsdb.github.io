import os
import shutil

from components import *
from pathlib import Path


# Create output directory
OUT_DIR = Path("dist")
try:
    os.mkdir(OUT_DIR)
    
except FileExistsError:
    pass


# Build a single page
def build_page(path):
    page = RRSDBPage[path.parent.stem](path.stem, path.read_text(encoding="utf-8"))
        
    with open(OUT_DIR.joinpath(path).with_suffix(".html"), "w+", encoding="utf-8", errors="xmlcharrefreplace") as outfile:
        outfile.write(page.content)


# Build all pages in a directory
def process_directory(path):
    try:
        os.mkdir(OUT_DIR.joinpath(path))
        
    except FileExistsError:
        pass
    
    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith(".") and entry.name != OUT_DIR.name:
                if entry.is_file():
                    if entry.name.endswith(".md"):
                        # Markdown: render the page
                        build_page(Path(entry.path))
                        
                    else:
                        # Anything else: just copy it over
                        shutil.copyfile(entry.path, OUT_DIR.joinpath(entry.path))
                        
                elif entry.is_dir():
                    # Recurse down subdirectories
                    process_directory(entry.path)


if __name__ == "__main__":
    process_directory("pages")
