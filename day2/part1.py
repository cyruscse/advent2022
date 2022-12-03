def main():
    in_file = open('input.txt', 'r')

    score = 0

    for line in in_file:
        opmove = line.split()[0]
        mymove = line.split()[1]

        if mymove == 'X':
            score = score + 1

            if opmove == 'A':
                score = score + 3
            elif opmove == 'C':
                score = score + 6
        elif mymove == 'Y':
            score = score + 2

            if opmove == 'A':
                score = score + 6
            elif opmove == 'B':
                score = score + 3
        elif mymove == 'Z':
            score = score + 3

            if opmove == 'B':
                score = score + 6
            elif opmove == 'C':
                score = score + 3
        else:
            print("unhandled")

    print(score)

main()