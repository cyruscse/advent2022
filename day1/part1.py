def main():
    in_file = open('input.txt', 'r')

    large = 0
    largest = 0

    for line in in_file:
        if (line == '\n'):
            if large > largest:
                largest = large
            large = 0
        else:
            large = large + int(line)

    print(largest)

main()