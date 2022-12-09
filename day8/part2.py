# ugly but it works :) - this one was painful
def main():
    in_file = open('input.txt', 'r')
    trees_rows = list()
    scores = dict()

    for line in in_file:
        row = list()
        for height in line.strip():
            row.append(int(height))
        trees_rows.append(row)

    row = 1

    while row < len(trees_rows) - 1:
        col = 1

        score = 0
        stidx = row * len(trees_rows) + col
        stcol = col
        col = col + 1

        while col < len(trees_rows):
            if trees_rows[row][stcol] <= trees_rows[row][col] or col == len(trees_rows) - 1:
                score = score + 1

                if stidx not in scores.keys():
                    scores[stidx] = score
                else:
                    scores[stidx] = scores[stidx] * score
               
                score = 0
                stcol = stcol + 1
                col = stcol + 1
                stidx = row * len(trees_rows) + stcol
            else:
                score = score + 1
                col = col + 1

        col = len(trees_rows) - 2

        score = 0
        stidx = row * len(trees_rows) + col
        stcol = col
        col = col - 1

        while col != -1:
            if trees_rows[row][stcol] <= trees_rows[row][col] or col == 0:
                score = score + 1

                if stidx not in scores.keys():
                    scores[stidx] = score
                else:
                    scores[stidx] = scores[stidx] * score

                score = 0
                stcol = stcol - 1
                col = stcol - 1
                stidx = row * len(trees_rows) + stcol
            else:
                score = score + 1
                col = col - 1

        row = row + 1

    col = 1

    while col < len(trees_rows) - 1:
        row = 1

        score = 0
        stidx = row * len(trees_rows) + col
        strow = row
        row = row + 1

        while row < len(trees_rows):
            if trees_rows[strow][col] <= trees_rows[row][col] or row == len(trees_rows) - 1:
                score = score + 1

                if stidx not in scores.keys():
                    scores[stidx] = score
                else:
                    scores[stidx] = scores[stidx] * score
               
                score = 0
                strow = strow + 1
                row = strow + 1
                stidx = strow * len(trees_rows) + col
            else:
                score = score + 1
                row = row + 1

        row = len(trees_rows) - 2

        score = 0
        stidx = row * len(trees_rows) + col
        strow = row
        row = row - 1

        while row != -1:
            if trees_rows[strow][col] <= trees_rows[row][col] or row == 0:
                score = score + 1

                if stidx not in scores.keys():
                    scores[stidx] = score
                else:
                    scores[stidx] = scores[stidx] * score

                score = 0
                strow = strow - 1
                row = strow - 1
                stidx = strow * len(trees_rows) + col
            else:
                score = score + 1
                row = row - 1

        col = col + 1

    topscore = 0

    for idx in scores.keys():
        if scores[idx] > topscore:
            topscore = scores[idx]

    print(topscore)

main()