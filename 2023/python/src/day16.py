import os
import sys

RIGHT = (0,1)
LEFT = (0,-1)
UP = (-1,0)
DOWN = (1,0)

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day16.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    return do_laser((0,0), RIGHT, input)

def part2(input):
    ret = set()
    for c in range(0,len(input[0])):
        ret.add(do_laser((0,c),DOWN, input))
        ret.add(do_laser((len(input)-1,c),UP,input))
    
    for r in range(0,len(input)):
        ret.add(do_laser((r,0),RIGHT, input))
        ret.add(do_laser((r,len(input[0])-1),LEFT,input))
    
    return max(ret)
    
def do_laser(pos, dir, input):
    lasers = [(pos,dir)]
    energized = set()
    energized.add(pos)
    
    done = dict()
    for r in range(0, len(input)):
        for c in range(0,len(input)):
            done[(r,c)] = set()
    done[pos].add(dir)
    
    while True:
        next_lasers = []
        for (pos,dir) in lasers:
            next = get_dir(input[pos[0]][pos[1]], dir)
            for n in next:
                next_pos = (pos[0]+n[0], pos[1]+n[1])
                if next_pos[0] >= len(input) or next_pos[0] < 0 or next_pos[1] >= len(input[0]) or next_pos[1] < 0:
                    continue
                if n not in done[next_pos]:
                    next_lasers.append((next_pos,n))
                    energized.add(next_pos)
                    done[next_pos].add(n)
        if len(next_lasers) == 0:
            break
        lasers = next_lasers 
    
    return len(energized)

def get_dir(c, dir):
    if c == '.':
        return [dir]
    if c == '-':
        if dir == LEFT or dir == RIGHT:
            return [dir]
        else:
            return [RIGHT,LEFT]
    if c == '|':
        if dir == UP or dir == DOWN:
            return [dir]
        else:
            return [UP,DOWN]
    if c == '/':
        if dir == RIGHT:
            return [UP]
        elif dir == LEFT:
            return [DOWN]
        elif dir == UP:
            return [RIGHT]
        else:
            return [LEFT]
    if c == '\\':
        if dir == RIGHT:
            return [DOWN]
        elif dir == LEFT:
            return [UP]
        elif dir == UP:
            return [LEFT]
        else:
            return [RIGHT]

if __name__ == "__main__":
    sys.exit(main())