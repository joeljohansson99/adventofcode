import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day5.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    ranges = list()
    i = 0
    while input[i] != "":
        [a,b] = aoc.ints(input[i].replace("-", " "))
        ranges.append((a,b))
        i+=1
    count = 0
    
    for j in range(i+1,len(input)):
        id = int(input[j])
        fresh = False
        for (a,b) in ranges:
            if a <= id <= b:
                fresh = True
                break
        if fresh:
            count += 1
    return count 

def part2(input):
    ranges = list()
    i = 0
    while input[i] != "":
        [a,b] = aoc.ints(input[i].replace("-", " "))
        ranges.append((a,b))
        i+=1

    left = True
    while left:
        left = False
        for i in range(len(ranges)):
            (a,b) = ranges[i]
            inserted = False
            for j in range(len(ranges)):
                if i == j:
                    continue
                (l,h) = ranges[j]
                if l <= a <= h or l <= b <= h:
                    ranges[j] = (min(l,a), max(h,b))
                    inserted = True
            if inserted:
                ranges[i] = (0,0)
                left = True
        ranges = [n for n in ranges if n != (0,0)]
    
    total = 0
    for (a,b) in ranges:
        total += (b - a)+1

    return total


if __name__ == "__main__":
    sys.exit(main())