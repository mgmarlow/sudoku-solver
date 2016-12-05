import csv
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: maingit .py <file.csv>")
        exit(1)

    grid = parsePuzzle(sys.argv[1])
    for line in grid:
        print(line)

def parsePuzzle(filename):
    puzzleGrid = []

    try:
        with open(filename, newline='') as puzzleFile:
            reader = csv.reader(puzzleFile, delimiter=',')
            for row in reader:
                puzzleGrid.append(list(map(lambda i: int(i), row)))
    except IOError:
        print("There was an error opening the file specified.")
        exit(1)

    return puzzleGrid

if __name__ == '__main__':
    main()
