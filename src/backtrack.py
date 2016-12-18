def solve(grid, window, tk):
    # Keep track of row and column indices
    record = [0, 0]

    if (not find_empty_loc(grid, record)):
        return True

    row = record[0]
    col = record[1]

    for num in range(1, 10):
        if check_proper_position(grid, row, col, num):
            # Attempt number placement
            grid[row][col] = num

            window.redraw(grid)
            tk.update()

            if (solve(grid, window, tk)):
                return True

            # Reset if unsuccessful
            grid[row][col] = 0

    return False

def find_empty_loc(grid, record):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                record[0] = row
                record[1] = col
                return True
    return False

def used_in_row(grid, row, num):
    for col in range(9):
        if grid[row][col] == num:
            return True
    return False

def used_in_col(grid, col, num):
    for row in range(9):
        if(grid[row][col] == num):
            return True
    return False

def used_in_box(grid, row, col, num):
    for box_row in range(3):
        starting_row_index = box_row + (row - row % 3)
        for box_col in range(3):
            starting_col_index = box_col + (col - col % 3)
            if grid[starting_row_index][starting_col_index] == num:
                return True
    return False

def check_proper_position(grid, row, col, num):
    return not used_in_row(grid, row, num) \
           and not used_in_col(grid, col, num) \
           and not used_in_box(grid, row, col, num)
