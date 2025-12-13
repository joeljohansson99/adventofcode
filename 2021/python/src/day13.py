import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day13.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    dots = set()
    for i in range(len(input)):
        if input[i] == "":
            break
        x,y = aoc.ints(input[i])
        dots.add((x,y))

    for k in range(i+1, len(input)):
        next = set()
        if "y" in input[k]:
            fold = aoc.ints(input[k])[0]
            for (x,y) in dots:
                if y > fold:
                    d = abs(y - fold)
                    next.add((x, fold - d))
                else:
                    next.add((x, y))
        else:
            fold = aoc.ints(input[k])[0]
            for (x,y) in dots:
                if x > fold:
                    d = abs(x - fold)
                    next.add((fold - d, y))
                else:
                    next.add((x, y))
        dots = next
        break
    return len(dots)

def part2(input):
    dots = set()
    for i in range(len(input)):
        if input[i] == "":
            break
        x,y = aoc.ints(input[i])
        dots.add((x,y))

    for k in range(i+1, len(input)):
        next = set()
        if "y" in input[k]:
            fold = aoc.ints(input[k])[0]
            for (x,y) in dots:
                if y > fold:
                    d = abs(y - fold)
                    next.add((x, fold - d))
                else:
                    next.add((x, y))
        else:
            fold = aoc.ints(input[k])[0]
            for (x,y) in dots:
                if x > fold:
                    d = abs(x - fold)
                    next.add((fold - d, y))
                else:
                    next.add((x, y))
        dots = next

    for y in range(max([y for (x,y) in dots])+1):
        for x in range(max([x for (x,y) in dots])+1):
            if (x,y) in dots:
                print("█", end="")
            else:
                print(" ", end="")
        print("")

if __name__ == "__main__":
    sys.exit(main())