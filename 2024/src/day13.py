import os
import sys
import re
import z3

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day13.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    games = []
    for i in range(len(input)):
        if "Button A" in input[i]:
            [adx, ady] = list(map(int, re.findall(r'\d+', input[i])))
            [bdx, bdy] = list(map(int, re.findall(r'\d+', input[i+1])))
            [px, py] = list(map(int, re.findall(r'\d+', input[i+2])))
            games.append((adx,ady,bdx,bdy,px,py))
        

    sum = 0
    for game in games:
        ac, bc, coins = z3.Ints('ac bc coins')
        solver = z3.Optimize()

        (adx,ady,bdx,bdy,px,py) = game
        solver.add(adx*ac + bdx*bc == px)
        solver.add(ady*ac + bdy*bc == py)
        solver.add(coins == ac*3+bc)
        solver.minimize(coins)

        if solver.check() == z3.sat:
            sol = solver.model()
            sum += sol[coins].as_long()

    return sum
    


def part2(input):
    games = []
    for i in range(len(input)):
        if "Button A" in input[i]:
            [adx, ady] = list(map(int, re.findall(r'\d+', input[i])))
            [bdx, bdy] = list(map(int, re.findall(r'\d+', input[i+1])))
            [px, py] = list(map(int, re.findall(r'\d+', input[i+2])))
            games.append((adx,ady,bdx,bdy,px,py))
        

    sum = 0
    for game in games:
        ac, bc, coins = z3.Ints('ac bc coins')
        solver = z3.Optimize()

        (adx,ady,bdx,bdy,px,py) = game

        px = 10000000000000 + px
        py = 10000000000000 + py

        solver.add(adx*ac + bdx*bc == px)
        solver.add(ady*ac + bdy*bc == py)
        solver.add(coins == ac*3+bc)
        solver.minimize(coins)

        if solver.check() == z3.sat:
            sol = solver.model()
            sum += sol[coins].as_long()

    return sum

if __name__ == "__main__":
    sys.exit(main())