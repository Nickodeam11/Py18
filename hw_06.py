import sys
from pathlib import Path


CATEGORIES = {"Audio": [".mp3", ".wav", ".flac", ".wma"],
              "Docs": [".docx", ".txt", ".pdf"]}


def get_categories(file:Path) -> str:
    ext = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if ext in exts:
            return cat
    return "Other"


def move_file(file:Path, category:str, root_dir:Path) -> None:
    target_dir = root_dir.joinpath(category)
    if not target_dir.exists():
        target_dir.mkdir()
    new_path = target_dir.joinpath(file.name)
    if not new_path.exists():
        file.replace(new_path)


def sort_folder(path:Path) -> None:

    for element in path.glob("**/*"):
        if element.is_file():
            category = get_categories(element)
            move_file(element, category, path)


def main() -> str:
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "No path to folder"
    
    if not path.exists():
        return "Folder dos not exists"
    
    sort_folder(path)
    
    return "All Ok"


if __name__ == '__main__':
    main()
