def main():
    in_file = open('input.txt', 'r')

    score = 0

    for line in in_file:
        opmove = line.split()[0]
        result = line.split()[1]

        if result == 'X':
            if opmove == 'A':
                score = score + 3
            elif opmove == 'B':
                score = score + 1
            elif opmove == 'C':
                score = score + 2
        elif result == 'Y':
            if opmove == 'A':
                score = score + 4
            elif opmove == 'B':
                score = score + 5
            elif opmove == 'C':
                score = score + 6
        elif result == 'Z':
            if opmove == 'A':
                score = score + 8
            elif opmove == 'B':
                score = score + 9
            elif opmove == 'C':
                score = score + 7
        else:
            print("unhandled")

    print(score)

main()