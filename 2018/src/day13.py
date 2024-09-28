import os
import sys
import time

def main():
    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day13.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

def part1(input):
    rails = [list(line) for line in input]
    pos = list()
    vel = dict()
    carts = 0
    for y in range(0, len(rails)):
        for x in range(0, len(rails[0])):
            if rails[y][x] == '^':
                rails[y][x] = '|'
                pos.append((x,y))
                vel[carts] = UP
                carts+=1
            if rails[y][x] == 'v':
                rails[y][x] = '|'
                pos.append((x,y))
                vel[carts] = DOWN
                carts+=1
            if rails[y][x] == '<':
                rails[y][x] = '-'
                pos.append((x,y))
                vel[carts] = LEFT
                carts+=1
            if rails[y][x] == '>':
                rails[y][x] = '-'
                pos.append((x,y))
                vel[carts] = RIGHT
                carts+=1
    
    turns = dict()
    intersect = [LEFT, None, RIGHT]
    for cart in range(0, carts):
        turns[cart] = 0

    order = [cart for cart in range(0,carts)]
    
    while True:
        order.sort(key=lambda x: pos[x])
        for cart in order:
            p = pos[cart]
            v = vel[cart]
            if rails[p[1]][p[0]] == '/':
                if v == LEFT:
                    v = DOWN
                elif v == RIGHT:
                    v = UP
                elif v == UP:
                    v = RIGHT
                elif v == DOWN:
                    v = LEFT
            elif rails[p[1]][p[0]] == '\\':
                if v == LEFT:
                    v = UP
                elif v == RIGHT:
                    v = DOWN
                elif v == UP:
                    v = LEFT
                elif v == DOWN:
                    v = RIGHT
            elif rails[p[1]][p[0]] == '+':
                turn = turns[cart]
                turn = turn % 3
                dir = intersect[turn]
                if dir is LEFT:
                    if v == LEFT:
                        v = DOWN
                    elif v == RIGHT:
                        v = UP
                    elif v == UP:
                        v = LEFT
                    elif v == DOWN:
                        v = RIGHT
                if dir is RIGHT:
                    if v == LEFT:
                        v = UP
                    elif v == RIGHT:
                        v = DOWN
                    elif v == UP:
                        v = RIGHT
                    elif v == DOWN:
                        v = LEFT
                turns[cart] = turn + 1

            p = tuple(map(sum, zip(p, v)))
            
            if p in pos:
                return f'{p[0]},{p[1]}'
            
            pos[cart] = p
            vel[cart] = v

def part2(input):
    rails = [list(line) for line in input]
    pos = list()
    vel = dict()
    carts = 0
    for y in range(0, len(rails)):
        for x in range(0, len(rails[0])):
            if rails[y][x] == '^':
                rails[y][x] = '|'
                pos.append((x,y))
                vel[carts] = UP
                carts+=1
            if rails[y][x] == 'v':
                rails[y][x] = '|'
                pos.append((x,y))
                vel[carts] = DOWN
                carts+=1
            if rails[y][x] == '<':
                rails[y][x] = '-'
                pos.append((x,y))
                vel[carts] = LEFT
                carts+=1
            if rails[y][x] == '>':
                rails[y][x] = '-'
                pos.append((x,y))
                vel[carts] = RIGHT
                carts+=1
    
    turns = dict()
    intersect = [LEFT, None, RIGHT]
    for cart in range(0, carts):
        turns[cart] = 0

    order = [cart for cart in range(0,carts)]
    crashed = set()

    while carts - len(crashed) != 1:
        order.sort(key=lambda x: pos[x])
        for cart in order:
            if cart in crashed:
                continue
            p = pos[cart]
            v = vel[cart]
            if rails[p[1]][p[0]] == '/':
                if v == LEFT:
                    v = DOWN
                elif v == RIGHT:
                    v = UP
                elif v == UP:
                    v = RIGHT
                elif v == DOWN:
                    v = LEFT
            elif rails[p[1]][p[0]] == '\\':
                if v == LEFT:
                    v = UP
                elif v == RIGHT:
                    v = DOWN
                elif v == UP:
                    v = LEFT
                elif v == DOWN:
                    v = RIGHT
            elif rails[p[1]][p[0]] == '+':
                turn = turns[cart]
                turn = turn % 3
                dir = intersect[turn]
                if dir is LEFT:
                    if v == LEFT:
                        v = DOWN
                    elif v == RIGHT:
                        v = UP
                    elif v == UP:
                        v = LEFT
                    elif v == DOWN:
                        v = RIGHT
                if dir is RIGHT:
                    if v == LEFT:
                        v = UP
                    elif v == RIGHT:
                        v = DOWN
                    elif v == UP:
                        v = RIGHT
                    elif v == DOWN:
                        v = LEFT
                turns[cart] = turn + 1

            p = tuple(map(sum, zip(p, v)))
            
            if p in pos:
                crashed.add(cart)
                crashed.add(pos.index(p))
                pos[cart] = (-1,-1)
                pos[pos.index(p)] = (-1,-1)
            else:
                pos[cart] = p
                vel[cart] = v

    for cart in range(0, carts):
        if cart not in crashed:
            return f'{pos[cart][0]},{pos[cart][1]}'

if __name__ == "__main__":
    sys.exit(main())