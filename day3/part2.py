def main():
    in_file = open('input.txt', 'r')
    score = 0
    bag1 = ''
    bag2 = ''
    bag3 = ''

    for line in in_file:
        idx = 0

        if bag1 == '':
            bag1 = line
        elif bag2 == '':
            bag2 = line
        elif bag3 == '':
            bag3 = line

            for char in bag1:
                if char in bag2:
                    if char in bag3:
                        if char.islower():
                            score = score + (ord(char) - 96)
                        else:
                            score = score + (ord(char) - 38)
                        break
            bag1 = ''
            bag2 = ''
            bag3 = ''

    print(score)


main()