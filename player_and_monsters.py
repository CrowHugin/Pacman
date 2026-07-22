from abc import ABC, abstractmethod


class Mobs(ABC):
    def __init__(self,
                 status: str,
                 color: str,
                 coords: tuple[int, int]) -> None:
        self.status = status
        self.color = color
        self.coords = coords

    @abstractmethod
    def movements(self, coor: tuple[int, int]):
        pass


class Player(Mobs):
    def __init__(self,
                 nb_lives: int,
                 status: str,
                 color: str,
                 coords: tuple[int, int]) -> None:
        super().__init__(status, color, coords)


class Ghosts(Mobs):
    def __init__(self,
                 status: str,
                 color: str,
                 coords: tuple[int, int]) -> None:
        super().__init__(status, color, coords)
