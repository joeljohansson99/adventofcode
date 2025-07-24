import os
import sys
import re
from itertools import permutations


def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day7.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    output = 0

    for setting in permutations(range(5)):
        mem = list()
        pcs = list()
        queue = list()
        done = list()
        for i in range(5):
            mem.append(list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', input[0]))))
            pcs.append(0)
            queue.append(list())
            done.append(False)
            queue[i].append(setting[i])

        while not all(done):
            for i in range(5):
                inst = str(mem[i][pcs[i]]).zfill(5)
                opcode = int(inst[-2:])

                if opcode == 99:
                    done[i] = True
                    continue

                if opcode == 1:
                    val1 = mem[i][mem[i][pcs[i]+1]] if int(inst[-3]) == 0 else mem[i][pcs[i]+1]
                    val2 = mem[i][mem[i][pcs[i]+2]] if int(inst[-4]) == 0 else mem[i][pcs[i]+2]
                    mem[i][mem[i][pcs[i]+3]] = val1 + val2
                    pcs[i] += 4
                elif opcode == 2:
                    val1 = mem[i][mem[i][pcs[i]+1]] if int(inst[-3]) == 0 else mem[i][pcs[i]+1]
                    val2 = mem[i][mem[i][pcs[i]+2]] if int(inst[-4]) == 0 else mem[i][pcs[i]+2]
                    mem[i][mem[i][pcs[i]+3]] = val1 * val2
                    pcs[i] += 4
                elif opcode == 3:
                    if queue[i]:
                        mem[i][mem[i][pcs[i]+1]] = queue[i].pop(0)
                        pcs[i] += 2
                    elif i == 0:
                        mem[i][mem[i][pcs[i]+1]] = 0
                        pcs[i] += 2
                elif opcode == 4:
                    val1 = mem[i][mem[i][pcs[i]+1]] if int(inst[-3]) == 0 else mem[i][pcs[i]+1]
                    if i == 4:
                        output = max(output,val1)
                    else:
                        queue[i+1].append(val1)
                    pcs[i] += 2
                elif opcode == 5:
                    val1 = mem[i][mem[i][pcs[i]+1]] if int(inst[-3]) == 0 else mem[i][pcs[i]+1]
                    val2 = mem[i][mem[i][pcs[i]+2]] if int(inst[-4]) == 0 else mem[i][pcs[i]+2]
                    if val1 != 0:
                        pcs[i] = val2
                    else:
                        pcs[i] += 3
                elif opcode == 6:
                    val1 = mem[i][mem[i][pcs[i]+1]] if int(inst[-3]) == 0 else mem[i][pcs[i]+1]
                    val2 = mem[i][mem[i][pcs[i]+2]] if int(inst[-4]) == 0 else mem[i][pcs[i]+2]
                    if val1 == 0:
                        pcs[i] = val2
                    else:
                        pcs[i] += 3
                elif opcode == 7:
                    val1 = mem[i][mem[i][pcs[i]+1]] if int(inst[-3]) == 0 else mem[i][pcs[i]+1]
                    val2 = mem[i][mem[i][pcs[i]+2]] if int(inst[-4]) == 0 else mem[i][pcs[i]+2]
                    mem[i][mem[i][pcs[i]+3]] = 1 if val1 < val2 else 0 
                    pcs[i] += 4
                elif opcode == 8:
                    val1 = mem[i][mem[i][pcs[i]+1]] if int(inst[-3]) == 0 else mem[i][pcs[i]+1]
                    val2 = mem[i][mem[i][pcs[i]+2]] if int(inst[-4]) == 0 else mem[i][pcs[i]+2]
                    mem[i][mem[i][pcs[i]+3]] = 1 if val1 == val2 else 0 
                    pcs[i] += 4
    return output

def part2(input):
    output = 0
    
    for setting in permutations(range(5,10)):
        mem = list()
        pcs = list()
        queue = list()
        done = list()
        for i in range(5):
            mem.append(list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', input[0]))))
            pcs.append(0)
            queue.append(list())
            done.append(False)
            queue[i].append(setting[i])
        
        first = True

        while not all(done):
            for i in range(5):
                inst = str(mem[i][pcs[i]]).zfill(5)
                opcode = int(inst[-2:])

                if opcode == 99:
                    done[i] = True
                    continue

                if opcode == 1:
                    val1 = mem[i][mem[i][pcs[i]+1]] if int(inst[-3]) == 0 else mem[i][pcs[i]+1]
                    val2 = mem[i][mem[i][pcs[i]+2]] if int(inst[-4]) == 0 else mem[i][pcs[i]+2]
                    mem[i][mem[i][pcs[i]+3]] = val1 + val2
                    pcs[i] += 4
                elif opcode == 2:
                    val1 = mem[i][mem[i][pcs[i]+1]] if int(inst[-3]) == 0 else mem[i][pcs[i]+1]
                    val2 = mem[i][mem[i][pcs[i]+2]] if int(inst[-4]) == 0 else mem[i][pcs[i]+2]
                    mem[i][mem[i][pcs[i]+3]] = val1 * val2
                    pcs[i] += 4
                elif opcode == 3:
                    if queue[i]:
                        mem[i][mem[i][pcs[i]+1]] = queue[i].pop(0)
                        pcs[i] += 2
                    elif i == 0 and first:
                        mem[i][mem[i][pcs[i]+1]] = 0
                        pcs[i] += 2
                        first = False
                elif opcode == 4:
                    val1 = mem[i][mem[i][pcs[i]+1]] if int(inst[-3]) == 0 else mem[i][pcs[i]+1]
                    if i == 4:
                        output = max(output,val1)
                    queue[(i+1)%5].append(val1)
                    pcs[i] += 2
                elif opcode == 5:
                    val1 = mem[i][mem[i][pcs[i]+1]] if int(inst[-3]) == 0 else mem[i][pcs[i]+1]
                    val2 = mem[i][mem[i][pcs[i]+2]] if int(inst[-4]) == 0 else mem[i][pcs[i]+2]
                    if val1 != 0:
                        pcs[i] = val2
                    else:
                        pcs[i] += 3
                elif opcode == 6:
                    val1 = mem[i][mem[i][pcs[i]+1]] if int(inst[-3]) == 0 else mem[i][pcs[i]+1]
                    val2 = mem[i][mem[i][pcs[i]+2]] if int(inst[-4]) == 0 else mem[i][pcs[i]+2]
                    if val1 == 0:
                        pcs[i] = val2
                    else:
                        pcs[i] += 3
                elif opcode == 7:
                    val1 = mem[i][mem[i][pcs[i]+1]] if int(inst[-3]) == 0 else mem[i][pcs[i]+1]
                    val2 = mem[i][mem[i][pcs[i]+2]] if int(inst[-4]) == 0 else mem[i][pcs[i]+2]
                    mem[i][mem[i][pcs[i]+3]] = 1 if val1 < val2 else 0 
                    pcs[i] += 4
                elif opcode == 8:
                    val1 = mem[i][mem[i][pcs[i]+1]] if int(inst[-3]) == 0 else mem[i][pcs[i]+1]
                    val2 = mem[i][mem[i][pcs[i]+2]] if int(inst[-4]) == 0 else mem[i][pcs[i]+2]
                    mem[i][mem[i][pcs[i]+3]] = 1 if val1 == val2 else 0 
                    pcs[i] += 4
    return output

if __name__ == "__main__":
    sys.exit(main())