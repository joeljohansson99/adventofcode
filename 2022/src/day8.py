import sys


def main():
    input = []
    with open('input/day8.txt') as f:
        for line in f.readlines():
            l = [int(n) for n in list(line.replace("\n",""))]
            input.append(l)
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    count = 0
    for r in range(0, len(input)):
        for c in range(0, len(input[0])):
            row = input[r]
            col = [row[c] for row in input]

            if visibleLine(row, c) or visibleLine(col, r):
                count += 1
    
    return count

def visibleLine(line, pos):
    visible = True
    for i in range(0, len(line)):
        if i == pos:
            if visible:
                break
            else:
                visible = True
        elif line[i] >= line[pos]:
            visible = False
            if i > pos:
                break
            else:
                i = pos-1
    
    return visible


def part2(input):
    best = 0
    for r in range(0, len(input)):
        for c in range(0, len(input[0])):
            row = input[r]
            col = [row[c] for row in input]

            view = rightView(row, c) * leftView(row, c) * upView(col, r) * downView(col, r)
            
            if view > best:
                best = view
    
    return best


def rightView(row, pos):
    count = 0
    for r in range(pos+1, len(row)):
        count += 1
        if row[r] >= row[pos]:
            break
    
    return count

def leftView(row, pos):
    count = 0
    for r in range(pos-1, -1, -1):
        if row[r] >= row[pos]:
            break
        count += 1
    return count

def downView(col, pos):
    count = 0
    for c in range(pos+1, len(col)):
        count += 1
        if col[c] >= col[pos]:
            break
    return count

def upView(col, pos):
    count = 0
    for c in range(pos-1, -1, -1):
        count += 1
        if col[c] >= col[pos]:
            break
    return count

if __name__ == "__main__":
    sys.exit(main())