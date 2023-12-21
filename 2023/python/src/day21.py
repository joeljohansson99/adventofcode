import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day21.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    start = (0,0)
    for r in range(0, len(input)):
        for c in range(0, len(input[0])):
            if input[r][c] == 'S':
                start = (r,c)
                break
    
    return bfs(input, start, 64, 0)

    
def part2(input):
    start = (0,0)
    for r in range(0, len(input)):
        for c in range(0, len(input[0])):
            if input[r][c] == 'S':
                start = (r,c)
    
    w = len(input)
    middle = (w//2)
    
    steps = 26501365
    reach = (steps-middle) // w

    even = bfs(input, start, 2*w, 0)
    
    odd = bfs(input, start, 2*w, 1)
    
    bottom_left_64 = bfs(input, (w-1,0), 64, 0)
    bottom_right_64 = bfs(input, (w-1,w-1), 64, 0)
    upper_left_64 = bfs(input, (0,0), 64, 0)
    upper_right_64 = bfs(input, (0,w-1), 64, 0)
    
    bottom_left_195 = bfs(input, (w-1,0), 195, 1)
    bottom_right_195 = bfs(input, (w-1,w-1), 195, 1)
    upper_left_195 = bfs(input, (0,0), 195, 1)
    upper_right_195 = bfs(input, (0,w-1), 195, 1)
    
    middle_left = bfs(input, (middle, w-1), 130, 0)
    middle_right = bfs(input, (middle, 0), 130, 0)
    middle_down = bfs(input, (0, middle), 130, 0)
    middle_up = bfs(input, (w-1, middle), 130, 0)

    ret = odd
    
    for i in range(1,reach):
        if i % 2 == 0:
            ret += 4*i*odd
        else: 
            ret += 4*i*even
    
    ret += middle_down + middle_left + middle_up + middle_right
    
    left195 = reach*4 - 4
    left64 = left195+4
    
    for i in range(0, int(left195//4)):
        ret += bottom_left_195 + bottom_right_195 + upper_left_195 + upper_right_195
    
    for i in range(0, int(left64//4)):
        ret += bottom_left_64 + bottom_right_64 + upper_left_64 + upper_right_64
    
    return ret
    
def bfs(map, start, steps, m):
    current = set()
    visited = set()
    
    current.add(start)
    visited.add(start)
    
    count = (1 + m)%2
    i = 0
    while current and i < steps:
        next = set()
        for (r,c) in current:
            neigh = [(r+1, c),(r-1, c), (r, c+1),(r, c-1)]
            for n in neigh:
                if n not in visited and n[0] >= 0 and n[0] < len(map) and n[1] >= 0 and n[1] < len(map[0]) and map[n[0]][n[1]] != "#":
                    if (i+1) % 2 == m:
                        count += 1
                    next.add(n)
                    visited.add(n)
        i += 1
        current = next
    return count

if __name__ == "__main__":
    sys.exit(main())