import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day2.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    valid = 0
    for line in input[0].split(","):
        [l,h] = aoc.ints(line.replace("-", " "))
        for i in range(l, h+1):
            id = str(i)
            for k in range(len(id)):
                if id[:k] == id[k:]:
                    valid += i
    return valid

def part2(input):
    valid = 0
    for line in input[0].split(","):
        [l,h] = aoc.ints(line.replace("-", " "))
        for ii in range(l, h+1):
            id = str(ii)
            for j in range(1, (len(id) // 2)+1):
                groups = [id[i:i + j] for i in range(0, len(id), j)]
                if len(set(groups)) == 1:
                    valid += ii
                    break
    return valid
if __name__ == "__main__":
    sys.exit(main())