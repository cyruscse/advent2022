def processline(line, idx):
    packet = list()
    bstr = ''

    while idx < len(line):
        char = line[idx]
        if char == '[':
            np, idx = processline(line, idx + 1)
            packet.append(np)
        elif char == ',':
            if len(bstr) != 0:
                packet.append(int(bstr))
                bstr = ''
            idx = idx + 1
            continue
        elif char == ']':
            if len(bstr) != 0:
                packet.append(int(bstr))
            return packet, idx
        else:
            bstr = bstr + char
        idx = idx + 1

    return packet, idx

def comparelines(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return None

        return left < right

    elif isinstance(left, list) and isinstance(right, list):
        idx = 0
        dpass = None

        while idx < len(left) and idx < len(right):
            if (comp := comparelines(left[idx], right[idx])) is not None:
                return comp
            idx = idx + 1

        return comparelines(len(left), len(right))
        
    elif isinstance(left, list):
        return comparelines(left, [right])

    return comparelines([left], right)

def main():
    in_file = open('input.txt', 'r')
    left = None
    right = None
    idx = 1
    valid = list()

    for line in in_file:
        if left != None and right != None:
            if comparelines(left, right) == True:
                valid.append(idx)

            left = None
            right = None
            idx = idx + 1
        elif left == None:
            left = processline(line.strip(), 1)[0]
        elif right == None:
            right = processline(line.strip(), 1)[0]

    if comparelines(left, right) == True:
        valid.append(idx)

    svalid = 0

    for entry in valid:
        svalid = svalid + entry

    print(svalid)

main()