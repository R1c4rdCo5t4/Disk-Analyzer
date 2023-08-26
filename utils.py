import os
import math
from datetime import datetime


def get_created_datetime(entry: os.DirEntry) -> datetime:
    return datetime.fromtimestamp(entry.stat().st_ctime), datetime.fromtimestamp(entry.stat().st_mtime)

def get_modified_datetime(entry: os.DirEntry) -> datetime:
    return datetime.fromtimestamp(entry.stat().st_mtime)


def convert_size(size_bytes: int) -> str:
    if size_bytes == 0: return "0B"
    units = ("B", "KB", "MB", "GB", "TB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {units[i]}"