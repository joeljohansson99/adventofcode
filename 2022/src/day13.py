import enum
import sys
from copy import deepcopy

class CHECK(enum.Enum):
    TRUE = 1
    FALSE = 2
    EQUAL = 3

def main():
    input = []
    pair = []
    with open('input/day13.txt') as f:
        pair = []
        for line in f.readlines():
            l = line.replace("\n","")
            if len(l) == 0:
                input.append(pair)
                pair = []
            else:
                pair.append(parse(l.split(" ")[0]))
        
    input.append(pair)
    print("Part 1: " + str(part1(deepcopy(input))))
    print("Part 2: " + str(part2(deepcopy(input))))

def part1(input):
    idxs = []
    for i in range(0,len(input)):
        (p1,p2) = input[i]
        res = check(deepcopy(p1), deepcopy(p2))
        if res == CHECK.TRUE or res == CHECK.EQUAL:
            idxs.append(i+1)

    return sum(idxs)

def part2(input):
    packets = []
    for (p1,p2) in input:
        packets.append(p1)
        packets.append(p2)
    
    packets.append([[2]])
    packets.append([[6]])

    sorting = True
    while sorting:
        sorting = False
        for i in range(0,len(packets)-1):
            res = check(deepcopy(packets[i]), deepcopy(packets[i+1]))
            if res == CHECK.FALSE:
                tmp = packets[i]
                packets[i] = packets[i+1]
                packets[i+1] = tmp
                sorting = True

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)


def check(p1,p2):
    k = 0
    while True:
        if k >= len(p1) and k >= len(p2):
            return CHECK.EQUAL
        if k >= len(p1):
            return CHECK.TRUE
        if k >= len(p2):
            return CHECK.FALSE
            
        if type(p1[k]) is list and type(p2[k]) is int:
            p2[k] = [p2[k]]
        if type(p1[k]) is int and type(p2[k]) is list:
            p1[k] = [p1[k]]

        if type(p1[k]) is int:
            if p1[k] > p2[k]:
                return CHECK.FALSE
            elif p1[k] < p2[k]:
                return CHECK.TRUE

        else:
            res = check(p1[k], p2[k])
            if res == CHECK.TRUE:
                return CHECK.TRUE
            elif res == CHECK.FALSE:
                return CHECK.FALSE

        k += 1

def parse(line):
    packet = []
    i = 1
    num = ""
    while i < len(line)-1:
        if line[i] == '[':
            p = ""
            extra = 1
            for j in range(i, len(line)-1):
                p = p + line[j]
                if line[j] == ']':
                    extra -= 1
                    if extra == 0:
                        packet.append(parse(p))
                        i = j
                        break
                elif line[j] == '[' and j != i:
                    extra += 1
        elif line[i].isdigit():
            num = ""

            while line[i].isdigit():
                num += line[i]
                i+=1
            packet.append(int(num))

        i += 1

    return packet


if __name__ == "__main__":
    sys.exit(main())