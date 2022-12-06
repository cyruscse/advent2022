def main():
    in_file = open('input.txt', 'r')
    letters = list()
    idx = 0

    for line in in_file:
        for letter in line:
            if len(letters) != 4:
                letters.append(letter)
            else:
                letters.pop(0)
                letters.append(letter)

            if len(letters) == 4:
                if len(set(letters)) == len(letters):
                    print(idx + 1)
                    return
            idx = idx + 1


main()