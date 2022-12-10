import sys


def main():

    input = []
    with open('input/day10.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    clock = 0
    value = 1
    signal = []
    for instr in input:
        if instr == "noop":
            clock+=1
            if clock % 40 == 20:
                signal.append(clock*value)
        else:
            (_, val) = instr.split(" ")
            for i in range(0, 2):
                clock += 1
                if clock % 40 == 20:
                    signal.append(clock*value)
            value += int(val)
        if clock > 220:
            break
    print(signal)
    return sum(signal)

def part2(input):
    clock = 0
    value = 1
    CRT = []
    for instr in input:
        if instr == "noop":
            if abs((clock%40) - value) < 2:
                CRT.append("#")
            else:
                CRT.append(" ")
                
            clock+=1
            if clock == 220:
                break

        else:
            (_, val) = instr.split(" ")
            for i in range(0, 2):
                if abs((clock%40) - value) < 2:
                    CRT.append("#")
                else:
                    CRT.append(" ")

                clock+=1
                if clock == 220:
                    break
            
            value += int(val)

    ret = ["\n"]
    for c in chunks(CRT, 40):
        ret.append("".join(c))
    ret = "\n".join(ret)
    return ret

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


if __name__ == "__main__":
    sys.exit(main())