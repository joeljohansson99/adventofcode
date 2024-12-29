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
    count = 0
    for line in input:
        words = line.split(" ")
        if not any([words.count(word) > 1 for word in words]):
            count += 1
    
    return count
                

def part2(input):
    count = 0
    for line in input:
        words = line.split(" ")
        valid = True
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if sorted(words[i]) == sorted(words[j]):
                    valid = False
        if valid:
            count += 1
    
    return count

if __name__ == "__main__":
    sys.exit(main())