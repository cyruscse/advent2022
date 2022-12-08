def flatten(current):
    if type(current) is not list:
        return int(current)

    for path in current[1].keys():
        if len(current[1][path][1].keys()) == 0:
            current[1][path] = current[1][path][0]

        current[0] = current[0] + flatten(current[1][path])

    return(current[0])

def part1(current):
    value = 0

    if type(current) is not list:
        if current <= 100000:
            return current
        else:
            return 0
    elif current[0] <= 100000:
        value = current[0]

    for path in current[1].keys():
        value = value + part1(current[1][path])

    return value

def main():
    in_file = open('input.txt', 'r')
    system = [0, dict()]
    history = list()
    current = system
    dirsum = 0

    for line in in_file:
        splitline = line.strip().split(' ')
        
        if splitline[1] == 'cd':
            if dirsum != 0:
                current[0] = dirsum
            dirsum = 0
            if splitline[2] == '..':
                history.pop(-1)

                cursor = system

                for path in history:
                    cursor = cursor[1][path]
                    parent = path

                current = cursor
            else:
                parent = splitline[2]
                history.append(splitline[2])
                current[1][splitline[2]] = [0, dict()]
                current = current[1][splitline[2]]
                
        if '$' not in line:
            if splitline[0].isnumeric():
                dirsum = dirsum + int(splitline[0])

    current[0] = dirsum

    flatten(system)

    print(part1(system[1]['/']))

main()