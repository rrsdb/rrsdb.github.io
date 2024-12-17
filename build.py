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
def build_page(path: Path):
    page = RRSDBPage.create(path, path.read_text(encoding="utf-8"))
        
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
                    try:
                        build_page(Path(entry.path))
                        print(f"Built page '{entry.path}'")
                        
                    except ValueError:
                        # Skip non-text and ambiguous build matches
                        print(f"Could not build page '{entry.path}'")
                        shutil.copyfile(entry.path, OUT_DIR.joinpath(entry.path))
                        
                elif entry.is_dir():
                    # Recurse down subdirectories
                    process_directory(entry.path)


if __name__ == "__main__":
    process_directory("pages")

    # Copy sidebar (for now)
    shutil.copyfile("components/sidebar.html", "dist/pages/sidebar.html")
