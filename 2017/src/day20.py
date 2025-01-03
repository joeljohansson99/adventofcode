from collections import defaultdict
import os
import re
import sys
from sympy.solvers import solve
from sympy import Eq, Symbol, diophantine

import z3

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day20.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    particles = []
    for line in input:
        [px,py,pz,vx,vy,vz,ax,ay,az] = list(map(int, re.findall(r'-?\d+', line)))
        particles.append((px,py,pz,vx,vy,vz,ax,ay,az))
    
    best = float('inf')
    t = 100000000000000
    for p, (px,py,pz,vx,vy,vz,ax,ay,az) in enumerate(particles):
        sx = px+vx*t+0.5*ax*(t**2)
        sy = py+vy*t+0.5*ay*(t**2)
        sz = pz+vz*t+0.5*az*(t**2)
        dist = (abs(sx)+abs(sy)+abs(sz))
        if dist < best:
            best = dist 
            bp = p
    
    return bp

def part2(input):
    particles = []
    for line in input:
        [px,py,pz,vx,vy,vz,ax,ay,az] = list(map(int, re.findall(r'-?\d+', line)))
        particles.append((px,py,pz,vx,vy,vz,ax,ay,az))
    
    for _ in range(50):
        counter = defaultdict(list)
        for i in range(len(particles)):
            (px,py,pz,vx,vy,vz,ax,ay,az) = particles[i]
            vx += ax
            vy += ay
            vz += az
            px += vx
            py += vy
            pz += vz
            particles[i] = (px,py,pz,vx,vy,vz,ax,ay,az)
            counter[(px,py,pz)].append(particles[i])

        for collisions in counter.values():
            if len(collisions) > 1:
                for p in collisions:
                    particles.remove(p)

    return len(particles)


if __name__ == "__main__":
    sys.exit(main())