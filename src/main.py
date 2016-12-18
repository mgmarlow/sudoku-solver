import csv
import sys
import time

from backtrack import backtrack
from ui import sudokui
from tkinter import Tk


def main():
    if len(sys.argv) != 2:
        print("Usage: main.py <file.csv>")
        exit(1)

    start_time = time.time()
    grid = parse_puzzle(sys.argv[1])

    # Draw UI
    root = Tk()
    window = sudokui.SudokuUI(root, grid)

    time_drawn = False
    while True:
        root.update_idletasks()
        root.update()
        backtrack.solve(grid, window, root)
        if not time_drawn:
            window.redraw(grid, round(time.time() - start_time, 10))
            time_drawn = True


def parse_puzzle(filename):
    puzzle_grid = []

    try:
        with open(filename, newline='') as puzzleFile:
            reader = csv.reader(puzzleFile, delimiter=',')
            for row in reader:
                puzzle_grid.append(list(map(lambda i: int(i), row)))
    except IOError:
        print("There was an error opening the file specified.")
        exit(1)

    return puzzle_grid

if __name__ == '__main__':
    main()
