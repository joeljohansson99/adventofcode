from heapq import heappush, heappop
import os
import sys

RIGHT = (0,1)
LEFT = (0,-1)
UP = (-1,0)
DOWN = (1,0)

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day17.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    
    queue = [(0, (0,0), (0,0))]
    visited = set()
    
    while queue:
        (heat, u, dir) = heappop(queue)
        
        if (u,dir) in visited:
            continue
        
        if u == (len(input)-1, len(input[0])-1):
            return heat
        
        visited.add((u,dir))
        
        for d in [x for x in [DOWN,RIGHT,UP,LEFT] if x != dir and x != (dir[0]*-1, dir[1]*-1)]:
            v = u
            tmp = heat
            for _ in range(0,3):
                v = add(d,v)
                
                if v[0] >= len(input) or v[0] < 0 or v[1] >= len(input[0]) or v[1] < 0:
                    break
                
                tmp = tmp + int(input[v[0]][v[1]])
                
                heappush(queue, (tmp, v, d))

def part2(input):
    queue = [(0, (0,0), (0,0))]
    visited = set()
    
    while queue:
        (heat, u, dir) = heappop(queue)
        
        if (u,dir) in visited:
            continue
        
        if u == (len(input)-1, len(input[0])-1):
            return heat
        
        visited.add((u,dir))
        
        for d in [x for x in [DOWN,RIGHT,UP,LEFT] if x != dir and x != (dir[0]*-1, dir[1]*-1)]:
            v = u
            tmp = heat
            for i in range(1,11):
                v = add(d,v)
                
                if v[0] >= len(input) or v[0] < 0 or v[1] >= len(input[0]) or v[1] < 0:
                    break
                
                tmp = tmp + int(input[v[0]][v[1]])
                
                if i >= 4:
                    heappush(queue, (tmp, v, d))

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

if __name__ == "__main__":
    sys.exit(main())