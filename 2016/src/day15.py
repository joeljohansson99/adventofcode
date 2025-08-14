import os
import sys
import z3
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day15.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    t = z3.Int('t')
    solver = z3.Optimize()
    solver.add(t >= 0)
    for i in range(len(input)):
        [_, mod, _, pos] = aoc.ints(input[i])
        solver.add(((t+i+1)+pos) % mod == 0)
    
    solver.check()
    sol = solver.model()
    return sol[t]

def part2(input):
    t = z3.Int('t')
    solver = z3.Optimize()
    solver.add(t >= 0)
    for i in range(len(input)):
        [_, mod, _, pos] = aoc.ints(input[i])
        solver.add(((t+i+1)+pos) % mod == 0)
    solver.add((t+i+2) % 11 == 0)
    solver.check()
    sol = solver.model()
    return sol[t]


if __name__ == "__main__":
    sys.exit(main())
