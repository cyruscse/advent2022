def adjacent(head, tail):
    if head == tail:
        return True

    if head[0] == tail[0] and (head[1] == tail[1] + 1 or head[1] == tail[1] - 1):
        return True

    if head[1] == tail[1] and (head[0] == tail[0] + 1 or head[0] == tail[0] - 1):
        return True

    if head[0] == tail[0] + 1 and (head[1] == tail[1] + 1 or head[1] == tail[1] - 1):
        return True

    if head[0] == tail[0] - 1 and (head[1] == tail[1] + 1 or head[1] == tail[1] - 1):
        return True

    if head[1] == tail[1] + 1 and (head[0] == tail[0] + 1 or head[0] == tail[0] - 1):
        return True

    if head[1] == tail[1] - 1 and (head[0] == tail[0] + 1 or head[0] == tail[0] - 1):
        return True

    return False

def adjust(prev, tails, visits):
    for tidx in range(0, 9):
        curr = tails[tidx]

        if adjacent(prev, curr):
            prev = curr
            continue

        if prev[0] == curr[0]:
            if prev[1] > curr[1]:
                curr[1] = curr[1] + 1
            else:
                curr[1] = curr[1] - 1
        elif prev[1] == curr[1]:
            if prev[0] > curr[0]:
                curr[0] = curr[0] + 1
            else:
                curr[0] = curr[0] - 1
        elif prev[0] == curr[0] + 2 or prev[0] == curr[0] - 2 or prev[1] == curr[1] + 2 or prev[1] == curr[1] - 2:
            if prev[1] > curr[1]:
                curr[1] = curr[1] + 1
            else:
                curr[1] = curr[1] - 1
            
            if prev[0] > curr[0]:
                curr[0] = curr[0] + 1
            else:
                curr[0] = curr[0] - 1

        prev = curr

        if tidx == 8:
            visits.add((curr[0], curr[1]))

def main():
    in_file = open('input.txt', 'r')
    visits = set()
    head = [0, 0]
    tails = list()

    for _ in range(0, 9):
        tails.append([0, 0])

    visits.add((head[0], head[1]))

    for line in in_file:
        distance = int(line.strip().split()[1])
        move = line.strip().split()[0]
        newhead = head.copy()

        if move == 'R':
            newhead[0] = head[0] + distance
            
            while newhead[0] != head[0]:
                head[0] = head[0] + 1

                adjust(head, tails, visits)

        elif move == 'U':
            newhead[1] = head[1] - distance

            while newhead[1] != head[1]:
                head[1] = head[1] - 1

                adjust(head, tails, visits)

        elif move == 'L':
            newhead[0] = head[0] - distance

            while newhead[0] != head[0]:
                head[0] = head[0] - 1

                adjust(head, tails, visits)

        elif move == 'D':
            newhead[1] = head[1] + distance

            while newhead[1] != head[1]:
                head[1] = head[1] + 1

                adjust(head, tails, visits)

    print(len(visits))

main()