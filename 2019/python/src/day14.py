from collections import defaultdict
from email.policy import default
import os
import sys
import re
import math

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day14.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    reactions = dict()
    outputs = dict()
    for line in input:
        chemicals = [(int(chemical.split(" ")[0]), chemical.split(" ")[1]) for chemical in re.findall(r"\b[\d]+\s[a-zA-Z]+", line)]
        [output, chem] = chemicals.pop()
        outputs[chem] = output
        reactions[chem] = chemicals
    
    return calc(reactions, outputs, "FUEL", 1, defaultdict(int))

def part2(input):
    reactions = dict()
    outputs = dict()
    for line in input:
        chemicals = [(int(chemical.split(" ")[0]), chemical.split(" ")[1]) for chemical in re.findall(r"\b[\d]+\s[a-zA-Z]+", line)]
        [output, chem] = chemicals.pop()
        outputs[chem] = output
        reactions[chem] = chemicals

    return calc(reactions, outputs, "FUEL", 6226152, defaultdict(int))

def calc(reactions, outputs, target, amount, have):
    if target == "ORE":
        return amount
    if amount < have[target]:
        have[target] -= amount
        return 0
    
    amount -= have[target]
    chemicals = reactions[target]

    output_amount = outputs[target]
    factor = math.ceil(amount / output_amount)
    have[target] = output_amount * factor - amount
    
    ores = 0
    for (input_amount, chemical) in chemicals:
        ores += calc(reactions, outputs, chemical, input_amount*factor, have)
    return ores

if __name__ == "__main__":
    sys.exit(main())