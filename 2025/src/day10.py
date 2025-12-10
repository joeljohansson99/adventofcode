import os
import sys
import utils.aoc as aoc
import z3

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day10.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    configs = list()
    for line in input:
        indicator = set()
        buttons = list()
        info = line.split(" ")
        for i in range(len(info)):
            if info[i][0] == "[":
                lights = info[i][1:-1]
                for k in range(len(lights)):
                    if lights[k] == "#":
                        indicator.add(k)
            elif info[i][0] == "(":
                buttons.append(aoc.ints(info[i]))
        configs.append((indicator,buttons))

    sum = 0
    i = 0
    for (indicator, buttons) in configs:
        sum += getPresses(indicator,buttons)
        i+=1
    return sum

def part2(input):    
    configs = list()
    for line in input:
        jolts = list()
        buttons = list()
        info = line.split(" ")
        for i in range(len(info)):
            if info[i][0] == "{":
                jolts = aoc.ints(info[i])
            elif info[i][0] == "(":
                buttons.append(aoc.ints(info[i]))
        configs.append((jolts,buttons))

    sum = 0
    i = 0
    for (jolts, buttons) in configs:
        sum += getPresses2(jolts,buttons)
        i+=1
    return sum

def getPresses2(indicator, buttons):
    solver = z3.Optimize()
    xs = []

    ys = []
    for i in range(len(indicator)):
        y = z3.Int(f'y_{i}')
        solver.add(y == indicator[i])
        ys.append(y)

    sums = [[] for _ in range(len(ys))]
    xs = []
    for i in range(len(buttons)):
        x = z3.Int(f'x_{i}')
        for b in buttons[i]:
            sums[b].append(x)
        solver.add(x >= 0)
        xs.append(x)
    for i in range(len(sums)):
        solver.add(ys[i] == z3.Sum([x for x in sums[i]]))
    x_sum = z3.Sum(xs)
    solver.minimize(x_sum)
    solver.check()
    m = solver.model()
    min = 0
    for x in xs:
        min += int(m[x].as_long())
    return min

def getPresses(indicator, buttons):
    Q = list()
    Q.append((list(),0))
    seen = set()
    while Q:
        (lights, presses) = Q.pop(0)
        for button in buttons:
            next_lights = lights.copy()
            for b in button:
                if b in next_lights:
                    next_lights.remove(b)
                else:
                    next_lights.append(b)
            if tuple(next_lights) in seen:
                continue
            else:
                seen.add(tuple(next_lights))
            if set(next_lights) == indicator:
                return presses + 1
            Q.append((next_lights, presses+1))
            Q = sorted(Q, key=lambda x: x[1])
    return "error"

if __name__ == "__main__":
    sys.exit(main())