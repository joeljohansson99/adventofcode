import sys

def main():
    input = []
    with open('input/day6.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)
    input = input[0]
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    found = False
    i = 0
    code = ""
    while not found:
        c = input[i]
        i += 1
        if i <= 4:
            code += c
        else:
            code = code[1:] + c
            if code == ''.join(sorted(set(code), key=code.index)):
                found = True
    return i

def part2(input):
    found = False
    i = 0
    code = ""
    while not found:
        c = input[i]
        i += 1
        if i <= 14:
            code += c
        else:
            code = code[1:] + c
            if code == ''.join(sorted(set(code), key=code.index)):
                found = True
    return i

if __name__ == "__main__":
    sys.exit(main())