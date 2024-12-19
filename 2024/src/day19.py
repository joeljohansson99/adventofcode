import functools
import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day19.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    towels = set()
    for towel in input[0].split(","):
        towels.add(towel.strip())

    ans = 0
    for pattern in input[2:]:
        if match(towels, pattern):
           ans += 1

    return ans 

cache = dict()
def match(towels, pattern):
    if pattern in cache:
        return cache[pattern]
    if pattern == "":
        return True
    for towel in towels:
        if towel == pattern[:len(towel)]:
            if match(towels, pattern[len(towel):]):
                cache[pattern] = True
                return True
    cache[pattern] = False
    return False

def part2(input):
    towels = set()
    for towel in input[0].split(","):
        towels.add(towel.strip())

    ans = 0
    for pattern in input[2:]:
        ans += all_match(towels, pattern)
    return ans

cache2 = dict()
def all_match(towels, pattern):
    if pattern in cache2:
        return cache2[pattern]
    if pattern == "":
        return 1
    
    matches = 0
    for towel in towels:
        if towel == pattern[:len(towel)]:
            matches += all_match(towels, pattern[len(towel):])
            
    cache2[pattern] = matches
    return matches

if __name__ == "__main__":
    sys.exit(main())