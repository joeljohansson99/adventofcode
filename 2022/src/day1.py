import sys


def main():

    input = []
    with open('input/day1.txt') as f:
        tmp = []
        for line in f.readlines():
            l = line.replace("\n","")

            if len(l) == 0:
                input.append(tmp)
                tmp = []
                continue
            
            tmp.append(int(l))
        
        input.append(tmp)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    cals = [sum(i) for i in input]
    most = 0

    for cal in cals:
        if cal > most:
            most = cal

    return most

def part2(input):
    cals = [sum(i) for i in input]
    total = 0
    for k in range(0, 3):
        most = 0

        for cal in cals:

            if cal > most:
                most = cal
        total += most
        cals.remove(most)

    return total

if __name__ == "__main__":
    sys.exit(main())