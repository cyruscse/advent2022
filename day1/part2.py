def main():
    in_file = open('input.txt', 'r')

    large = 0
    largest = 0
    largest2 = 0
    largest3 = 0

    for line in in_file:
        if (line == '\n'):
            if large > largest:
                largest3 = largest2
                largest2 = largest
                largest = large
            elif large > largest2:
                largest3 = largest2
                largest2 = large
            elif large > largest3:
                largest3 = large

            large = 0
        else:
            large = large + int(line)

    if large > largest:
        largest3 = largest2
        largest2 = largest
        largest = large
    elif large > largest2:
        largest3 = largest2
        largest2 = large
    elif large > largest3:
        largest3 = large

    print(largest + largest2 + largest3)

main()