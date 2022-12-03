def main():
    in_file = open('input.txt', 'r')
    score = 0

    for line in in_file:
        first = list()
        second = list()
        idx = 0

        for char in line.strip():
            if idx < len(line.strip()) / 2:
                first.append(char)
            else:
                second.append(char)

            idx = idx + 1

        for char in first:
            if char in second:
                if char.islower():
                    score = score + (ord(char) - 96)
                else:
                    score = score + (ord(char) - 38)
                break

    print(score)


main()