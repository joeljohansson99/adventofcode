import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day19.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    for c in range(len(input[0])):
        if input[0][c] != " ":
            loc = (0,c)
    dir = (1,0)
    seq = ""
    (r,c) = loc
    while True:
        while True:
            (nr,nc) = (r+dir[0], c+dir[1])
            if input[nr][nc] == " ":
                break
            elif input[nr][nc] not in ["-","|","+"]:
                seq += input[nr][nc]
            (r,c) = (nr,nc)

        for (dr,dc) in [left(dir), right(dir)]:
            if input[r+dr][c+dc] != " ":
                dir = (dr,dc)
                break
        else:
            break
        
        loc = (r,c)

    return seq
        
def part2(input):
    for c in range(len(input[0])):
        if input[0][c] != " ":
            loc = (0,c)
    dir = (1,0)
    (r,c) = loc
    steps = 1
    while True:
        while True:
            (nr,nc) = (r+dir[0], c+dir[1])
            if input[nr][nc] == " ":
                break
            (r,c) = (nr,nc)
            steps += 1

        for (dr,dc) in [left(dir), right(dir)]:
            if input[r+dr][c+dc] != " ":
                dir = (dr,dc)
                break
        else:
            break
        
        loc = (r,c)

    return steps

def left(dir):
    return {
        (1,0):(0,1),
        (-1,0):(0,-1),
        (0,1):(1,0),
        (0,-1):(-1,0),
    }[dir]

def right(dir):
    return {
        (1,0):(0,-1),
        (-1,0):(0,1),
        (0,1):(-1,0),
        (0,-1):(1,0),
    }[dir]
                


if __name__ == "__main__":
    sys.exit(main())