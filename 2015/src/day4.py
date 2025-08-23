import hashlib
import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day4.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    key = input[0].encode()
    number = 0
    while True:
        hash = hashlib.md5(key + str(number).encode()).hexdigest()
        if all([c == "0" for c in hash[:5]]):
            return number
        number += 1

def part2(input):
    key = input[0].encode()
    number = 0
    while True:
        hash = hashlib.md5(key + str(number).encode()).hexdigest()
        if all([c == "0" for c in hash[:6]]):
            return number
        number += 1

if __name__ == "__main__":
    sys.exit(main())
