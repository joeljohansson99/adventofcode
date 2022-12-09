import sys


def main():

    input = []
    with open('input/day9.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            
            input.append(l)
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    x = [0,0]
    y = [0,0]
    posses = set()
    posses.add((0,0))
    for instr in input:
        (dir, steps) = instr.split(" ")
        steps = int(steps)
        for _ in range(0, steps):
            if dir == "U":
                y[0] -= 1
            if dir == "D":
                y[0] += 1
            if dir == "L":
                x[0] -= 1
            if dir == "R":
                x[0] += 1
            if abs(x[1] - x[0]) == 2:
                if x[1] < x[0]:
                    x[1] += 1
                elif x[1] > x[0]:
                    x[1] -= 1

                if y[1] < y[0]:
                    y[1] += 1
                elif y[1] > y[0]:
                    y[1] -= 1
            
            if abs(y[1] - y[0]) == 2:
                if x[1] < x[0]:
                    x[1] += 1
                elif x[1] > x[0]:
                    x[1] -= 1

                if y[1] < y[0]:
                    y[1] += 1
                elif y[1] > y[0]:
                    y[1] -= 1

            posses.add((y[1], x[1]))

    return len(posses)

def part2(input):
    x = [0] * 10
    y = [0] * 10
    posses = set()
    posses.add((0,0))
    for instr in input:
        (dir, steps) = instr.split(" ")
        steps = int(steps)
        for _ in range(0, steps):
            if dir == "U":
                y[0] -= 1
            if dir == "D":
                y[0] += 1
            if dir == "L":
                x[0] -= 1
            if dir == "R":
                x[0] += 1
            
            for i in range(1, 10):
                if abs(x[i] - x[i-1]) == 2:
                    if x[i] < x[i-1]:
                        x[i] += 1
                    elif x[i] > x[i-1]:
                        x[i] -= 1

                    if y[i] < y[i-1]:
                        y[i] += 1
                    elif y[i] > y[i-1]:
                        y[i] -= 1
                
                if abs(y[i] - y[i-1]) == 2:
                    if y[i] < y[i-1]:
                        y[i] += 1
                    elif y[i] > y[i-1]: 
                        y[i] -= 1
                    
                    if x[i] < x[i-1]:
                        x[i] += 1
                    elif x[i] > x[i-1]:
                        x[i] -= 1

                if i == 9:
                    posses.add((y[i], x[i]))

    return len(posses)

if __name__ == "__main__":
    sys.exit(main())