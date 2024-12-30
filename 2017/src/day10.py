import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day10.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    size = 256
    lengths = [int(n) for n in input[0].split(",")]
    circle = list(range(size))
    pc = 0
    skip = 0
    for length in lengths:
        new_circle = circle.copy()
        indexes = [n % size for n in range(pc, pc + length)]
        for i in range(len(indexes)):
            new_circle[indexes[i]] = circle[indexes[len(indexes)-1-i]]
        circle = new_circle
        pc = (pc + length + skip) % len(circle)
        skip += 1

    return circle[0] * circle[1]
                

def part2(input):
    size = 256
    lengths = [ord(n) for n in input[0]]
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
        knot += str(hex(num))[2:]

    return knot

if __name__ == "__main__":
    sys.exit(main())