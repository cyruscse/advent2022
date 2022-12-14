def main():
    in_file = open('input.txt', 'r')
    entries = list()
    x = 0

    for line in in_file:
        y = 0
        row = list()
        for entry in line.strip():
            if entry == 'S':
                start = (x, y)
                row.append(ord('a'))
            elif entry == 'E':
                end = (x, y)
                row.append(ord('z'))
            else:
                row.append(ord(entry))
            y = y + 1
        entries.append(row)
        x = x + 1

    maxx = x
    maxy = y

    queue = list()
    visited = set()
    parents = dict()

    queue.append(start)
    visited.add(start)

    while len(queue) != 0:
        vert = queue.pop(0)

        if vert == end:
            break

        x = vert[0]
        y = vert[1]
        myval = entries[x][y]

        for (x, y) in ((x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)):
            if x < 0 or y < 0 or x >= maxx or y >= maxy:
                continue

            if entries[x][y] > (myval + 1):
                continue

            if (x, y) not in visited:
                visited.add((x, y))
                parents[(x, y)] = vert
                queue.append((x, y))

    node = end
    idx = 0

    while node != start:
        node = parents[node]
        idx = idx + 1

    print(idx)

main()