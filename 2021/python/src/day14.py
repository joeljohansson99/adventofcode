from collections import defaultdict
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day14.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    polymer = input[0]
    templates = dict()
    for line in [line for line in input[2:] if line != ""]:
        pair, ins = line.split(" -> ")
        templates[pair] = ins
    
    counts = defaultdict(int)
    pairs = [polymer[i:i+2] for i in range(len(polymer)-1)]

    for pair in pairs:
        if pair != pairs[-1]:
            counts[pair[1]] -= 1
        for k,v in process(templates, pair, 10).items():
            counts[k] += v
    
    return max(counts.values())-min(counts.values())


def part2(input):
    polymer = input[0]
    templates = dict()
    for line in [line for line in input[2:] if line != ""]:
        pair, ins = line.split(" -> ")
        templates[pair] = ins
    
    counts = defaultdict(int)
    pairs = [polymer[i:i+2] for i in range(len(polymer)-1)]

    for pair in pairs:
        if pair != pairs[-1]:
            counts[pair[1]] -= 1
        for k,v in process(templates, pair, 40).items():
            counts[k] += v
    
    return max(counts.values())-min(counts.values())

cache = dict()
def process(T, pair, count):
    key = (pair, count)
    if key in cache:
        return cache[key]
    res = defaultdict(int)
    if count == 0:
        for c in pair:
            res[c] += 1
        cache[key] = res
        return res
    
    left = pair[0] + T[pair]
    right = T[pair] + pair[1]

    for k,v in process(T, left, count-1).items():
        res[k] += v
    for k,v in process(T, right, count-1).items():
        res[k] += v
    res[T[pair]] -= 1
    cache[key] = res
    return res

if __name__ == "__main__":
    sys.exit(main())