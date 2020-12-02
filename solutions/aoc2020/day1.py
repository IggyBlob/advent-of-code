from aocd import data
from aocd import submit


def part_a(data):
    s = set()
    for line in data:
        s.add(int(line))
    for val in s:
        missingVal = 2020 - val
        if missingVal in val:
            return str(val * missingVal)
    return None


def part_b(data):
    s = set()
    for line in data:
        s.add(int(line))
    for firstVal in s:
        missingVal = 2020 - firstVal
        residualSet = s.copy()
        residualSet.remove(firstVal)
        for secondVal in residualSet:
            thirdVal = missingVal - secondVal
            if thirdVal in residualSet:
                return str(firstVal * secondVal * thirdVal)
    return None


test_data = """\
1721
979
366
299
675
1456
"""

if __name__ == "__main__":
    assert part_a(test_data) == "514579"
    solution_a = part_a(data)
    print(solution_a)
    #submit(solution_a, part="a", day=2, year=2020)

    assert part_b(test_data) == "241861950"
    solution_b = part_b(data)
    print(solution_b)
    #submit(solution_b, part="b", day=2, year=2020)
