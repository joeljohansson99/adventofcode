import z3
import sys
import os
import operator

def main():

    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day21.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))


    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    monkeys = dict()
    for line in input:
        [monkey, yell] = line.split(":")
        yell = yell.strip().split(" ")
        if len(yell) == 1:
            monkeys[monkey] = [int(yell[0])]
        else:
            if yell[1] == "+":
                monkeys[monkey] = (operator.add, yell[0], yell[2])
            elif yell[1] == "-":
                monkeys[monkey] = (operator.sub, yell[0], yell[2])
            elif yell[1] == "*":
                monkeys[monkey] = (operator.mul, yell[0], yell[2])
            elif yell[1] == "/":
                monkeys[monkey] = (operator.truediv, yell[0], yell[2])
    
    return int(dfs("root", monkeys))

def part2(input):
    monkeys = dict()
    for line in input:
        [monkey, yell] = line.split(":")
        yell = yell.strip().split(" ")
        if len(yell) == 1:
            monkeys[monkey] = [int(yell[0])]
        else:
            if yell[1] == "+":
                monkeys[monkey] = (operator.add, yell[0], yell[2])
            elif yell[1] == "-":
                monkeys[monkey] = (operator.sub, yell[0], yell[2])
            elif yell[1] == "*":
                monkeys[monkey] = (operator.mul, yell[0], yell[2])
            elif yell[1] == "/":
                monkeys[monkey] = (operator.truediv, yell[0], yell[2])
    
    (_, left, right) = monkeys["root"]
    rhs = dfs(right, monkeys)

    return binary_search(0, 21120928600114, rhs, left, monkeys)

def binary_search(low, high, rhs, left, monkeys):
    if high >= low:
        mid = (high + low) // 2
        monkeys["humn"] = [mid]
        lhs = dfs(left, monkeys)

        if lhs == rhs:
            return mid
        elif lhs < rhs:
            return binary_search(low, mid - 1, rhs, left, monkeys)
        else:
            return binary_search(mid + 1, high, rhs, left, monkeys)
    else:
        return "ERROR"
    

def dfs(monkey, monkeys):
    if len(monkeys[monkey]) == 1:
        return monkeys[monkey][0]
    else:
        (op, m1, m2) = monkeys[monkey]
        return op(dfs(m1, monkeys), dfs(m2, monkeys))

if __name__ == "__main__":
    sys.exit(main())