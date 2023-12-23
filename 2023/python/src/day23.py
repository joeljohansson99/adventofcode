import os
import sys

RIGHT = (0,1)
LEFT = (0,-1)
UP = (-1,0)
DOWN = (1,0)

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day23.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    start = (0,0)
    for c in range(0, len(input[0])):
        if input[0][c] == '.':
            start = (0,c)
    sys.setrecursionlimit(10000)
    return dfs(start, set(), input) - 1

def dfs(pos, visited, map):
    visited.add(pos)

    if pos[0] == len(map) - 1:
        return len(visited)

    if map[pos[0]][pos[1]] == '>':
        neigh = [(pos[0], pos[1]+1)]
    elif map[pos[0]][pos[1]] == '<':
        neigh = [(pos[0], pos[1]-1)]
    elif map[pos[0]][pos[1]] == '^':
        neigh = [(pos[0]-1, pos[1])]
    elif map[pos[0]][pos[1]] == 'v':
        neigh = [(pos[0]+1, pos[1])]
    else:
        neigh = [(pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1)]

    ret = [0]
    for n in neigh:
        if n not in visited and map[n[0]][n[1]] != '#':
            visited.add(n)
            ret.append(dfs(n, set(visited), map))
            visited.remove(n)
    
    return max(ret)


def part2(input):
    input = [list(x) for x in input]
    start = (0,0)
    for c in range(0, len(input[0])):
        if input[0][c] == '.':
            start = (0,c)
        if input[len(input)-1][c] == '.':
            end = (len(input)-1, c)
    
    vertices = set()
    for r in range(1, len(input)-1):
        for c in range(1,len(input[0])-1):
            if input[r][c] == '.':
                count = 0
                neigh = [(r+1, c),(r-1, c), (r, c+1),(r, c-1)]
                for n in neigh:
                    if input[n[0]][n[1]] in ['>','<', '^', 'v']:
                        count += 1
                if count > 1:
                    vertices.add((r,c))


    vertices.add(start)
    vertices.add(end)

    graph = dict()
    for v in vertices:
        graph[v] = bfs(v, input, vertices)

    return dfs2(start, end, graph, set(), 0)

def bfs(start, map, vertices):
    visited = set()
    visited.add(start)
    curr = set()
    curr.add(start)
    ret = []
    steps = 1
    while curr:
        next = set()
        for c in curr:
            neigh = [(c[0]+1, c[1]), (c[0]-1, c[1]), (c[0], c[1]+1), (c[0], c[1]-1)]
            for n in neigh:
                if n[0] > len(map)-1 or n[0] < 0 or n in visited:
                    continue
                if n in vertices:
                    ret.append((steps, n))
                elif map[n[0]][n[1]] != '#':
                    visited.add(n)
                    next.add(n)
        curr = next
        steps+=1
    
    return ret

def dfs2(node, end, graph, visited, steps):
    visited.add(node)
    if node == end:
        return steps

    ret = [0]
    for edges in graph[node]:
        (dist, next) = edges
        if next in visited:
            continue
        ret.append(dfs2(next, end, graph, set(visited), steps + dist))

    return max(ret)

if __name__ == "__main__":
    sys.exit(main())


#   