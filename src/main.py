import csv
import sys
import time
import backtrack
import grid_util

def main():
    if len(sys.argv) != 2:
        print("Usage: maingit .py <file.csv>")
        exit(1)

    start_time = time.time()

    grid = parse_puzzle(sys.argv[1])
    backtrack_solution = backtrack.solve(grid)

    print("Solution found after %s" % (time.time() - start_time))

    if backtrack_solution:
        grid_util.write_grid(grid)
        for row in grid:
            print(row)
    else:
        print('No solution.')


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
