# Sudoku Solver

A simple sodoku solving application that implements the backtrack algorithm. The program will open in an external TK window and will continuously update as the puzzle is being solved. Watch in realtime as the backtrack method is used to solve the provided puzzle.

More efficient algorithms may be added in the future.

## Usage

Use the included batch file:

```
.\run.bat
```

Or run it manually:

`main.py` takes in a single `.csv` filename as a command line argument. The CSV file should contain 0's to represent blank cells. See `easy.csv` and `hard.csv` for examples.

Terminal:

```
python3 src/main.py hard.csv
```

![screenshot of solved sudoku](screen.png)
