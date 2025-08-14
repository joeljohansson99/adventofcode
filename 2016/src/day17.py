import hashlib
import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day17.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

DIRECTIONS = [((0,-1), "U"), ((0,1), "D"), ((-1,0), "L"), ((1,0), "R")]

def part1(input):
    password = input[0]
    Q = [((0,0), password)]
    while Q:
        (pos, path) = Q.pop(0)
        if pos == (3,3):
            return path[len(password):]
        for i in range(len(DIRECTIONS)):
            (dir, d) = DIRECTIONS[i]
            next = add(pos,dir)
            if 0 <= next[0] <= 3 and 0 <= next[1] <= 3:
                hash = hashlib.md5(path.encode()).digest().hex()
                if isOpen(hash, i):
                    Q.append((next, path+d))
    
        Q = sorted(Q, key=lambda x: len(x[1]))

def part2(input):
    password = input[0].encode()
    longest = 0
    Q = [((0,0), "")]
    while Q:
        (pos, path) = Q.pop(0)
        if pos == (3,3):
            if len(path) > longest:
                longest = len(path)
            continue
        for i in range(len(DIRECTIONS)):
            (dir, d) = DIRECTIONS[i]
            next = add(pos,dir)
            if 0 <= next[0] <= 3 and 0 <= next[1] <= 3:
                hash = hashlib.md5(password + path.encode()).digest().hex()
                if isOpen(hash, i):
                    Q.append((next, path+d))
    
        Q = sorted(Q, key=lambda x: len(x[1]))
    
    return longest

def add(a,b):
    return (a[0] + b[0], a[1] + b[1])

def isOpen(hash, i):
    return hash[i] in ['b','c','d','e','f']

if __name__ == "__main__":
    sys.exit(main())
