def solve(grid):
    solved = False

    while not solved:
        solve_count = 0

        for row_index in range(len(grid)):
            if 0 not in grid[row_index]:
                solve_count += 1
                continue

            for col_index in range(len(grid[row_index])):
                if grid[row_index][col_index] == 0:
                    for new_val in range(1, 10):
                        val = compare_value(new_val, row_index, col_index, grid)
                        grid[row_index][col_index] = val
                        if val != 0:
                            break

        print(solve_count)
        if solve_count == 9:
            solved = True

    return grid

# Return True if val (1-9) is valid, false if not
def compare_value(val, row_index, col_index, grid):
    if val in grid[row_index]:
        return 0
    for row_list in grid:
        if row_list[col_index] == val:
            return 0
    if check_box(val, row_index, col_index, grid):
        return val
    return 0

def check_box(val, row_index, col_index, grid):
    # Determine which row and column offsets to check for the box a value falls in
    box_row_index = row_index % 3
    box_col_index = col_index % 3

    for row_iter in range(3):
        starting_row = (row_index - box_row_index) + row_iter
        for col_iter in range(3):
            starting_col = (col_index - box_col_index) + col_iter

            if starting_row == row_index and starting_col == col_index:
                continue

            if grid[starting_row][starting_col] == val:
                return False

    return True
