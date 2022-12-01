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
    cals.sort(reverse=True)

    return cals[0]

def part2(input):
    cals = [sum(i) for i in input]
    cals.sort(reverse=True)

    return sum(cals[0:3])

if __name__ == "__main__":
    sys.exit(main())