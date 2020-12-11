from aocd import data
# from aocd import submit
import numpy as np


def part_a(data):
    grid = read_data(data)
    resulting_grid = apply_until_stable(grid, get_neighbors, 4)
    return str(np.count_nonzero(resulting_grid == '#'))


def part_b(data):
    grid = read_data(data)
    resulting_grid = apply_until_stable(grid, get_visible, 5)
    return str(np.count_nonzero(resulting_grid == '#'))


def apply_until_stable(input_grid, adjacent_seats_func, min_occupied_seats):
    grid = input_grid
    new_grid = apply_rules(input_grid, adjacent_seats_func, min_occupied_seats)
    while not np.array_equal(grid, new_grid):
        grid = new_grid
        new_grid = apply_rules(new_grid, adjacent_seats_func, min_occupied_seats)
    return new_grid


def apply_rules(grid, adjacent_seats_func, min_occupied_seats):
    new_grid = grid.copy()
    for row, col in np.ndindex(grid.shape):
        if becomes_occupied(row, col, grid, adjacent_seats_func):
            new_grid[row, col] = '#'
        elif becomes_empty(row, col, grid, adjacent_seats_func, min_occupied_seats):
            new_grid[row, col] = 'L'
    return new_grid


def becomes_occupied(row, col, grid, adjacent_seats_func):
    return grid[row, col] == 'L' and '#' not in adjacent_seats_func(row, col, grid)


def becomes_empty(row, col, grid, adjacent_seats_func, min_occupied_seats):
    return grid[row, col] == '#' and adjacent_seats_func(row, col, grid).count('#') >= min_occupied_seats


def get_neighbors(row, col, grid):
    neighbors = []
    max_rows, max_cols = grid.shape
    if row - 1 >= 0:
        neighbors.append(grid[row - 1, col])
    if row - 1 >= 0 and col + 1 < max_cols:
        neighbors.append(grid[row - 1, col + 1])
    if col + 1 < max_cols:
        neighbors.append(grid[row, col + 1])
    if row + 1 < max_rows and col + 1 < max_cols:
        neighbors.append(grid[row + 1, col + 1])
    if row + 1 < max_rows:
        neighbors.append(grid[row + 1, col])
    if row + 1 < max_rows and col - 1 >= 0:
        neighbors.append(grid[row + 1, col - 1])
    if col - 1 >= 0:
        neighbors.append(grid[row, col - 1])
    if row - 1 >= 0 and col - 1 >= 0:
        neighbors.append(grid[row - 1, col - 1])
    return neighbors


def get_visible(row, col, grid):
    directions = [(-1, 0),
                  (-1, 1),
                  (0, 1),
                  (1, 1),
                  (1, 0),
                  (1, -1),
                  (0, -1),
                  (-1, -1)]
    max_rows, max_cols = grid.shape
    visible = []
    for row_delta, col_delta in directions:
        new_row = row + row_delta
        new_col = col + col_delta
        while 0 <= new_row < max_rows and 0 <= new_col < max_cols:
            if grid[new_row, new_col] == '#' or grid[new_row, new_col] == 'L':
                visible.append(grid[new_row, new_col])
                break
            new_row = new_row + row_delta
            new_col = new_col + col_delta
    return visible


def read_data(data):
    lines = data.split('\n')
    rows = len(lines)
    cols = len(lines[0])
    return np.array(list(data.replace('\n', ''))).reshape(rows, cols)


initial_state = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

state_0_a = """\
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""

state_1_a = """\
#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##"""

state_2_a = """\
#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##"""

state_3_a = """\
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##"""

state_4_a = """\
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##"""

state_0_b = """\
#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##"""

state_1_b = """\
#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#"""

state_2_b = """\
#.L#.##.L#
#L#####.LL
L.#.#..#..
##L#.##.##
#.##.#L.##
#.#####.#L
..#.#.....
LLL####LL#
#.L#####.L
#.L####.L#"""

state_3_b = """\
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##LL.LL.L#
L.LL.LL.L#
#.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLL#.L
#.L#LL#.L#"""

state_4_b = """\
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.#L.L#
#.L####.LL
..#.#.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#"""

state_5_b = """\
#.L#.L#.L#
#LLLLLL.LL
L.L.L..#..
##L#.#L.L#
L.L#.LL.L#
#.LLLL#.LL
..#.L.....
LLL###LLL#
#.LLLLL#.L
#.L#LL#.L#"""

if __name__ == "__main__":
    assert np.array_equal(apply_rules(read_data(initial_state), get_neighbors, 4), read_data(state_0_a))
    assert np.array_equal(apply_rules(read_data(state_0_a), get_neighbors, 4), read_data(state_1_a))
    assert np.array_equal(apply_rules(read_data(state_1_a), get_neighbors, 4), read_data(state_2_a))
    assert np.array_equal(apply_rules(read_data(state_2_a), get_neighbors, 4), read_data(state_3_a))
    assert np.array_equal(apply_rules(read_data(state_3_a), get_neighbors, 4), read_data(state_4_a))
    assert np.array_equal(apply_until_stable(read_data(initial_state), get_neighbors, 4), read_data(state_4_a))
    assert part_a(initial_state) == "37"
    solution_a = part_a(data)
    print(solution_a)
    # submit(solution_a, part="a", day=11, year=2020)

    assert np.array_equal(apply_rules(read_data(initial_state), get_visible, 5), read_data(state_0_b))
    assert np.array_equal(apply_rules(read_data(state_0_b), get_visible, 5), read_data(state_1_b))
    assert np.array_equal(apply_rules(read_data(state_1_b), get_visible, 5), read_data(state_2_b))
    assert np.array_equal(apply_rules(read_data(state_2_b), get_visible, 5), read_data(state_3_b))
    assert np.array_equal(apply_rules(read_data(state_3_b), get_visible, 5), read_data(state_4_b))
    assert np.array_equal(apply_rules(read_data(state_4_b), get_visible, 5), read_data(state_5_b))
    assert np.array_equal(apply_until_stable(read_data(initial_state), get_visible, 5), read_data(state_5_b))
    assert part_b(initial_state) == "26"
    solution_b = part_b(data)
    print(solution_b)
# submit(solution_b, part="b", day=11, year=2020)
