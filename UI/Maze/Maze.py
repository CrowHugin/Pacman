from mazegenerator import MazeGenerator


class Cell:
    def __init__(self, x: int, y: int, content: int):
        self.x = x
        self.y = y
        self.content = content
        self.is_42: bool = False


class Maze:
    def __init__(self, width: int, height: int, seed: int):
        self.width = width
        self.height = height
        generator = MazeGenerator(size=(width, height), seed=seed)
        self.maze = generator.maze
        self.cases: dict[tuple[int, int], Cell] = {}

        for idx_row, row in enumerate(self.maze):
            for idx_col, item in enumerate(row):
                if item == 0:
                    self.cases[(idx_col, idx_row)] = Cell(idx_col,
                                                          idx_row,
                                                          item)
                else:
                    self.cases[(idx_col, idx_row)] = Cell(idx_col,
                                                          idx_row,
                                                          item)
