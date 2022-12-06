import sys

def main():

    input = []
    with open('input/day3.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    sack = []
    for str in input:
        s1 = str[:int(len(str)/2)]
        s2 = str[int(len(str)/2):]
        dup = []
        for s in s1:
            if s in s2 and s not in dup:
                dup.append(s)
                sack.append(s)
    prio = 0
    for s in sack:
        if s.isupper():
            prio += ord(s) - 38
        else: 
            prio += ord(s)- 96

    return prio

def part2(input):
    group = []
    input = chunks(input, 3)

    for elfs in input:
        for s in elfs[0]:
            if s in elfs[1] and s in elfs[2]:
                group.append(s)
                break

    prio = 0
    for s in group:
        if s.isupper():
            prio += ord(s) - 38
        else: 
            prio += ord(s)- 96

    return prio

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

if __name__ == "__main__":
    sys.exit(main())