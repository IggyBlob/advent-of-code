from aocd import data
from aocd import submit

def part_a(data):
    rows = data.split()
    matrix = [list(row) for row in rows]
    rowIdx = 0
    colIdx = 0
    trees = 0
    print(matrix)
    while rowIdx < len(matrix):
        if colIdx >= len(matrix[0]):
            colIdx = colIdx - len(matrix[0])

        if matrix[rowIdx][colIdx] == '#':
            trees += 1
        rowIdx += 1
        colIdx += 3
    return str(trees)


def part_b(data):
    rows = data.split()
    matrix = [list(row) for row in rows]
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    res = 1
    for c, r in slopes:
        rowIdx = r
        colIdx = c
        trees = 0
        while rowIdx < len(matrix):
            if colIdx >= len(matrix[0]):
                colIdx = colIdx - len(matrix[0])

            if matrix[rowIdx][colIdx] == '#':
                trees += 1
            rowIdx += r
            colIdx += c
        res *= trees
    return str(res)


test_data = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

if __name__ == "__main__":
    assert part_a(test_data) == "7"
    solution_a = part_a(data)
    print(solution_a)

    assert part_b(test_data) == "336"
    solution_b = part_b(data)
    print(solution_b)
