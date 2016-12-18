# Sudoku Solver

A tkitner application that visualizes solving a sudoku puzzle with the backtrack algorithm.

More algorithms may be added in the future.

## Usage

Use the included batch file:

```
.\run.bat
```

Or run it manually:

```
python3 src/main.py hard.csv
```

- - -

`main.py` takes in a single `.csv` filename as a command line argument. The CSV file should contain 0's to represent blank cells. See `easy.csv` and `hard.csv` for examples.


![screenshot of solved sudoku](screen.png)
