def write_grid(grid, filename='sol.txt'):
    with open(filename, 'w') as result:
        result.truncate(0)
        for row in grid:
            result.write(str(row) + '\n')
