# Sudoku Solver

A simple sodoku solving application that implements the backtrack algorithm.

More efficient algorithms may be added in the future.

## Usage

`main.py` takes in a single `.csv` filename as a command line argument. The program will open in an external TK window and will continuously update as the puzzle is being solved. Watch in realtime as the backtrack method is used to solve a provided puzzle.

The CSV file should contain 0's to represent blank cells. See `easy.csv` and `hard.csv` for examples.

Terminal:

```
python3 src/main.py hard.csv
```

![screenshot of solved sudoku](screen.png)
