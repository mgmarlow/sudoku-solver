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
                        if only_possible_val(new_val, row_index, grid):
                            print('possible!')
                            grid[row_index][col_index] = new_val
                            break

        #print(solve_count)
        if solve_count == 9:
            solved = True

    return grid

# Returns True if only one integer can go in the given space
def only_possible_val(test_val, row_index, grid):
    col_count = 0

    for col_index in range(len(grid[row_index])):
        # print("{%d, %d, %d}" % (row_index, col_index, test_val))
        if proper_value(test_val, row_index, col_index, grid):
            col_count += 1
    #print(col_count)

    return True if col_count == 1 else False

# Return True if val (1-9) is valid, false if not
def proper_value(val, row_index, col_index, grid):
    # Check row
    if val in grid[row_index]:
        return False

    # Check Column
    for row_list in grid:
        if row_list[col_index] == val:
            return False

    # Check surrounding box
    if check_box(val, row_index, col_index, grid):
        return True

    return False

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
