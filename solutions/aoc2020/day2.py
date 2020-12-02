from aocd import data
from aocd import submit


def part_a(data):
    validPasswords = 0
    for line in data:
        lineParts = line.split(' ')
        charCount = lineParts[0]
        char = lineParts[1][:-1]
        password = lineParts[2]

        minCharCount = int(charCount.split('-')[0])
        maxCharCount = int(charCount.split('-')[1])

        actualCharCount = password.count(char)
        if minCharCount <= actualCharCount <= maxCharCount:
            validPasswords += 1

    return str(validPasswords)


def part_b(data):
    validPasswords = 0
    for line in data:
        lineParts = line.split(' ')
        positions = lineParts[0]
        char = lineParts[1][:-1]
        password = lineParts[2]

        firstPosition = int(positions.split('-')[0])
        secondPosition = int(positions.split('-')[1])

        charOnFirstPosition = password[firstPosition - 1] == char
        charOnSecondPosition = password[secondPosition - 1] == char
        if charOnFirstPosition ^ charOnSecondPosition:
            validPasswords += 1
            
    return str(validPasswords)


test_data = """\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

if __name__ == "__main__":
    assert part_a(test_data) == "2"
    solution_a = part_a(data)
    print(solution_a)
    #submit(solution_a, part="a", day=2, year=2020)

    assert part_b(test_data) == "1"
    solution_b = part_b(data)
    print(solution_b)
    #submit(solution_b, part="b", day=2, year=2020)
