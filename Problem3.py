def problem3_part1(grid, step_right=3, step_down=1):
    tree_count = 0
    current_point = (0, 0)

    # While we are not out of the depth of the grid, keep calling Move to change the current point
    # and check if the current point is a tree. if so, increase the tree count.
    while current_point != 'Done':
        current_point = move(grid, current_point, step_right, step_down)
        if read_location(grid, current_point):
            tree_count += 1
    print(f"We encountered {tree_count} trees on our way")
    return tree_count


def read_location(grid, current_point, tree='#'):
    # returns true if the location is a tree
    if current_point != 'Done':
        return grid[current_point[0]][current_point[1]] == tree


def move(grid, current_point, step_right=3, step_down=1):
    # Returns the new location in form of tuple
    # Returns 'Done' if the new location is beyond the grid

    # Assuming all rows are equal length, taking the length of first row as grid length
    grid_length = len(grid[0])
    grid_depth = len(grid)
    new_point_row = current_point[0] + step_down

    # adjusting for 0 index by doing -1
    new_point_col = current_point[1] + step_right
    if new_point_row >= grid_depth:
        # We are out of the grid so stop processing
        return 'Done'
    if new_point_col >= grid_length:
        # If we have crossed the length, then we wrap around the length.
        new_point_col = new_point_col - grid_length
    return new_point_row, new_point_col


if __name__ == '__main__':
    with open('Data/Problem3.txt') as file:
        input_3 = file.readlines()
        input_3 = [x.strip() for x in input_3]
        sol = 1
        sol = sol * problem3_part1(input_3, 1, 1)
        sol = sol * problem3_part1(input_3, 3, 1)
        sol = sol * problem3_part1(input_3, 5, 1)
        sol = sol * problem3_part1(input_3, 7, 1)
        sol = sol * problem3_part1(input_3, 1, 2)
        print(f"The multiplication of all trees found is {sol}")





