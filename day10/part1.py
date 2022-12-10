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
        else:
            print('oops', line)
            exit()

    cycle = 0
    nextinstrcycle = 0
    x = 1
    fx = x
    instidx = 0
    future = dict()
    strength = 0

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
        else:
            print('oops2')
            exit()

        cycle = cycle + 1

        if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
            strength = strength + cycle * x

        if cycle in future.keys():
            x = future[cycle]
            del future[cycle]

    print(strength)

main()