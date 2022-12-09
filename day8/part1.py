# ugly but it works :)
def main():
    in_file = open('input.txt', 'r')
    trees_rows = list()
    visibleset = set()

    for line in in_file:
        row = list()
        for height in line.strip():
            row.append(int(height))
        trees_rows.append(row)

    row = 1
    visible = len(trees_rows) * 2 + ((len(trees_rows) - 2) * 2)

    while row < len(trees_rows) - 1:
        col = 1
        bar = trees_rows[row][0]

        while col != len(trees_rows) - 1:
            if bar >= trees_rows[row][col]:
                col = col + 1
                continue

            idx = row * len(trees_rows) + col

            bar = trees_rows[row][col]
            
            if idx not in visibleset:
                visibleset.add(idx)
                visible = visible + 1
            col = col + 1

        col = len(trees_rows) - 2
        bar = trees_rows[row][col + 1]

        while col != 0:
            if bar >= trees_rows[row][col]:
                col = col - 1
                continue

            idx = row * len(trees_rows) + col

            bar = trees_rows[row][col]

            if idx not in visibleset:
                visibleset.add(idx)
                visible = visible + 1
            col = col - 1

        row = row + 1

    col = 1

    while col < len(trees_rows) - 1:
        row = 1
        bar = trees_rows[0][col]

        while row != len(trees_rows) - 1:
            if bar >= trees_rows[row][col]:
                row = row + 1
                continue

            idx = row * len(trees_rows) + col

            bar = trees_rows[row][col]

            if idx not in visibleset:
                visibleset.add(idx)
                visible = visible + 1
            row = row + 1

        row = len(trees_rows) - 2
        bar = trees_rows[row + 1][col]

        while row != 0:
            if bar >= trees_rows[row][col]:
                row = row - 1
                continue

            idx = row * len(trees_rows) + col

            bar = trees_rows[row][col]

            if idx not in visibleset:
                visibleset.add(idx)
                visible = visible + 1
            row = row - 1

        col = col + 1

    print(visible)

main()