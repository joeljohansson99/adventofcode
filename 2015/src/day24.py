import functools
from itertools import combinations
from operator import mul
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day24.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    nums = aoc.ints(" ".join(input))
    target = sum(nums)//3
    numset = tuple(nums)
    
    seen = set()
    min_entangle = float('inf')
    for size in range(1, len(numset)):
        for comb in combinations(numset, size):
            if sum(comb) != target:
                continue
            comb_key = frozenset(comb)
            if comb_key in seen:
                continue
            seen.add(comb_key)

            remaining = tuple(x for x in numset if x not in comb)
            if not list(getCombs(target, 0, remaining)):
                continue

            ent = functools.reduce(mul, comb, 1)
            if ent < min_entangle:
                min_entangle = ent

        if min_entangle < float('inf'):
            break

    return min_entangle
    

def part2(input):
    nums = aoc.ints(" ".join(input))
    nums.sort(reverse=True)
    target = sum(nums)//4
    numset = tuple(nums)
    
    seen = set()
    min_entangle = float('inf')
    for size in range(1, len(numset)):
        for comb in combinations(numset, size):
            if sum(comb) != target:
                continue
            comb_key = frozenset(comb)
            if comb_key in seen:
                continue
            seen.add(comb_key)

            remaining = tuple(x for x in numset if x not in comb)
            if not list(getCombs(target, 0, remaining)):
                continue

            ent = functools.reduce(mul, comb, 1)
            if ent < min_entangle:
                min_entangle = ent

        if min_entangle < float('inf'):
            break

    return min_entangle


@functools.cache
def getCombs(total, start, available):
    results = []
    for i in range(start, len(available)):
        n = available[i]
        if n == total:
            results.append((n,))
        elif n < total:
            for rest in getCombs(total - n, i + 1, available):
                results.append((n,) + rest)
        else:
            continue
    return tuple(results)

if __name__ == "__main__":
    sys.exit(main())
