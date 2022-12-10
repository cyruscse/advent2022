def main():
    in_file = open('input.txt', 'r')
    instructions = list()
    finalcycles = 0

    for line in in_file:
        instructions.append(line.strip())

        if line.strip() == 'noop':
            finalcycles = finalcycles + 1
        elif line.strip().split()[0] == 'addx':
            finalcycles = finalcycles + 2

    cycle = 0
    nextinstrcycle = 0
    x = 1
    fx = x
    instidx = 0
    future = dict()
    crt = list()

    while cycle <= finalcycles:
        instruction = ''

        if instidx < len(instructions) and cycle == nextinstrcycle:
            instruction = instructions[instidx]
            instidx = instidx + 1

        if instruction == '':
            pass
        elif instruction == 'noop':
            nextinstrcycle = cycle + 1
        elif instruction.split()[0] == 'addx':
            fx = fx + int(instruction.split()[1])
            future[cycle + 2] = fx
            nextinstrcycle = cycle + 2

        if cycle in future.keys():
            x = future[cycle]
            del future[cycle]

        adjcycle = cycle % 40

        if adjcycle == x or adjcycle == x - 1 or adjcycle == x + 1:
            crt.append('#')
        else:
            crt.append(' ')

        cycle = cycle + 1

    idx = 0

    for row in range(0, 6):
        for col in range(0, 40):
            print(crt[idx], end = '')
            idx = idx + 1
        print()

main()