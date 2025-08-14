import functools
import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day18.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    traps = input[0]
    safe = traps.count(".")
    for _ in range(40-1):
        traps = getNext(traps)
        safe += traps.count(".")
    return safe

def part2(input):
    traps = input[0]
    safe = traps.count(".")
    for _ in range(400000-1):
        traps = getNext(traps)
        safe += traps.count(".")
    return safe

@functools.cache
def getNext(traps):
    next = ""
    for i in range(len(traps)):
        if isTrap(traps, i-1) != isTrap(traps, i+1):
            next += '^'
        else:
            next += '.'
    return next

def isTrap(traps, n):
    if 0 <= n < len(traps):
        return traps[n] == "^"
    return False

    
if __name__ == "__main__":
    sys.exit(main())
