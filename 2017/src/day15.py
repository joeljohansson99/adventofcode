import os
import re
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day15.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    A = int(re.search(r'\d+', input[0]).group())
    B = int(re.search(r'\d+', input[1]).group())

    count = 0
    for _ in range(40000000):
        A = (A * 16807) % 2147483647
        B = (B * 48271) % 2147483647
        if (A % 65536) == (B % 65536):
            count += 1
    return count


def part2(input):
    A = int(re.search(r'\d+', input[0]).group())
    B = int(re.search(r'\d+', input[1]).group())

    count = 0
    for a, b in zip(generate(A, 16807, 4), generate(B, 48271, 8)):
        if (a % 65536) == (b % 65536):
            count += 1
    return count

def generate(num, factor, modulo):
    count = 0
    while count < 5000000:
        num = (num * factor) % 2147483647
        if num % modulo == 0:
            count += 1
            yield num

if __name__ == "__main__":
    sys.exit(main())