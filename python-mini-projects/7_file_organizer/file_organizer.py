#!/usr/bin/env python3
"""File Organizer - Auto Organize Current Folder"""

import shutil
from pathlib import Path

class Organizer:
    TYPES = {
        "Images"    : [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
        "Videos"    : [".mp4", ".mkv", ".avi", ".mov"],
        "Audio"     : [".mp3", ".wav", ".flac", ".aac"],
        "Documents" : [".pdf", ".doc", ".docx", ".pptx", ".txt"],
        "Code"      : [".py", ".java", ".c", ".cpp", ".html", ".js", ".css"],
        "Archives"  : [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Others"    : []
    }

    def __init__(self):
        self.folder = Path.cwd()   # ⭐ current folder

    def get_type(self, ext):
        ext = ext.lower()
        for t, exts in self.TYPES.items():
            if ext in exts:
                return t
        return "Others"

    def organize(self):
        # Make folders
        for t in self.TYPES:
            (self.folder / t).mkdir(exist_ok=True)

        # Move files
        for f in self.folder.iterdir():
            if (
                f.is_file()
                and f.name != Path(__file__).name       # don't move script
                and f.name.lower() not in ["readme.md", "readme.txt"]   # don't move README
            ):
                t = self.get_type(f.suffix)
                target = self.folder / t / f.name
                shutil.move(str(f), str(target))
                print(f"Moved: {f.name} → {t}/")

def main():
    print("\nFILE ORGANIZER\n")
    Organizer().organize()
    print("\n✔ Done!\n")

if __name__ == "__main__":
    main()
