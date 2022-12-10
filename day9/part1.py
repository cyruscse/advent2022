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

def main():
    in_file = open('input.txt', 'r')
    visits = set()
    head = [0, 0]
    tail = [0, 0]

    visits.add((tail[0], tail[1]))

    for line in in_file:
        distance = int(line.strip().split()[1])
        move = line.strip().split()[0]
        newhead = head.copy()

        if move == 'R':
            newhead[0] = head[0] + distance
            
            while newhead[0] != head[0]:
                head[0] = head[0] + 1

                if adjacent(head, tail):
                    continue

                if tail[1] > head[1]:
                    tail[1] = tail[1] - 1
                elif tail[1] < head[1]:
                    tail[1] = tail[1] + 1

                tail[0] = tail[0] + 1
                visits.add((tail[0], tail[1]))
        elif move == 'U':
            newhead[1] = head[1] - distance

            while newhead[1] != head[1]:
                head[1] = head[1] - 1

                if adjacent(head, tail):
                    continue

                if tail[0] > head[0]:
                    tail[0] = tail[0] - 1
                elif tail[0] < head[0]:
                    tail[0] = tail[0] + 1

                tail[1] = tail[1] - 1
                visits.add((tail[0], tail[1]))
        elif move == 'L':
            newhead[0] = head[0] - distance

            while newhead[0] != head[0]:
                head[0] = head[0] - 1

                if adjacent(head, tail):
                    continue

                if tail[1] > head[1]:
                    tail[1] = tail[1] - 1
                elif tail[1] < head[1]:
                    tail[1] = tail[1] + 1

                tail[0] = tail[0] - 1
                visits.add((tail[0], tail[1]))
        elif move == 'D':
            newhead[1] = head[1] + distance

            while newhead[1] != head[1]:
                head[1] = head[1] + 1

                if adjacent(head, tail):
                    continue

                if tail[0] > head[0]:
                    tail[0] = tail[0] - 1
                elif tail[0] < head[0]:
                    tail[0] = tail[0] + 1

                tail[1] = tail[1] + 1
                visits.add((tail[0], tail[1]))

    print(len(visits))
        #print(visits)

main()