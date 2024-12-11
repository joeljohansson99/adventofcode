import functools
import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day11.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    numbers = list(map(int, re.findall(r'\d+', input[0])))
    count = 0
    for num in numbers:
        count += step(num, 25)
    return count

def part2(input):
    numbers = list(map(int, re.findall(r'\d+', input[0])))
    count = 0
    for num in numbers:
        count += step(num, 75)
    return count

@functools.cache
def step(num, limit):
    if limit == 0:
        return 1
    count = 0
    if num == 0:
        count += step(1, limit-1)
    elif len(str(num)) % 2 == 0:
        split = str(num)
        i = len(split) // 2
        count += step(int(split[:i]), limit-1)
        count += step(int(split[i:]), limit-1)
    else:
        count += step(num*2024, limit-1)
    return count

if __name__ == "__main__":
    sys.exit(main())