from collections import defaultdict
import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day7.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    beams = set()
    splitters = set()
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == "S":
                beams.add((r,c))
            if input[r][c] == "^":
                splitters.add((r,c))

    splits = 0
    for _ in range(len(input)):
        next_beams = set()
        for b in beams:
            n = (b[0]+1,b[1])
            if n in splitters:
                next_beams.add((n[0],n[1]+1))
                next_beams.add((n[0],n[1]-1))
                splits += 1
            else:
                next_beams.add((n[0],n[1]))
        beams = next_beams

    return splits

def part2(input):
    beams = set()
    splitters = set()
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == "S":
                beams.add((r,c))
            if input[r][c] == "^":
                splitters.add((r,c))

    timelines = defaultdict(lambda:0)
    for b in beams:
        timelines[b] += 1
    for _ in range(len(input)):
        next_beams = set()
        for b in beams:
            n = (b[0]+1,b[1])
            if n in splitters:
                timelines[(n[0],n[1]+1)] += timelines[b]
                timelines[(n[0],n[1]-1)] += timelines[b]
                next_beams.add((n[0],n[1]+1))
                next_beams.add((n[0],n[1]-1))
            else:
                timelines[(n[0],n[1])] += timelines[b]
                next_beams.add((n[0],n[1]))
        beams = next_beams

    sum = 0
    for b in beams:
        sum += timelines[b]
    return sum

if __name__ == "__main__":
    sys.exit(main())