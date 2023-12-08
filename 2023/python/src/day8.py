import os
import sys
from math import gcd

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day8.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    inst = input[0]
    network = dict()
    
    for l in input[2:]:
        network[l.split("=")[0].replace(" ", "")] = (l.split("=")[1].replace("(", "").replace(")", "").replace(" ", "").split(","))
    
    i = 0
    curr = "AAA"
    while (curr != "ZZZ"):
        curr = network[curr][0] if inst[i % len(inst)] == "L" else network[curr][1]
        i+=1
    return i        

def part2(input):
    inst = input[0]
    network = dict()
    
    for l in input[2:]:
        network[l.split("=")[0].replace(" ", "")] = (l.split("=")[1].replace("(", "").replace(")", "").replace(" ", "").split(","))
    
    currents = []
    for key,_ in network.items():
        if key[2] == 'A':
            currents.append(key)
         
    i = 0   
    zs = [0 for _ in currents]
    
    while (True):
        for j in range(0,len(currents)):
            currents[j] = network[currents[j]][0] if inst[i % len(inst)] == "L" else network[currents[j]][1]
            if currents[j][2] == 'Z':
                zs[j] = i+1
                
        i+=1
        if all([True if z > 0 else False for z in zs]):
            break
    
    lcm = 1
    for z in zs:
        lcm = lcm*z//gcd(lcm, z)
    
    return lcm


if __name__ == "__main__":
    sys.exit(main())