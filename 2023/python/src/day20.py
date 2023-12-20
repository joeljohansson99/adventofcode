from math import gcd
import os
import sys
from shapely.geometry import Point, Polygon
import numpy as np 

R = (0,1)
L = (0,-1)
U = (-1,0)
D = (1,0)

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day20.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    mods = dict()
    mem = dict()
    flips = dict()
    for line in input:
        tmp = line
        n = ""
        if tmp[0] == '&':
            n = tmp[0]
            tmp = tmp[1:]
        elif tmp[0] == '%':
            n = tmp[0]
            tmp = tmp[1:]
        (flip, out) = tmp.split(" -> ")
        mods[flip] = [x.replace(" ", "") for x in out.split(",")]
        if n == "&":
            mem[flip] = dict()
        if n == "%":
            flips[flip] = 0
    
    stack = []
    high = 0
    low = 0
    
    for neg, dic in mem.items():
        for flip, vals in mods.items():
            if neg in vals:
                dic[flip] = 0
    
    for _ in range(0, 1000):
        low += 1
        for m in mods["broadcaster"]:
            stack.append(("broadcaster", m, 0))
            low += 1
        while stack:
            (f, t, sig) = stack.pop(0)
            if t == "output":
                continue
            if t in mem:
                mem[t][f] = sig
                if sum(mem[t].values()) == len(mem[t]):
                    for m in mods[t]:
                        low += 1
                        stack.append((t, m, 0))
                else:
                    for m in mods[t]:
                        high += 1
                        stack.append((t, m, 1))
            else:
                if sig == 0:
                    flips[t] = (flips[t] + 1) % 2
                
                    if flips[t] == 0:
                        for m in mods[t]:
                            low += 1
                            stack.append((t, m, 0))
                    else:
                        for m in mods[t]:
                            high += 1
                            stack.append((t, m, 1))
    return low * high    
                
def part2(input):
    mods = dict()
    mem = dict()
    flips = dict()
    for line in input:
        tmp = line
        n = ""
        if tmp[0] == '&':
            n = tmp[0]
            tmp = tmp[1:]
        elif tmp[0] == '%':
            n = tmp[0]
            tmp = tmp[1:]
        (flip, out) = tmp.split(" -> ")
        mods[flip] = [x.replace(" ", "") for x in out.split(",")]
        if n == "&":
            mem[flip] = dict()
        if n == "%":
            flips[flip] = 0
    
    stack = []
    high = 0
    low = 0
    
    for neg, dic in mem.items():
        for flip, vals in mods.items():
            if neg in vals:
                dic[flip] = 0
    b = 0
    target = ['vt','sk','xc','kk']
    loop = dict()
    while b < 5000:
        b+=1
        for m in mods["broadcaster"]:
            stack.append(("broadcaster", m, 0))
        while stack:
            (f, t, sig) = stack.pop(0)
            if t == "output":
                continue
            if t in mem:
                mem[t][f] = sig
                if sum(mem[t].values()) == len(mem[t]):
                    for m in mods[t]:
                        if m in target:
                            loop[m] = b
                        if m == "rx":
                            return b
                        stack.append((t, m, 0))
                else:
                    for m in mods[t]:
                        stack.append((t, m, 1))
            else:
                if sig == 0:
                    flips[t] = (flips[t] + 1) % 2
                
                    if flips[t] == 0:
                        for m in mods[t]:
                            if m in target:
                                loop[m] = b
                            if m == "rx":
                                return b
                            stack.append((t, m, 0))
                    else:
                        for m in mods[t]:
                            stack.append((t, m, 1))
    
    lcm = 1
    for z in loop.values():
        lcm = lcm*z//gcd(lcm, z)
    return lcm
    
if __name__ == "__main__":
    sys.exit(main())