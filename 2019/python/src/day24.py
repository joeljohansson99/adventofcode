from collections import defaultdict
import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day24.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    bugs = [list(line) for line in input]
    seen = set()
    while True:
        state = "".join(["".join(b) for b in bugs])
        if state in seen:
            break
        seen.add(state)

        next = [b.copy() for b in bugs]
        for r in range(len(bugs)):
            for c in range(len(bugs[r])):
                adj = [bugs[dr][dc] for (dr,dc) in neighbours(r,c) if 0 <= dr < len(bugs) and 0 <= dc < len(bugs[0])]
                count = adj.count("#")
                if bugs[r][c] == "#" and count != 1:
                    next[r][c] = "."
                elif bugs[r][c] != "#" and 1 <= count <= 2:
                    next[r][c] = "#"
        bugs = next

    exp = 0
    bio = 0
    for r in range(len(bugs)):
        for c in range(len(bugs[r])):
            if bugs[r][c] == "#":
                bio += pow(2, exp)
            exp += 1
    return bio

def part2(input):
    bugs = defaultdict(set)
    level = 0
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == '#':
                if r == c == 2:
                    continue
                bugs[level].add((r,c))

    for _ in range(200):
        start = min(bugs.keys())-1
        end = max(bugs.keys())+2
        next = defaultdict(set)
        for i in range(start,end):
            calc(bugs, next, i)
        bugs = next

    return sum([len(bug) for (level, bug) in bugs.items()])

def calc(bugs, next, level):
    for r in range(5):
        for c in range(5):
            if r == c == 2:
                continue
            count = 0
            if r == 0:
                count += 1 if (1,2) in bugs[level+1] else 0
            if r == 4:
                count += 1 if (3,2) in bugs[level+1] else 0
            if c == 0:
                count += 1 if (2,1) in bugs[level+1] else 0
            if c == 4:
                count += 1 if (2,3) in bugs[level+1] else 0
            if c == 2 and r == 1:
                count += sum([1 for (dr,dc) in bugs[level-1] if dr == 0])
            if c == 2 and r == 3:
                count += sum([1 for (dr,dc) in bugs[level-1] if dr == 4])
            if c == 1 and r == 2:
                count += sum([1 for (dr,dc) in bugs[level-1] if dc == 0])
            if c == 3 and r == 2:
                count += sum([1 for (dr,dc) in bugs[level-1] if dc == 4])

            count += sum([1 for (dr,dc) in neighbours(r,c) if (dr,dc) in bugs[level]])


            if (r,c) in bugs[level]:
                if count == 1:
                    next[level].add((r,c))
            elif (r,c) not in bugs[level]:
                if 1 <= count <= 2:
                    next[level].add((r,c))


            


def neighbours(r,c):
    return [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

if __name__ == "__main__":
    sys.exit(main())