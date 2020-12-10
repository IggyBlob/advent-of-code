from aocd import data
from aocd import submit

def part_a(data):
    effectiveJolts = 0
    jolts = {int(x) for x in data.split('\n')}
    joltCount = [0, 0, 0]
    for i in range(0, len(jolts)):
        if effectiveJolts + 1 in jolts:
            effectiveJolts += 1
            joltCount[0] += 1
        elif effectiveJolts + 2 in jolts:
            effectiveJolts += 2
            joltCount[1] += 1
        elif effectiveJolts + 3 in jolts:
            effectiveJolts += 3
            joltCount[2] += 1
        else:
            print("No next value found")
            break

    effectiveJolts += 3
    joltCount[2] += 1
    return joltCount[0], joltCount[2]


def part_b(data):
    jolts = {int(x) for x in data.split('\n')}
    graph = dict()
    build_graph(0, jolts, graph)
    return str(count_paths(graph))


def build_graph(parent, jolts, d):
    for joltDiff in range(1, 4):
        childCandidate = parent + joltDiff
        if childCandidate in jolts:
            children = d.get(parent)
            if children is None:
                d[parent] = [childCandidate]
                build_graph(childCandidate, jolts, d)
            elif childCandidate not in children:
                children.append(childCandidate)
                build_graph(childCandidate, jolts, d)


def count_paths(graph):
    childParentMapping = dict()
    for child, parents in graph.items():
        for parent in parents:
            if parent in childParentMapping:
                childParentMapping[parent].append(child)
            else:
                childParentMapping[parent] = [child]
    children = sorted(childParentMapping.keys())
    pathsToChild = dict()
    for child in children:
        sum = 0
        for parent in childParentMapping[child]:
            sum += pathsToChild[parent] if parent != 0 else 1
        pathsToChild[child] = sum if sum > 0 else 1
    return pathsToChild[children[-1]]


test_data = """\
16
10
15
5
1
11
7
19
6
12
4"""

test_data_2 = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


if __name__ == "__main__":
    assert part_a(test_data) == (7, 5)
    assert part_a(test_data_2) == (22, 10)
    a, b = part_a(data)
    print(a * b)
    # submit(solution_a, part="a", day=2, year=2020)

    assert part_b(test_data) == "8"
    assert part_b(test_data_2) == "19208"
    solution_b = part_b(data)
    print(solution_b)
    # submit(solution_b, part="b", day=2, year=2020)
