import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day13.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    num = int(input[0])
    current = [(1,1)]
    seen = {(1,1)}
    steps = 0
    while current:
        next = []
        for (r,c) in current:
            if (r,c) == (39,31):
                return steps
            for (dr,dc) in neighbours(r,c):
                if isOpen(dc,dr,num) and (dr,dc) not in seen:
                    next.append((dr,dc))
                    seen.add((dr,dc))
        current = next
        steps += 1

def part2(input):
    num = int(input[0])
    current = [(1,1)]
    seen = {(1,1)}
    steps = 0
    while steps < 50:
        next = []
        for (r,c) in current:
            for (dr,dc) in neighbours(r,c):
                if isOpen(dc,dr,num) and (dr,dc) not in seen:
                    next.append((dr,dc))
                    seen.add((dr,dc))
        current = next
        steps += 1
    return len(seen)

def neighbours(r,c):
    for (dr,dc) in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
        if 0 <= dr and 0 <= dc:
            yield (dr,dc)

def isOpen(x, y, num):
    n = x*x + 3*x + 2*x*y + y + y*y
    n += num
    bits = str(bin(n))[2:]
    ones = bits.count('1')
    return ones % 2 == 0


if __name__ == "__main__":
    sys.exit(main())
