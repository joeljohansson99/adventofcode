import os
import sys
import re
import math

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day12.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    planets = len(input)
    positions = dict()
    velocities = dict()

    for i in range(planets):
        pos = list(map(int, re.findall(r'[+-]?\d+(?:\.\d+)?', input[i])))
        positions[i] = pos
        velocities[i] = [0,0,0]
    
    for _ in range(1000):
        for i in range(planets):
            for k in range(planets):
                if positions[i][0] < positions[k][0]:
                    velocities[i][0] += 1
                elif positions[i][0] > positions[k][0]:
                    velocities[i][0] -= 1
                if positions[i][1] < positions[k][1]:
                    velocities[i][1] += 1
                elif positions[i][1] > positions[k][1]:
                    velocities[i][1] -= 1
                if positions[i][2] < positions[k][2]:
                    velocities[i][2] += 1
                elif positions[i][2] > positions[k][2]:
                    velocities[i][2] -= 1
        
        for i in range(planets):
            positions[i][0] += velocities[i][0]
            positions[i][1] += velocities[i][1]
            positions[i][2] += velocities[i][2]

    total_energy = 0
    for i in range(planets):
        pot_energy = abs(positions[i][0]) + abs(positions[i][1]) + abs(positions[i][2])
        kin_energy = abs(velocities[i][0]) + abs(velocities[i][1]) + abs(velocities[i][2])
        total_energy += pot_energy * kin_energy

    return total_energy

def part2(input):
    planets = len(input)
    positions = dict()
    velocities = dict()

    for i in range(planets):
        pos = list(map(int, re.findall(r'[+-]?\d+(?:\.\d+)?', input[i])))
        positions[i] = pos
        velocities[i] = [0,0,0]
    steps = 0

    done = list()
    orbits = list()
    seen = list()
    for i in range(3):
        done.append(False)
        seen.append(set())
        orbits.append(0)

    while not all(done):
        for i in range(3):
            if not done[i]:
                state = tuple([p[i] for p in positions.values()] + [v[i] for v in velocities.values()])
                if state in seen[i]:
                    orbits[i] = steps
                    done[i] = True
                else:
                    seen[i].add(state)

        for i in range(planets):
            for k in range(planets):
                if positions[i][0] < positions[k][0]:
                    velocities[i][0] += 1
                elif positions[i][0] > positions[k][0]:
                    velocities[i][0] -= 1
                if positions[i][1] < positions[k][1]:
                    velocities[i][1] += 1
                elif positions[i][1] > positions[k][1]:
                    velocities[i][1] -= 1
                if positions[i][2] < positions[k][2]:
                    velocities[i][2] += 1
                elif positions[i][2] > positions[k][2]:
                    velocities[i][2] -= 1
        
        for i in range(planets):
            positions[i][0] += velocities[i][0]
            positions[i][1] += velocities[i][1]
            positions[i][2] += velocities[i][2]
        
        steps+=1

    lcm = 1
    for i in orbits:
        lcm = lcm*i//math.gcd(lcm, i)
    return lcm

if __name__ == "__main__":
    sys.exit(main())