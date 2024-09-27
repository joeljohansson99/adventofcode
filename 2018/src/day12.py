import os
import sys
import math

def main():
    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day12.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    plants = input[0].replace(" ", "").split(":")[1]
    patterns = dict()
    
    for line in input[2:]:
        [pattern, res] = line.replace(" ","").split("=>")
        patterns[pattern] = res

    pot = 0
    for _ in range(0, 20):
        plants = "...." + plants + "...."
        next = ""
        for i in range(2, len(plants)-2):
            next += patterns[plants[i-2:i+3]]
        pot += next.find("#") - 2
        plants = next.strip("./")

    sum = 0
    for i in range(0, len(plants)):
        if plants[i] == "#":
            sum += pot
        pot += 1
    
    return sum

    
                
def part2(input):    
    plants = input[0].replace(" ", "").split(":")[1]
    patterns = dict()
    
    for line in input[2:]:
        [pattern, res] = line.replace(" ","").split("=>")
        patterns[pattern] = res

    pot = 0
    cache = set()
    gen = 0
    while True:
        if plants in cache:
            break
        else:
            cache.add(plants)
        plants = "...." + plants + "...."
        next = ""
        for i in range(2, len(plants)-2):
            next += patterns[plants[i-2:i+3]]
        pot += next.find("#") - 2
        plants = next.strip("./")
        gen += 1
        
    pot += 50000000000-gen
    sum = 0
    for i in range(0, len(plants)):
        if plants[i] == "#":
            sum += pot
        pot += 1

    return sum

if __name__ == "__main__":
    sys.exit(main())