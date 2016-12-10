def solve(grid):
    solved = False

    while not solved:
        solveCount = 0

        for row_index in range(len(grid)):
            if 0 not in grid[row_index]:
                solveCount += 1
                continue

            for val_index in range(len(grid[row_index])):
                if grid[row_index][val_index] == 0:
                    for new_val in range(1, 10):
                        val = compare_value(new_val, row_index, val_index, grid)
                        grid[row_index][val_index] = val if val else 0

        print(solveCount)
        if solveCount == 9:
            solved = True

    return grid

# Return True if val (1-9) is valid, false if not
def compare_value(val, row_index, col, grid):
    if val in grid[row_index]:
        return False
    for row_list in grid:
        if row_list[col] == val:
            return False
    if check_box(val, row_index, col, grid):
        return val
    return False

def check_box(val, row_index, col, grid):
    # Determine which row and column offsets to check for the box a value falls in
    box_row_index = row_index % 3
    box_col_index = col % 3

    for row_iter in range(3):
        starting_row = (row_index - box_row_index) + row_iter
        for col_iter in range(3):
            starting_col = (col - box_col_index) + col_iter
            if grid[starting_row][starting_col] == val:
                return False
    return True
