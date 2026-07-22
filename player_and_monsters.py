from abc import ABC, abstractmethod


__all__ = ["abstractmethod"]


class Mobs(ABC):
    def __init__(self, status: str) -> None:
        self.status = status


class Player(Mobs):
    def __init__(self, status: str) -> None:
        super().__init__(status)


class Ghosts(Mobs):
    def __init__(self, status: str) -> None:
        super().__init__(status)
