from collections import defaultdict
import os
from queue import LifoQueue, Queue
import sys
import threading

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day18.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    regs = defaultdict(int)
    sound = 0
    pc = 0
    while True:
        [op, * params] = input[pc].split(" ")
        if op == "snd":
            [x] = params
            sound = regs[x]
        elif op == "set":
            [x,y] = params
            regs[x] = int(y) if check_int(y) else regs[y]
        elif op == "add":
            [x,y] = params
            regs[x] += int(y) if check_int(y) else regs[y]
        elif op == "mul":
            [x,y] = params
            regs[x] *= int(y) if check_int(y) else regs[y]
        elif op == "mod":
            [x,y] = params
            regs[x] %= (int(y) if check_int(y) else regs[y])
        elif op == "rcv":
            [x] = params
            if regs[x] != 0:
                return sound
        elif op == "jgz":
            [x,y] = params
            if regs[x] > 0:
                pc += int(y) if check_int(y) else regs[y]
                continue
        pc += 1

def part2(input):
    Q = [Queue(), Queue()]
    regs = (defaultdict(int), defaultdict(int))
    signal = threading.Event()
    pc = [0,0]
    count = [0,0]
    done = [False,False]
    instructions = []
    for line in input:
        instructions.append(line.split(" "))
    def run(id):
        regs[id]["p"] = id
        while 0 <= pc[id] < len(instructions):
            [op, * params] = instructions[pc[id]]
            if op == "snd":
                [x] = params
                count[id] += 1
                Q[(id+1)%2].put(regs[id][x])
                signal.set()
            elif op == "set":
                [x,y] = params
                regs[id][x] = int(y) if check_int(y) else regs[id][y]
            elif op == "add":
                [x,y] = params
                regs[id][x] += int(y) if check_int(y) else regs[id][y]
            elif op == "mul":
                [x,y] = params
                regs[id][x] *= int(y) if check_int(y) else regs[id][y]
            elif op == "mod":
                [x,y] = params
                regs[id][x] %= (int(y) if check_int(y) else regs[id][y])
            elif op == "rcv":
                [x] = params
                while Q[id].empty():
                    if Q[(id+1)%2].empty() or done[(id+1)%2]:
                        done[id] = True
                        signal.set()
                        return
                    signal.clear()
                    signal.wait(timeout=100)
                regs[id][x] = Q[id].get()
            elif op == "jgz":
                [x,y] = params
                if int(x) if check_int(x) else regs[id][x] > 0:
                    pc[id] += int(y) if check_int(y) else regs[id][y]
                    continue
            else:
                print("ERROR", op)
            pc[id] += 1

    t1 = threading.Thread(target=run, args=(0,))
    t2 = threading.Thread(target=run, args=(1,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    return count[1]

def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

if __name__ == "__main__":
    sys.exit(main())