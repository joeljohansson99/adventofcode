from functools import cache
import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day14.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    key = input[0]
    used = 0
    for r in range(128):
        hash = knot_hash(key + "-" + str(r))
        blocks = ""
        for c in hash:
            blocks += bin(int(c, 16))[2:].zfill(4)
        used += blocks.count("1")
    return used    

def part2(input):
    key = input[0]
    used = set()
    for r in range(128):
        hash = knot_hash(key + "-" + str(r))
        blocks = ""
        for c in hash:
            blocks += bin(int(c, 16))[2:].zfill(4)
        for c in range(len(blocks)):
            if blocks[c] == "1":
                used.add((r,c))
                
    visited = set()
    groups = 0
    for pos in used:
        if pos in visited:
            continue
        groups += 1
        visited.add(pos)
        current = {pos}
        while current:
            next = set()
            for (r, c) in current:
                for (dr,dc) in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if (dr,dc) in used and (dr,dc) not in visited:
                        next.add((dr,dc))
                        visited.add((dr,dc))
            current = next

    return groups

@cache
def knot_hash(string):
    size = 256
    lengths = [ord(n) for n in string]
    lengths += [17, 31, 73, 47, 23]
    circle = list(range(size))
    pc = 0
    skip = 0
    for _ in range(64):
        for length in lengths:
            new_circle = circle.copy()
            indexes = [n % size for n in range(pc, pc + length)]
            for i in range(len(indexes)):
                new_circle[indexes[i]] = circle[indexes[len(indexes)-1-i]]
            circle = new_circle
            pc = (pc + length + skip) % len(circle)
            skip += 1

    dense_hash = []
    for i in range(16):
        num = circle[i*16]
        for j in range(1,16):
            num = num ^ circle[i*16+j]
        dense_hash.append(num)

    knot = ""
    for num in dense_hash:
        knot += str(hex(num))[2:].zfill(2)

    return knot

if __name__ == "__main__":
    sys.exit(main())