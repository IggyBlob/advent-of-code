from aocd import data
from aocd import submit


def part_a(data):
    accumulator = 0
    currentPos = 0
    instructions = data.split('\n')
    visited = [0] * len(instructions)
    while currentPos < len(instructions):
        instruction = instructions[currentPos]
        op, val = instruction.split(' ')
        if op == 'nop':
            visited[currentPos] = 1
            currentPos += 1
            continue
        if op == 'acc':
            visited[currentPos] = 1
            currentPos += 1
            accumulator += int(val)
            continue
        if op == 'jmp':
            visited[currentPos] = 1
            currentPos += int(val)
            if visited[currentPos] != 0:
                return str(accumulator)
            continue
        print("undefined op code found", op)
    print("finished without loop")
    return str(accumulator)

def part_b(data):
    instructions = data.split('\n')
    line = -1
    for i in instructions:
        line += 1
        print(i)
        if i.startswith('nop'):
            repOp = 'jmp'
        elif i.startswith('jmp'):
            repOp = 'nop'
        else:
            continue
        accumulator = 0
        currentPos = 0
        visited = [0] * len(instructions)
        while currentPos < len(instructions):
            instruction = instructions[currentPos]
            op, val = instruction.split(' ')
            if visited[currentPos] != 0:
                break
            if currentPos == line:
                op = repOp
            if op == 'nop':
                visited[currentPos] = 1
                currentPos += 1
            elif op == 'acc':
                visited[currentPos] = 1
                currentPos += 1
                accumulator += int(val)
            elif op == 'jmp':
                visited[currentPos] = 1
                currentPos += int(val)
            else:
                print("undefined op code found", op)
        if currentPos >= len(instructions):
            print("finished without infinite loop")
            return str(accumulator)
    print("error")
    return str(None)


test_data = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

if __name__ == "__main__":
    assert part_a(test_data) == "5"
    solution_a = part_a(data)
    print(solution_a)
    # submit(solution_a, part="a", day=2, year=2020)

    print(part_b(test_data))
    assert part_b(test_data) == "8"
    solution_b = part_b(data)
    print(solution_b)
    # submit(solution_b, part="b", day=2, year=2020)
