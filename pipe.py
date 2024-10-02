from multiprocessing import Queue

from cv2.typing import MatLike


class Pipe:
    def __init__(self) -> None:
        self.queue: Queue = Queue()

    def send(self, data: MatLike) -> None:
        self.queue.put(data)

    def recv(self) -> MatLike:
        return self.queue.get()
