def solve(grid):
    return 'stub'

# Return True if val (1-9) is valid, false if not
def compare_value(val, row_index, col, grid):
    if val in grid[row_index]:
        return False
    for row_list in grid:
        if row_list[col] == val:
            return False
    return check_box(val, row_index, col, grid)

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
