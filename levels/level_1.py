import sys
#import pygame
from mazegenerator import MazeGenerator


class Cell:
    def __init__(self, x: int, y: int, content: str):
        self.x = x
        self.y = y
        self.content = content

class Maze:
    def __init__(self, width: int, height: int, seed: int):
        generator = MazeGenerator(size=(width, height), seed=seed)
        self.maze = generator.maze
        self.cases: dict[tuple[int, int], Cell]= {}

        for idx_row, row in enumerate(self.maze):
            for idx_col, item in enumerate(row):
                self.cases[(idx_col, idx_row)] = Cell(idx_col, idx_row, item)

def create_maze() -> list[list[str]]:
    mzgn = MazeGenerator(size=(20, 20), seed=42)
    maze: list[list[str]] = mzgn.maze
    return (maze)


#def create_window(MAZE: list[list[str]]) -> None:
#    CELL_SIZE = 40
#    COLS = len(MAZE[0])
#    ROWS = len(MAZE)
#    SCREEN_WIDTH = COLS * CELL_SIZE
#    SCREEN_HEIGHT = ROWS * CELL_SIZE
#    pygame.init()
#    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#    pygame.display.set_caption("PAC-MAN")
#    running: bool = True
#    while running:
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                running = False
#        pygame.display.flip()    # Effacer l'écran en noir
#        window.fill((0, 0, 0))
#
#        for row_idx in range(ROWS):
#            for col_idx in range(COLS):
#                x = col_idx * CELL_SIZE
#                y = row_idx * CELL_SIZE
#                pygame.draw.rect(window, (240, 240, 240),
#                                 (x, y, CELL_SIZE, CELL_SIZE))
#        pygame.display.flip()
#    pygame.quit()
#    sys.exit()

if __name__ == '__main__':
    maze = Maze(20, 20, 42)
    print(maze.cases[(0,0)].content)
    print(maze.cases[(19,19)].content)
