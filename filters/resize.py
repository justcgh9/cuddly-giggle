from multiprocessing import Process
from typing import Self

import cv2

from filters.protocol import Filter
from pipe import Pipe


class ResizeFilter(Filter):
    def __init__(
        self,
        inputs: list[Pipe],
        outputs: list[Pipe],
        width: int = 600,
        height: int = 600,
    ) -> None:
        self.width = width
        self.height = height
        self.inputs = inputs
        self.outputs = outputs

    def run(self) -> None:
        process = Process(target=self._process)
        process.start()

    def _process(self) -> None:
        while True:
            for input_ in self.inputs:
                frame = input_.recv()
                processed_frame = cv2.resize(frame, (self.width, self.height))
                for output in self.outputs:
                    output.send(processed_frame)
