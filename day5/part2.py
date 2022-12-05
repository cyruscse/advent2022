def main():
    in_file = open('input.txt', 'r')
    nof_stacks = 0
    stacks = list()
    reading_instructions = False

    for line in in_file:
        if 'move' in line:
            reading_instructions = True
            
        if reading_instructions == False and '[' in line:
            if nof_stacks == 0:
                nof_stacks = int(len(line) / 4)

                for _ in range(0, nof_stacks):
                    stacks.append(list())

            idx = 0

            line = line.replace(']', '[')
            line = line.replace('\n', '')

            for entry in line.split('['):
                if entry == '' or entry == ' ':
                    continue
                if len(entry) > 1:
                    lenentry = len(entry)
                    while lenentry >= 4:
                        idx = idx + 1
                        lenentry = lenentry - 4
                else:
                    stacks[idx].append(entry)
                    idx = idx + 1


        if reading_instructions == True:
            line = line.split()
            quantity = int(line[1])
            start = int(line[3])
            end = int(line[5])

            popped = list()

            for _ in range(0, quantity):
                popped.append(stacks[start - 1].pop(0))

            stacks[end - 1] = popped + stacks[end - 1]

    for stack in stacks:
        print(stack[0], end = '')
            

main()