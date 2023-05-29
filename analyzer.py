import os
import math
from dataclasses import dataclass, field


@dataclass
class FileSystem:
    directories: dict[str, int] = field(default_factory=dict)
    files: dict[str, int] = field(default_factory=dict)

    @property
    def total_size(self) -> int:
        return sum(self.directories.values()) + sum(self.files.values())


def get_dir_size(path: str = ".") -> FileSystem:
    fs = FileSystem()
    try:
        with os.scandir(path) as it:
            for entry in it:
                if entry.is_file():
                    fs.files[entry.name] = entry.stat().st_size

                elif entry.is_dir():
                    fs.directories[entry.name] = get_dir_size(entry.path).total_size
    except PermissionError:
        pass

    return fs


def convert_size(size_bytes: int) -> str:
    if size_bytes == 0: return "0B"
    units = ("B", "KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {units[i]}"

def sort_dict(d: dict, reverse: bool):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=not reverse))