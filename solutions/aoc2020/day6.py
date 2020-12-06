from aocd import data
from aocd import submit

def part_a(data):
    groups = data.split("\n\n")
    sum = 0
    for group in groups:
        allYes = set()
        for person in group.split():
            yes = list(person)
            allYes.update(yes)
        sum += len(allYes)
    return str(sum)


def part_b(data):
    groups = data.split("\n\n")
    sum = 0
    for group in groups:
        sets = []
        for person in group.split():
            yes = list(person)
            sets.append(set(yes))
        set.intersection(*sets)
        sum += len(set.intersection(*sets))
    return str(sum)


test_data = """\
abc

a
b
c

ab
ac

a
a
a
a

b
"""

if __name__ == "__main__":
    assert part_a(test_data) == "11"
    solution_a = part_a(data)
    print(solution_a)
    #submit(solution_a, part="a", day=2, year=2020)

    assert part_b(test_data) == "6"
    solution_b = part_b(data)
    print(solution_b)
    #submit(solution_b, part="b", day=2, year=2020)

