from aocd import data
from aocd import submit

def part_a(data):
    ruleMap = dict()
    rules = data.split("\n")
    for rule in rules:
        key = rule.split(" contain ")[0][:-5]
        values = list()
        for valStr in rule.split(" contain ")[1].split(', '):
            if len(valStr.split(' ')) == 4:
                count, adj, color, _ = valStr.split(' ')
            else:
                continue
            val = (int(count), adj + " " + color)
            values.append(val)
        ruleMap[key] = values

    searchStrs = {'shiny gold'}

    print(ruleMap)
    allKeys = set()
    while True:
        keys = set()
        for key, valList in ruleMap.items():
            for count, adjCol in valList:

                if adjCol in searchStrs:
                    keys.add(key)
        if len(keys) == 0:
            break
        allKeys.update(keys)
        searchStrs = set(keys)

    ruleKeys = set(ruleMap.keys())
    return str(len(ruleKeys.intersection(allKeys)))


def part_b(data):
    ruleMap = dict()
    rules = data.split("\n")
    for rule in rules:
        key = rule.split(" contain ")[0][:-5]
        values = list()
        for valStr in rule.split(" contain ")[1].split(', '):
            if len(valStr.split(' ')) == 4:
                count, adj, color, _ = valStr.split(' ')
            else:
                continue
            val = (int(count), adj + " " + color)
            values.append(val)
        ruleMap[key] = values

    print(str(calcSumOfBagsRec(ruleMap, 'shiny gold')))
    return str(calcSumOfBagsRec(ruleMap, 'shiny gold'))

def calcSumOfBagsRec(rules, searchStr):
    s = 0
    for count, bagType in rules[searchStr]:
        print(bagType)
        s += count + count * calcSumOfBagsRec(rules, bagType)
    return s

test_data = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

test_data2 = """\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""


if __name__ == "__main__":
    assert part_a(test_data) == "4"
    solution_a = part_a(data)
    print(solution_a)
    #submit(solution_a, part="a", day=2, year=2020)

    assert part_b(test_data2) == "126"
    solution_b = part_b(data)
    print(solution_b)
    #submit(solution_b, part="b", day=2, year=2020)

