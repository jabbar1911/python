#!/usr/bin/env python3
"""File Organizer"""

import os
import shutil
from pathlib import Path

class FileOrganizer:
    FILE_CATEGORIES = {
        'Images': ['.jpg', '.png', '.gif'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Audio': ['.mp3', '.wav', '.flac'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt'],
        'Archives': ['.zip', '.rar', '.7z'],
        'Others': []
    }

    def __init__(self, directory=None):
        self.directory = Path(directory) if directory else Path.cwd()

    def get_category(self, ext):
        ext = ext.lower()
        for cat, exts in self.FILE_CATEGORIES.items():
            if ext in exts:
                return cat
        return 'Others'

    def organize(self):
        for cat in self.FILE_CATEGORIES:
            (self.directory / cat).mkdir(exist_ok=True)

        for file in self.directory.iterdir():
            if file.is_file():
                cat = self.get_category(file.suffix)
                target = self.directory / cat / file.name
                shutil.move(str(file), str(target))
                print(f"Moved: {file.name} → {cat}/")

def main():
    print("FILE ORGANIZER")
    print("\nOrganize current directory? (y/n): ", end='')

    if input().lower() == 'y':
        org = FileOrganizer()
        org.organize()
        print("Done!")

if __name__ == "__main__":
    main()
