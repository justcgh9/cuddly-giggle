from typing import Protocol


class Filter(Protocol):
    def __init__(self):
        self.process = None

    def run(self) -> None: ...
