import os
import sys
import networkx as nx # type: ignore

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day20.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    open = set()
    doors = dict()
    seen = set()
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == ".":
                open.add((r,c))
            elif input[r][c].isalpha():
                (door, pos, inner) = getDoor(r,c, input)
                if pos not in seen:
                    if door in doors:
                        doors[door].append(pos)
                    else:
                        doors[door] = [pos]
                seen.add(pos)
    
    G = nx.Graph()
    for (door, posses) in doors.items():
        if door == "ZZ":
            continue
        for pos in posses:
            for (tag, steps) in search(pos, door, doors, open):
                if tag == "AA":
                    continue
                if tag != "ZZ":
                    steps+=1
                G.add_edge(door, tag, weight=steps)
                
    return nx.shortest_path_length(G, "AA", "ZZ", weight='weight')

def part2(input):
    open = set()
    doors = dict()
    seen = set()
    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == ".":
                open.add((r,c))
            elif input[r][c].isalpha():
                (door, pos, inner) = getDoor(r,c, input)
                if pos not in seen:
                    if door == "AA" or door == "ZZ":
                        doors[door] = pos
                        continue
                    if door not in doors:
                        doors[door] = [0,0]
                    doors[door][int(inner)] = pos
                seen.add(pos)
                
    mappings = dict()
    for (door, pos) in doors.items():
        if door != "AA" and door != "ZZ":
            mappings[pos[0]] = (pos[1], -1)
            mappings[pos[1]] = (pos[0], 1)

    return bfs(doors["AA"], doors["ZZ"], mappings, open)

def bfs(start, end, mappings, open):
    (x,y) = start
    current = [(x, y, 0)]
    seen = set()
    seen.add((x, y, 0))
    steps = 0
    while current:
        next = []
        for (x,y,level) in current:
            if (x,y) in mappings:
                ((dx,dy),dl) = mappings[(x,y)]
                if level >= 0 and (dx,dy,level+dl) not in seen:
                    next.append((dx, dy, level+dl))
            for (dx,dy) in neighbors(x,y):
                if (dx,dy) in open and (dx,dy,level) not in seen:
                    next.append((dx,dy,level))
        steps += 1
        for (x,y,level) in next:
            if (x,y) == end and level == 0:
                return steps
            seen.add((x,y,level))
        current = next
    return None   


def search(start, tag, doors, open):
    current = [start]
    seen = set()
    reachable = set()
    steps = 0
    while current:
        steps += 1
        next = []
        for (r,c) in current:
            for (dr,dc) in neighbors(r,c):
                if (dr,dc) not in seen:
                    if (dr,dc) in open:
                        next.append((dr,dc))
                    for (door, posses) in doors.items():
                        if door != tag and (dr,dc) in posses:
                            reachable.add((door, steps))
                    seen.add((dr,dc))
        current = next
    return reachable

def getDoor(r,c, input):
    door = [(r,c)]
    for (dr,dc) in neighbors(r,c):
        if dr >= 0 and dc >= 0 and dr < len(input) and dc < len(input[0]) and input[dr][dc].isalpha():
            door.append((dr,dc))
    
    door = sorted(door, key=lambda x: x[0] + x[1])
    tag = "".join([input[r][c] for (r,c) in door])
    inner = not any([r == 0 or c == 0 or r == len(input)-1 or c == len(input[0])-1 for (r,c) in door])

    for (r,c) in neighbors(door[0][0], door[0][1]) + neighbors(door[1][0], door[1][1]):
        if r >= 0 and c >= 0 and r < len(input) and c < len(input[0]) and input[r][c] == ".":
            pos = (r,c)
    
    return (tag, pos, inner)
    

def neighbors(r,c):
    return [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

if __name__ == "__main__":
    sys.exit(main())