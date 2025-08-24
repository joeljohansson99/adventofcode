import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day15.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    capacities = []
    durabilities = []
    flavors = []
    textures = []

    for i in range(len(input)):
        capacity, durability, flavor, texture, _ = aoc.ints(input[i])
        capacities.append(capacity)
        durabilities.append(durability)
        flavors.append(flavor)
        textures.append(texture)

    best = 0
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                d = 100 - a - b - c
                capacity = max(0, a*capacities[0] + b*capacities[1] + c*capacities[2] + d*capacities[3])
                durability = max(0, a*durabilities[0] + b*durabilities[1] + c*durabilities[2] + d*durabilities[3])
                flavor = max(0, a*flavors[0] + b*flavors[1] + c*flavors[2] + d*flavors[3])
                texture = max(0, a*textures[0] + b*textures[1] + c*textures[2] + d*textures[3])

                score = capacity * durability * flavor * texture
                best = max(best, score)

    return best

def part2(input):
    capacities = []
    durabilities = []
    flavors = []
    textures = []
    calories = []

    for i in range(len(input)):
        capacity, durability, flavor, texture, calory = aoc.ints(input[i])
        capacities.append(capacity)
        durabilities.append(durability)
        flavors.append(flavor)
        textures.append(texture)
        calories.append(calory)

    best = 0
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                d = 100 - a - b - c
                calory = a*calories[0] + b*calories[1] + c*calories[2] + d*calories[3]
                if calory != 500:
                    continue
                capacity = max(0, a*capacities[0] + b*capacities[1] + c*capacities[2] + d*capacities[3])
                durability = max(0, a*durabilities[0] + b*durabilities[1] + c*durabilities[2] + d*durabilities[3])
                flavor = max(0, a*flavors[0] + b*flavors[1] + c*flavors[2] + d*flavors[3])
                texture = max(0, a*textures[0] + b*textures[1] + c*textures[2] + d*textures[3])
                
                score = capacity * durability * flavor * texture
                best = max(best, score)

    return best

if __name__ == "__main__":
    sys.exit(main())
