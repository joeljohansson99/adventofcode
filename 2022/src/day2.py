import sys


def main():

    input = []
    with open('input/day2.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")

            input.append(l.split(" "))
    print(input)
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    sum = 0
    for i in input:
        if i[1] == 'X':
            sum += 1
            if i[0] == 'A':
                sum += 3
            elif i[0] == 'C':
                sum += 6
        
        elif i[1] == 'Y':
            sum += 2
            if i[0] == 'A':
                sum += 6
            elif i[0] == 'B':
                sum += 3
        
        elif i[1] == 'Z':
            sum += 3
            if i[0] == 'B':
                sum += 6
            elif i[0] == 'C':
                sum += 3
    return sum

def part2(input):
    sum = 0
    for i in input:
        if i[1] == 'X':
            if i[0] == 'A':
                sum += 3 + 0
            elif i[0] == 'B':
                sum += 1 + 0
            elif i[0] == 'C':
                sum += 2 + 0
        
        elif i[1] == 'Y':
            if i[0] == 'A':
                sum += 1 + 3
            elif i[0] == 'B':
                sum += 2 + 3
            elif i[0] == 'C':
                sum += 3 + 3
        
        elif i[1] == 'Z':
            if i[0] == 'A':
                sum += 2 + 6
            elif i[0] == 'B':
                sum += 3 + 6
            elif i[0] == 'C':
                sum += 1 + 6
    return sum

if __name__ == "__main__":
    sys.exit(main())