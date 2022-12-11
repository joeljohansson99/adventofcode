import math
import sys
from copy import deepcopy

def main():

    input = []
    with open('input/day11.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","").strip()
            if (len(l) != 0):
                input.append(l)
    input = chunks(input, 6)


    monkeys = []
    ops = []
    tests = []
    for act in input:
        [_, items, op, test, t, f] = act
        items = [int(item.replace(",","")) for item in items.split(" ")[2:]]
        op = op.split(" ")[3:]
        test = int(test.split(" ")[3])
        t = int(t.split(" ")[5])
        f = int(f.split(" ")[5])
        monkeys.append(items)
        ops.append(op)
        tests.append([test,t,f])

    print("Part 1: " + str(part1(deepcopy(monkeys), ops, tests)))
    print("Part 2: " + str(part2(deepcopy(monkeys), ops, tests)))

def part1(monkeys, ops, tests):
    count = [0] * len(monkeys)
    for _ in range(0,20):
        for i in range(0, len(monkeys)):
            
            monkey = monkeys[i]
            for j in range(0, len(monkey)):
                count[i] += 1

                op = ops[i]
                if op[1] == '+':
                    monkey[j] = monkey[j] + int(op[2])

                elif op[1] == '*':
                    if op[2].isdigit():
                        monkey[j] = monkey[j] * int(op[2])
                    else:
                        monkey[j] = monkey[j] * monkey[j]
                monkey[j] = math.trunc(monkey[j] / 3)

                test = tests[i]
                if monkey[j] % test[0] == 0:
                    monkeys[test[1]].append(monkey[j])
                else:
                    monkeys[test[2]].append(monkey[j])  

            for _ in range(0, len(monkey)):
                monkeys[i].pop(0)

    count.sort(reverse=True)

    return count[0] * count[1]


def part2(monkeys, ops, tests):
    count = [0] * len(monkeys)
    max = math.prod([test[0] for test in tests])

    for _ in range(0,10000):
        for i in range(0, len(monkeys)):
            
            monkey = monkeys[i]
            for j in range(0, len(monkey)):
                count[i] += 1

                op = ops[i]
                if op[1] == '+':
                    monkey[j] = (monkey[j] + int(op[2])) % max

                elif op[1] == '*':
                    if op[2].isdigit():
                        monkey[j] = (monkey[j] * int(op[2])) % max
                    else:
                        monkey[j] = (monkey[j] * monkey[j]) % max

                test = tests[i]
                if monkey[j] % test[0] == 0:
                    monkeys[test[1]].append(monkey[j])
                else:
                    monkeys[test[2]].append(monkey[j])  

            for _ in range(0, len(monkey)):
                monkeys[i].pop(0)

    count.sort(reverse=True)

    return count[0] * count[1]

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

if __name__ == "__main__":
    sys.exit(main())