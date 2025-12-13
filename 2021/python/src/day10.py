import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day10.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

CHUNK = {
    "<" : ">",
    "(" : ")",
    "[" : "]",
    "{" : "}"
}

def part1(input):
    POINTS = {
        ")" : 3,
        "]" : 57,
        "}" : 1197,
        ">" : 25137
    }

    score = 0
    for line in input:
        stack = list()
        for c in line:
            if c in CHUNK.keys():
                stack.append(c)
            elif not c == CHUNK[stack.pop()]:
                score += POINTS[c]
                break
    return score

def part2(input):
    POINTS = {
        ")" : 1,
        "]" : 2,
        "}" : 3,
        ">" : 4
    }

    scores = []
    for line in input:
        stack = list()
        for c in line:
            if c in CHUNK.keys():
                stack.append(c)
            elif not c == CHUNK[stack.pop()]:
                break
        else:
            score = 0
            for c in stack[::-1]:
                score *= 5
                score += POINTS[CHUNK[c]]
            scores.append(score)
    return sorted(scores)[len(scores)//2]

if __name__ == "__main__":
    sys.exit(main())