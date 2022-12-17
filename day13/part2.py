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
    packets = list()

    for line in in_file:
        if line == '\n':
            continue
        packets.append(line)

    packets.append('[[2]]')
    packets.append('[[6]]')

    npackets = list()

    for packet in packets:
        npacket = processline(packet, 1)[0]
        npackets.append(npacket)

    swapped = True

    while swapped == True:
        swapped = False
        idx = 0
        while idx < len(npackets) - 1:
            left = npackets[idx]
            right = npackets[idx + 1]

            if comparelines(left, right) == False:
                npackets[idx] = right
                npackets[idx + 1] = left
                swapped = True
            idx = idx + 1

    comp1 = list()
    c1bld = list()
    c1bld.append(2)
    comp1.append(c1bld)

    comp2 = list()
    c2bld = list()
    c2bld.append(6)
    comp2.append(c2bld)

    val1 = 0
    val2 = 0

    idx = 1

    for packet in npackets:
        if packet == comp1:
            val1 = idx
        elif packet == comp2:
            val2 = idx
        idx = idx + 1

    print(val1 * val2)

main()