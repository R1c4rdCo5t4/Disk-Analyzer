from abc import ABC, abstractmethod
from datetime import datetime
from functools import reduce

class Entry(ABC):
    def __init__(self, name: str, size: int, created: datetime, modified: datetime):
        self.name = name
        self.size = size
        self.created = created
        self.modified = modified

    pass

class File(Entry):
    pass


class Directory(Entry):
    def __init__(self, name: str, size: int, created: datetime, modified: datetime):
        super().__init__(name, size, created, modified)
        self.files = []
        self.directories = []

    @property
    def total_size(self) -> int:
        return (
            reduce(lambda acc, file: acc + file.size, self.files, 0) +
            reduce(lambda acc, dir: acc + dir.total_size, self.directories, 0)
        )

    def items(self) -> list[Entry]:
        return self.files + self.directories
