def main():
    in_file = open('input.txt', 'r')
    items = dict()
    ops = dict()
    tests = dict()
    testpass = dict()
    testfail = dict()
    inspections = dict()
    product = 1
    monkey = 0

    for line in in_file:
        if "Monkey" in line:
            monkey = int(line.split()[1][:-1])
            items[monkey] = list()
            inspections[monkey] = 0
        elif "Starting" in line:
            for idx in range(2, len(line.split())):
                items[monkey].append(int(line.split()[idx].strip(',')))
        elif "Operation" in line:
            ops[monkey] = (line.split()[-2], line.split()[-1])
        elif "Test" in line:
            tests[monkey] = int(line.split()[-1])
            product = product * tests[monkey]
        elif "true" in line:
            testpass[monkey] = int(line.split()[-1])
        elif "false" in line:
            testfail[monkey] = int(line.split()[-1])

    round = 1

    while round != 10001:
        for monkey in items.keys():
            monkeyitems = items[monkey].copy()
            for item in items[monkey]:
                inspections[monkey] = inspections[monkey] + 1
                monkeyitems.pop(0)
                operation = ops[monkey][0]
                value = ops[monkey][1]

                if value.isnumeric():
                    value = int(value)
                else:
                    value = item

                if operation == '*':
                    value = item * value
                elif operation == '+':
                    value = item + value
                else:
                    print('oops')

                value = value % product

                if value % tests[monkey] == 0:
                    items[testpass[monkey]].append(value)
                else:
                    items[testfail[monkey]].append(value)

            items[monkey] = monkeyitems

        round = round + 1

    top1 = 0
    top2 = 0

    for monkey in inspections.keys():
        if inspections[monkey] > top1:
            if top1 > top2:
                top2 = top1
            top1 = inspections[monkey]
        elif inspections[monkey] > top2:
            top2 = inspections[monkey]

    print(top1 * top2)

main()