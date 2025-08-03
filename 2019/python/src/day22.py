import os
import re
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day22.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    deck = 10007
    card = 2019

    (offset, increment) = getVars(deck, input)
    return ((card - offset) * pow(increment, -1, deck)) % deck

def part2(input):
    deck = 119315717514047
    pos = 2020
    times = 101741582076661

    (d_offset, d_increment) = getVars(deck, input)
    increment = pow(d_increment, times, deck)
    offset = (d_offset * ((1 - increment) * pow((1 - d_increment), -1, deck)))

    return (offset + increment * pos) % deck

def getVars(deck, input):
    offset = 0
    increment = 1
    for line in input:
        if "cut" in line:
            n = int(re.search(r'[+-]?\d+(?:\.\d+)?', line).group())
            offset += increment * n
        elif "deal with increment" in line:
            n = int(re.search(r'[+-]?\d+(?:\.\d+)?', line).group())
            increment *= pow(n, -1, deck)
        elif "deal into new stack" in line:
            increment *= -1
            offset += increment

    return (offset%deck, increment%deck)


if __name__ == "__main__":
    sys.exit(main())