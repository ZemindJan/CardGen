from data.fetch import fetch
from data.process import process
from abc import abstractmethod
from typing import Callable

Entry = dict[str, str]

class Source:
    def __init__(self) -> None:
        self.preprocessors : list[Callable[[Entry], Entry]] = []

    @abstractmethod
    def get_data(self) -> list[dict[str, str]]:
        pass

    def preprocess(self, entry : Entry) -> Entry:
        for processor in self.preprocessors:
            entry = processor(entry)
        
        return entry

class OnlineSource(Source):
    def __init__(self, url : str) -> None:
        super().__init__()
        self.url = url

    def get_data(self) -> list[dict[str, str]]:
        fetched_file = fetch(self.url)
        return process(fetched_file)

class LocalSource(Source):
    def __init__(self, path : str) -> None:
        super().__init__()
        self.path = path

    def get_data(self) -> list[dict[str, str]]:
        return process(self.path)
    
class ManualSource(Source):
    def __init__(self, entries : list[dict[str, str]]) -> None:
        super().__init__()
        self.entries = entries
    
    def get_data(self) -> list[dict[str, str]]:
        return self.entries