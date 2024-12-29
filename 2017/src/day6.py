import os
import re
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day6.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    seen = set()
    banks = list(map(int, re.findall(r'\d+', input[0])))
    cycles = 0
    while True:
        state = tuple(banks)
        if state in seen:
            return cycles
        seen.add(state)

        bank_idx = banks.index(max(banks))
        blocks = banks[bank_idx]
        banks[bank_idx] = 0
        i = (bank_idx + 1)%len(banks)
        while blocks:
            banks[i] +=1
            blocks -= 1
            i = (i+1)%len(banks)
        cycles += 1

                

def part2(input):
    seen = dict()
    banks = list(map(int, re.findall(r'\d+', input[0])))
    cycles = 0
    while True:
        state = tuple(banks)
        if state in seen:
            return cycles - seen[state]
        seen[state] = cycles

        bank_idx = banks.index(max(banks))
        blocks = banks[bank_idx]
        banks[bank_idx] = 0
        i = (bank_idx + 1)%len(banks)
        while blocks:
            banks[i] +=1
            blocks -= 1
            i = (i+1)%len(banks)
        cycles += 1

if __name__ == "__main__":
    sys.exit(main())