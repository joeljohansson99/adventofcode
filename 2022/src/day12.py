import sys
from copy import deepcopy


def main():

    input = []
    with open('input/day12.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append([c for c in l])
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    start = (0,0)
    for r in range(0,len(input)):
        for c in range(0,len(input[0])):
            if input[r][c] == 'S':
                start = (r,c)
                input[r][c] = 'a'
    visited = [start]
    currents = [start]
    count = 0
    tmp = deepcopy(input)

    while len(currents) != 0:
        count += 1
        next = []
        for (row,col) in currents:
            neighbours = [(r,c) for (r,c) in [(row-1, col), (row, col-1), (row, col+1), (row+1, col)] if r >= 0 and r < len(input) and c >= 0 and c < len(input[0]) and (r,c) not in visited]
            for (r,c) in neighbours:
                if input[r][c] == 'E':
                    if input[row][col] == 'z' or input[row][col] == 'y':
                        return count
                else:
                    h = ord(input[r][c]) - ord(input[row][col])
                    if h <= 1: 
                        tmp[r][c] = '.'
                        visited.append((r,c))
                        next.append((r,c))
        
        currents = next
    return count

def part2(input):
    for r in range(0,len(input)):
        for c in range(0,len(input[0])):
            if input[r][c] == 'S':
                input[r][c] = 'a'
    
    start = (0,0)
    for r in range(0,len(input)):
        for c in range(0,len(input[0])):
            if input[r][c] == 'E':
                input[r][c] = 'z'
                start = (r,c)

    visited = [start]
    currents = [start]
    count = 0
    tmp = deepcopy(input)

    while len(currents) != 0:
        count += 1
        next = []
        for (row,col) in currents:
            neighbours = [(r,c) for (r,c) in [(row-1, col), (row, col-1), (row, col+1), (row+1, col)] if r >= 0 and r < len(input) and c >= 0 and c < len(input[0]) and (r,c) not in visited]
            for (r,c) in neighbours:
                
                h = ord(input[row][col]) - ord(input[r][c])
                if h <= 1: 
                    if input[r][c] == 'a':
                        return count
                    tmp[r][c] = '.'
                    visited.append((r,c))
                    next.append((r,c))

        currents = next
    return count

if __name__ == "__main__":
    sys.exit(main())