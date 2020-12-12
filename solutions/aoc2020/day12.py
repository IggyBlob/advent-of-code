from aocd import data
# from aocd import submit


def calcBearing(bearing, instruction, unit):
    value = degrees_of_bearing(bearing)
    if instruction == 'L':
        value = value - unit if value - unit >= 0 else 360 + (value - unit)
    if instruction == 'R':
        value = abs(value + unit) % 360

    if value == 0:
        return 'N'
    elif value == 180:
        return 'S'
    elif value == 90:
        return 'E'
    elif value == 270:
        return 'W'
    print("No bearing found for value", value)
    exit(-1)


def degrees_of_bearing(bearing):
    if bearing == 'N':
        return 0
    if bearing == 'S':
        return 180
    if bearing == 'E':
        return 90
    if bearing == 'W':
        return 270


def part_a(data):
    bearing = 'E'
    ew = ns = 0
    for instruction, unit in read_data(data):
        if instruction == 'N':
            ns += unit
        elif instruction == 'S':
            ns -= unit
        elif instruction == 'E':
            ew += unit
        elif instruction == 'W':
            ew -= unit
        elif instruction == 'L' or instruction == 'R':
            bearing = calcBearing(bearing, instruction, unit)
        elif instruction == 'F':
            if bearing == 'N':
                ns += unit
            elif bearing == 'S':
                ns -= unit
            elif bearing == 'E':
                ew += unit
            elif bearing == 'W':
                ew -= unit
        else:
            print("Invalid instruction:", instruction)
    return str(abs(ew) + abs(ns))


def rotate_waypoint(instruction, unit, wpew, wpns):
    mappings = [(wpew, wpns), (wpns, -1 * wpew), (-1 * wpew, -1 * wpns), (-1 * wpns, wpew)]
    i = 0
    for _ in range(unit // 90):
        if instruction == 'R':
            i = (i + 1) % 4
        elif instruction == 'L':
            i = i - 1 if i > 0 else 3
        else:
            print("Instruction not found:", instruction)
    return mappings[i]


def part_b(data):
    wpew = 10
    wpns = 1
    ew = ns = 0
    for instruction, unit in read_data(data):
        if instruction == 'N':
            wpns += unit
        elif instruction == 'S':
            wpns -= unit
        elif instruction == 'E':
            wpew += unit
        elif instruction == 'W':
            wpew -= unit
        elif instruction == 'L' or instruction == 'R':
            wpew, wpns = rotate_waypoint(instruction, unit, wpew, wpns)
        elif instruction == 'F':
            ew += unit * wpew
            ns += unit * wpns
        else:
            print("Invalid instruction:", instruction)
    return str(abs(ew) + abs(ns))


def read_data(data):
    return [(row[0], int(row[1:])) for row in data.split('\n')]


test_data = """\
F10
N3
F7
R90
F11"""

if __name__ == "__main__":
    assert part_a(test_data) == "25"
    solution_a = part_a(data)
    print(solution_a)
    # submit(solution_a, part="a", day=12, year=2020)

    assert part_b(test_data) == "286"
    solution_b = part_b(data)
    print(solution_b)
    # submit(solution_b, part="b", day=12, year=2020)
