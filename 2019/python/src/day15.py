from collections import defaultdict
import os
import re
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day15.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

NORTH = 1
SOUTH = 2
WEST = 3
EAST = 4

WALL_HIT = 0
FORWARD = 1
OXYGEN = 2

def part1(input):
    nums = list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', input[0])))
    mem = defaultdict(int)
    for i in range(len(nums)):
        mem[i] = nums[i]
    rel = 0
    pc = 0
    walls = set()
    visited = dict()
    dir = (-1,0)
    pos = (0,0)
    steps = 0
    visited[pos] = 0

    while mem[pc] != 99:
        inst = str(mem[pc]).zfill(5)
        opcode = int(inst[-2:])

        if opcode == 1:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            write(mem, pc+3, int(inst[-5]), rel, val1 + val2)
            pc += 4
        elif opcode == 2:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            write(mem, pc+3, int(inst[-5]), rel, val1 * val2)
            pc += 4
        elif opcode == 3:
            choice = choose_dir(pos, visited, walls)
            dir = to_dir(choice)
            write(mem, pc+1, int(inst[-3]), rel, choice)
            pc += 2
        elif opcode == 4:
            val = read(mem, pc+1, int(inst[-3]), rel)
            if val == WALL_HIT:
                walls.add((pos[0] + dir[0], pos[1] + dir[1]))
            if val == FORWARD:
                pos = (pos[0] + dir[0], pos[1] + dir[1])
                visited[pos] = steps
            if val == OXYGEN:
                pos = (pos[0] + dir[0], pos[1] + dir[1])
                break
            pc += 2
        elif opcode == 5:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            if val1 != 0:
                pc = val2
            else:
                pc += 3
        elif opcode == 6:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            if val1 == 0:
                pc = val2
            else:
                pc += 3
        elif opcode == 7:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            write(mem, pc+3, int(inst[-5]), rel, 1 if val1 < val2 else 0)
            pc += 4
        elif opcode == 8:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            write(mem, pc+3, int(inst[-5]), rel, 1 if val1 == val2 else 0)
            pc += 4
        elif opcode == 9:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            rel += val1
            pc += 2
        
        steps+=1
    
    current = [(0,0)]
    seen = set()
    seen.add((0,0))
    steps = 0
    while current:
        steps += 1
        next = []
        for (r,c) in current:
            for (dr,dc) in neighbours((r,c)):
                if (dr,dc) in visited and (dr,dc) not in seen:
                    next.append((dr,dc))
                    seen.add((dr,dc))
                if (dr,dc) == pos:
                    return steps
        current = next

    return steps

def part2(input):
    nums = list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', input[0])))
    mem = defaultdict(int)
    for i in range(len(nums)):
        mem[i] = nums[i]
    rel = 0
    pc = 0
    walls = set()
    visited = set()
    dir = (-1,0)
    pos = (0,0)
    steps = 0
    visited.add(pos)
    oxygen = (0,0)

    while mem[pc] != 99:
        inst = str(mem[pc]).zfill(5)
        opcode = int(inst[-2:])

        if opcode == 1:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            write(mem, pc+3, int(inst[-5]), rel, val1 + val2)
            pc += 4
        elif opcode == 2:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            write(mem, pc+3, int(inst[-5]), rel, val1 * val2)
            pc += 4
        elif opcode == 3:
            choice = choose_dir(pos, visited, walls)
            if choice == 0:
                break
            dir = to_dir(choice)
            write(mem, pc+1, int(inst[-3]), rel, choice)
            pc += 2
        elif opcode == 4:
            val = read(mem, pc+1, int(inst[-3]), rel)
            if val == WALL_HIT:
                walls.add((pos[0] + dir[0], pos[1] + dir[1]))
            if val == FORWARD:
                pos = (pos[0] + dir[0], pos[1] + dir[1])
                visited.add(pos)
            if val == OXYGEN:
                pos = (pos[0] + dir[0], pos[1] + dir[1])
                visited.add(pos)
                oxygen = pos
            pc += 2
        elif opcode == 5:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            if val1 != 0:
                pc = val2
            else:
                pc += 3
        elif opcode == 6:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            if val1 == 0:
                pc = val2
            else:
                pc += 3
        elif opcode == 7:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            write(mem, pc+3, int(inst[-5]), rel, 1 if val1 < val2 else 0)
            pc += 4
        elif opcode == 8:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            val2 = read(mem, pc+2, int(inst[-4]), rel)
            write(mem, pc+3, int(inst[-5]), rel, 1 if val1 == val2 else 0)
            pc += 4
        elif opcode == 9:
            val1 = read(mem, pc+1, int(inst[-3]), rel)
            rel += val1
            pc += 2
        
        steps+=1
    
    current = [oxygen]
    seen = set()
    seen.add(oxygen)
    steps = 0
    while current:
        steps += 1
        next = []
        for (r,c) in current:
            for (dr,dc) in neighbours((r,c)):
                if (dr,dc) in visited and (dr,dc) not in seen:
                    next.append((dr,dc))
                    seen.add((dr,dc))
        current = next

    return steps - 1


def read(mem, i, mode, rel):
    if mode == 0:
        return mem[mem[i]]
    elif mode == 1:
        return mem[i]
    elif mode == 2:
        return mem[rel+mem[i]]

def write(mem, i, mode, rel, val):
    if mode == 0:
        mem[mem[i]] = val
    if mode == 1:
        sys.exit(-1)
    if mode == 2:
        mem[rel+mem[i]] = val

def choose_dir(pos, visited, walls):
    best_steps = float('inf')
    best = 0
    for n in [NORTH, SOUTH, EAST, WEST]:
        dir = to_dir(n)
        next = (pos[0] + dir[0], pos[1] + dir[1])
        if next in walls:
            continue
        steps = to_empty_square(next, visited, walls)
        if steps < best_steps and steps != -1:
            best_steps = steps
            best = n
    return best

def to_empty_square(pos, visited, walls):
    if pos not in visited and pos not in walls:
        return 0
    current = [pos]
    seen = set()
    seen.add(pos)
    steps = 0
    while current:
        steps += 1
        next = []
        for (r,c) in current:
            for (dr,dc) in neighbours((r,c)):
                if (dr,dc) in visited and (dr,dc) not in seen:
                    next.append((dr,dc))
                    seen.add((dr,dc))
                elif (dr,dc) not in visited and (dr,dc) not in walls:
                    return steps
        current = next
    return -1

def neighbours(pos):
    (r,c) = pos
    return [(r+1,c), (r-1,c), (r,c-1), (r,c+1)]

def to_dir(dir):
    if dir == NORTH:
        return (-1,0)
    if dir == SOUTH:
        return (1,0)
    if dir == EAST:
        return (0,1)
    if dir == WEST:
        return (0,-1)

if __name__ == "__main__":
    sys.exit(main())