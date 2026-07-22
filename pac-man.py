from mazegenerator import MazeGenerator

mzgn = MazeGenerator(size=(20, 20), seed=42)
for items in mzgn.maze:
    for item in items:
        print(f"{item:2d}", end=" ")
    print()
