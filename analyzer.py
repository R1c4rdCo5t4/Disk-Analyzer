import os
from classes import *
from utils import *
from dataclasses import *
from datetime import *



def scan_path(path: str = ".") -> Directory:
    fs = Directory(path, 0, os.path.getctime(path), os.path.getmtime(path))
    try:
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    file = File(entry.name, entry.stat().st_size, get_created_datetime(entry),  get_modified_datetime(entry))
                    fs.files.append(file)

                elif entry.is_dir():
                    dir = Directory(entry.name, scan_path(entry.path).total_size, get_created_datetime(entry), get_modified_datetime(entry))
                    fs.directories.append(dir)
    except PermissionError:
        pass

    return fs

def sort_by_attribute(entries: list[Entry], attribute: str, reverse: bool = False) -> list[Entry]:
    return sorted(entries, key=lambda x: getattr(x, attribute), reverse=reverse)

def sort(sort_by: str, entries: list[Entry], reverse: bool = False) -> list[Entry]:
    attributes = ["name", "size", "created"]
    if sort_by not in attributes:
        raise ValueError("Invalid sort option")
    
    return sort_by_attribute(entries, sort_by, reverse)