import os
from json import JSONEncoder

class OutputRecord:

    def __init__(self, n:str, dup: list) -> None:
        self.name = os.path.basename(n)
        self.folder = os.path.dirname(n)
        self.duplicates = list()
        for i in dup:
            self.duplicates.append(vars(OutputRecordDuplicate(i)))

class OutputRecordDuplicate(JSONEncoder):

    def __init__(self, n:str) -> None:
        self.name = os.path.basename(n)
        self.folder = os.path.dirname(n)
