import os
import sys
import utils.aoc as aoc

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day21.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    password = list("abcdefgh")
    for line in input:
        info = line.split()

        if info[0] == "swap":
            if info[1] == "position":
                [x,y] = aoc.ints(line)
                tmp = password[x]
                password[x] = password[y]
                password[y] = tmp
            else:
                (x,y) = (info[2], info[5])
                xi = password.index(x)
                yi = password.index(y)
                password[xi] = y
                password[yi] = x
        elif info[0] == "rotate":
            if info[1] == "based":
                x = info[6]
                xi = password.index(x)
                rot = 1 + xi + (1 if xi >= 4 else 0)
                for _ in range(rot):
                    password.insert(0, password.pop())
            else:
                [x] = aoc.ints(line)
                if info[1] == "right":
                    for _ in range(x):
                        password.insert(0, password.pop())
                else:
                    for _ in range(x):
                        password.append(password.pop(0))
        elif info[0] == "move":
            [x,y] = aoc.ints(line)
            password.insert(y, password.pop(x))
        elif info[0] == "reverse":
            [x,y] = aoc.ints(line)
            password = password[:x] + password[x:y+1][::-1] + password[y+1:]

    return "".join(password)



def part2(input):
    password = list("fbgdceah")
    for i in range(len(input)-1, -1, -1):
        line = input[i]
        info = line.split()

        if info[0] == "swap":
            if info[1] == "position":
                [x,y] = aoc.ints(line)
                tmp = password[x]
                password[x] = password[y]
                password[y] = tmp
            else:
                (x,y) = (info[2], info[5])
                xi = password.index(x)
                yi = password.index(y)
                password[xi] = y
                password[yi] = x
        elif info[0] == "rotate":
            if info[1] == "based":
                x = info[6]
                xi = password.index(x)
                if xi == 0:
                    rot = 1
                if xi == 1:
                    rot = 1
                if xi == 2:
                    rot = 6
                if xi == 3:
                    rot = 2
                if xi == 4:
                    rot = 7
                if xi == 5:
                    rot = 3
                if xi == 6:
                    rot = 0
                if xi == 7:
                    rot = 4
                for _ in range(rot):
                    password.append(password.pop(0))

                
            else:
                [x] = aoc.ints(line)
                if info[1] == "right":
                    for _ in range(x):
                        password.append(password.pop(0))
                else:
                    for _ in range(x):
                        password.insert(0, password.pop())
        elif info[0] == "move":
            [x,y] = aoc.ints(line)
            password.insert(x, password.pop(y))
        elif info[0] == "reverse":
            [x,y] = aoc.ints(line)
            password = password[:x] + password[x:y+1][::-1] + password[y+1:]
    
    return "".join(password)

if __name__ == "__main__":
    sys.exit(main())
