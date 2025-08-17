import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day20.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    blocked = list()
    for line in input:
        [lo,hi] = aoc.ints(line)
        blocked.append((lo,abs(hi)))

    ip = 0
    while ip <= 4294967295:
        for (lo,hi) in blocked:
            if lo <= ip <= hi:
                ip = hi+1
                break
        else:
            return ip

def part2(input):
    blocked = list()
    for line in input:
        [lo,hi] = aoc.ints(line)
        blocked.append((lo,abs(hi)))

    allowed = set()
    ip = 0
    while ip <= 4294967295:
        for (lo,hi) in blocked:
            if lo <= ip <= hi:
                ip = hi+1
                break
        else:
            allowed.add(ip)
            ip += 1
    return len(allowed)

if __name__ == "__main__":
    sys.exit(main())
