from functools import cache
import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day12.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    ret = 0
    for record in input:
        (springs, groups) = record.split(" ")
        groups = [int(x) for x in groups.split(",")]
        ret += rec(springs, tuple(groups), 0, 0)
    return ret

def part2(input):
    ret = 0
    k= 0
    for record in input:
        (springs, groups) = record.split(" ")
        groups = [int(x) for x in groups.split(",")]
        new_springs = springs + "?" + springs + "?" + springs + "?" + springs + "?" + springs
        new_groups = []
        for _ in range(0,5):
            new_groups.extend(groups)
            
        ret += rec(new_springs, tuple(new_groups), 0, 0)
    return ret

@cache
def rec(springs, groups, i, k):
    if k >= len(groups):
        if springs[i:].count("#") > 0:
            return 0
        else:
            return 1
    if len(springs) - i < sum(groups[k:]):
        return 0
    
    if springs[i] == '#':
        target = springs[i:i+groups[k]]
        
        if target.count("#") + target.count("?") == groups[k]:
            if i + groups[k] >= len(springs):
                return rec(springs, groups, i+groups[k]+1, k+1)
            if springs[i+groups[k]] != '#':
                return rec(springs, groups, i+groups[k]+1, k+1)
        return 0
    
    elif springs[i] == '.':
        return rec(springs, groups, i+1, k)
    
    else:
        target = springs[i:i+groups[k]]
        if target.count("#") + target.count("?") == groups[k]:
            if i + groups[k] >= len(springs):
                return rec(springs, groups, i+groups[k]+1, k+1) + rec(springs, groups, i+1, k,)
            elif springs[i+groups[k]] != '#':
                return rec(springs, groups, i+groups[k]+1, k+1) + rec(springs, groups, i+1, k,)
        
        return rec(springs, groups, i+1, k)
    
if __name__ == "__main__":
    sys.exit(main())