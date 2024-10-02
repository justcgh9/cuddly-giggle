import multiprocessing

import cv2

from filters.protocol import Filter
from pipe import Pipe


class GrayScaleFilter(Filter):
    def __init__(self, inputs: list[Pipe], outputs: list[Pipe]):
        self.inputs, self.outputs = inputs, outputs

    def run(self):
        self.process = multiprocessing.Process(target=self._process)
        self.process.start()

    def _process(self):
        while True:
            for input_pipe in self.inputs:
                frame = input_pipe.recv()
                processed_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                for output_pipe in self.outputs:
                    output_pipe.send(processed_frame)
