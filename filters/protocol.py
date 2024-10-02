from typing import Protocol


class Filter(Protocol):
    def run(self) -> None: ...
