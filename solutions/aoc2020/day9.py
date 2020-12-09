from aocd import data
from aocd import submit


def part_a(data, n_preamble):
    lines = data.split('\n')
    preamble = list()
    for line in lines:
        number = int(line)
        if len(preamble) < n_preamble:
            preamble.append(number)
            continue
        pairs = {(number - x, x) if number - x in preamble and (number - x) != x else () for x in preamble} - {()}
        if len(pairs) == 0:
            return str(number)
        preamble.pop(0)
        preamble.append(number)
    print("All numbers valid")
    return str(None)


def part_b(data, n_preamble):
    target = int(part_a(data, n_preamble))
    lines = data.split('\n')
    contiguous = list()
    i = 0
    start = i
    while i < len(lines):
        number = int(lines[i])
        if sum(contiguous) < target:
            if len(contiguous) == 0:
                start = i
            contiguous.append(number)
            i += 1
        elif sum(contiguous) == target:
            return str(min(contiguous) + max(contiguous))
        else:
            i = start + 1
            contiguous = list()
    return str(None)


test_data = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

if __name__ == "__main__":
    assert part_a(test_data, 5) == "127"
    solution_a = part_a(data, 25)
    print(solution_a)
    # submit(solution_a, part="a", day=2, year=2020)

    print(part_b(test_data, 5))
    assert part_b(test_data, 5) == "62"
    solution_b = part_b(data, 25)
    print(solution_b)
    # submit(solution_b, part="b", day=2, year=2020)
