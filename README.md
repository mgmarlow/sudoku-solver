# Sudoku Solver

A simple sodoku solving application that implements the backtrack algorithm.

## Usage

The main program takes in a `csv` filename as its only argument. If the program successfully solves the puzzle, the solution
will be printed to the terminal with a benchmark and to an external file, `sol.txt`. The CSV file should contain `0`s
to represent blank cells.


Terminal:

```
python3 src/main.py hard.csv
```