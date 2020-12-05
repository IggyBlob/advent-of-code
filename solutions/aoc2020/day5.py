from aocd import data
from aocd import submit

def part_a(data):
    codes = data.split()
    maxId = -1
    for code in codes:
        if len(code) != 10:
            print("skipping code", code)
            continue
        row = calcRow(code[0:7])
        col = calcCol(code[7:])
        newId = row * 8 + col
        if newId > maxId:
            maxId = newId

    return str(maxId)

def calcRow(code):
    lower = 0
    upper = 127
    for char in code[0:6]:
        value = (upper - lower) // 2
        if char == 'F':
            # taking the lower half
            upper = lower + value
        elif char == 'B':
            # taking the upper half
            lower = lower + value + 1
    if code[6] == 'F':
        return lower
    else:
        return upper

def calcCol(code):
    lower = 0
    upper = 7
    for char in code[0:2]:
        value = (upper - lower) // 2
        if char == 'L':
            # taking the lower half
            upper = lower + value
        elif char == 'R':
            # taking the upper half
            lower = lower + value + 1
    if code[2] == 'L':
        return lower
    else:
        return upper



def part_b(data):
    codes = data.split()
    ids = []
    for code in codes:
        if len(code) != 10:
            print("skipping code", code)
            continue
        row = calcRow(code[0:7])
        col = calcCol(code[7:])
        newId = row * 8 + col
        print(newId)
        ids.append(newId)

    ids = sorted(ids)
    missing = [x for x in range(ids[0], ids[-1]+1) if x not in ids]
    return str(missing[0])


if __name__ == "__main__":
    assert calcRow('BFFFBBFRRR') == 70
    assert calcRow('FFFBBBFRRR') == 14
    assert calcRow('BBFFBBFRLL') == 102

    assert calcCol('RRR') == 7
    assert calcCol('RRR') == 7
    assert calcCol('RLL') == 4

    assert part_a('BFFFBBFRRR') == "567"
    assert part_a('FFFBBBFRRR') == "119"
    assert part_a('BBFFBBFRLL') == "820"
    solution_a = part_a(data)
    print(solution_a)

    solution_b = part_b(data)
    print(solution_b)

