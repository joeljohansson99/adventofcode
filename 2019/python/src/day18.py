import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day18.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    walls = set()
    keys = dict()
    doors = dict()
    paths = dict()

    for r in range(len(input)):
        for c in range(len(input[r])):
            if input[r][c] == "#":
                walls.add((r,c))
            elif input[r][c] == "@":
                pos = (r,c)
            elif input[r][c].isalpha():
                if input[r][c].islower():
                    keys[(r,c)] = input[r][c]
                else:
                    doors[(r,c)] = input[r][c]

    paths["@"] = dict()
    for (n, key) in keys.items():
        paths["@"][key] = getPath(pos, n, walls, doors)
            
    for (n, key) in keys.items():
        paths[key] = dict()
        for (dn, dkey) in keys.items():
            if key == dkey:
                continue
            paths[key][dkey] = getPath(n, dn, walls, doors)

    return search("@", paths, [])

def part2(input):
    fixed = [list(input[r]) for r in range(len(input))]
    done = False
    for r in range(len(fixed)):
        for c in range(len(fixed[r])):
            if fixed[r][c] == "@":
                fixed[r][c] = "#"
                for (dr,dc) in neighbours(r,c):
                    fixed[dr][dc] = "#"
                for (dr,dc) in diag_neighbours(r,c):
                    fixed[dr][dc] = "@"
                done = True 
                break
        if done:
            break
        
    walls = set()
    keys = dict()
    doors = dict()
    paths = dict()
    posses = list()

    for r in range(len(fixed)):
        for c in range(len(fixed[r])):
            if fixed[r][c] == "#":
                walls.add((r,c))
            elif fixed[r][c] == "@":
                posses.append((r,c))
            elif fixed[r][c].isalpha():
                if fixed[r][c].islower():
                    keys[(r,c)] = fixed[r][c]
                else:
                    doors[(r,c)] = fixed[r][c]
    
    for i in range(len(posses)):
        paths[str(i)] = dict()
        for (n, key) in keys.items():
            path = getPath(posses[i], n, walls, doors)
            if path is not None:
                paths[str(i)][key] = path
    
    for (n, key) in keys.items():
        paths[key] = dict()
        for (dn, dkey) in keys.items():
            if key == dkey:
                continue
            path = getPath(n, dn, walls, doors)
            if path is not None:
                paths[key][dkey] = path

    return search2(["0","1","2","3"], paths, [])

cache = dict()
def search(node, paths, unlocked):
    keys = [key for (key, (_, doors)) in paths[node].items() if all([door in unlocked for door in doors]) and key not in unlocked]
    
    state = (node, tuple(sorted(unlocked)))
    if state in cache and cache[state]:
        return cache[state]

    if len(keys) == 0:
        return 0
    
    vals = []
    for key in keys:
        unlocked.append(key)
        vals.append(paths[node][key][0] + search(key, paths, unlocked))
        unlocked.remove(key)
    cache[state] = min(vals)
    return cache[state]

cache2 = dict()
def search2(nodes, paths, unlocked):
    keys = list()
    for node in nodes:
        for (key, (_, doors)) in paths[node].items():
            if key not in unlocked and all([door in unlocked for door in doors]):
                keys.append((node, key))

    state = (tuple(sorted(nodes)), tuple(sorted(unlocked)))
    if state in cache and cache[state]:
        return cache[state]

    if len(keys) == 0:
        return 0
    
    vals = []
    for (node, key) in keys:
        unlocked.append(key)
        nodes.append(key)
        nodes.remove(node)
        vals.append(paths[node][key][0] + search2(nodes, paths, unlocked))
        unlocked.remove(key)
        nodes.remove(key)
        nodes.append(node)
    cache[state] = min(vals)
    return cache[state]

def getPath(start, end, walls, doors):
    current = [start]
    prevs = dict()
    steps = 0
    seen = set()
    seen.add(start)
    done = False
    while not done:
        steps += 1
        next = list()
        for (r,c) in current:
            for n in neighbours(r,c):
                if n not in walls and n not in seen:
                    prevs[n] = (r,c)
                    if n == end:
                        done = True
                        break
                    next.append(n)
                    seen.add(n)
        current = next
        if not current and not done:
            return None

    blocked = []
    pos = end
    while pos != start:
        pos = prevs[pos]
        if pos in doors:
            blocked.append(doors[pos].lower())
    
    return (steps, blocked)

def neighbours(r,c):
    return [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

def diag_neighbours(r,c):
    return [(r+1,c+1),(r-1,c-1),(r+1,c-1),(r-1,c+1)]


if __name__ == "__main__":
    sys.exit(main())