import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day22.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    bricks = []
    for line in input:
        (x1,y1,z1), (x2,y2,z2) = [x.split(",") for x in line.split("~")]
        bricks.append(((int(x1),int(x2)), (int(y1),int(y2)),(int(z1),int(z2))))

    bricks.sort(key=lambda p: min(p[2]))
    for i in range(0, len(bricks)):
        (x1,y1,z1) = bricks[i]
        floor = 0
        for j in range(0, i):
            if (j == i):
                continue
            (x2,y2,z2) = bricks[j]
            if overlap(x1,x2) and overlap(y1,y2):
                if max(z2) > floor:
                    floor = max(z2)
        bricks[i] = (x1,y1,(floor + 1, floor + 1 + (z1[1] - z1[0])))

    supp = dict()
    for i in range(0, len(bricks)):
        (x1,y1,z1) = bricks[i]
        tmp = set()
        for j in range(0, i):
            if j == i:
                continue
            (x2,y2,z2) = bricks[j]
            if min(z1)-1 == max(z2) and overlap(x1,x2) and overlap(y1,y2):
                tmp.add(bricks[j])
        
        supp[bricks[i]] = tmp
    
    count = 0
    for i in range(0, len(bricks)):
        (x1,y1,z1) = bricks[i]
        needed = False
        for j in range(i, len(bricks)):
            if j == i:
                continue
            if bricks[i] in supp[bricks[j]] and len(supp[bricks[j]]) == 1:
                needed = True
                break
        if not needed:
            count += 1

    return count


def part2(input):
    bricks = []
    for line in input:
        (x1,y1,z1), (x2,y2,z2) = [x.split(",") for x in line.split("~")]
        bricks.append(((int(x1),int(x2)), (int(y1),int(y2)),(int(z1),int(z2))))

    bricks.sort(key=lambda p: min(p[2]))
    for i in range(0, len(bricks)):
        (x1,y1,z1) = bricks[i]
        floor = 0
        for j in range(0, i):
            if (j == i):
                continue
            (x2,y2,z2) = bricks[j]
            if overlap(x1,x2) and overlap(y1,y2):
                if max(z2) > floor:
                    floor = max(z2)
        bricks[i] = (x1,y1,(floor + 1, floor + 1 + (z1[1] - z1[0])))

    under = dict()
    for i in range(0, len(bricks)):
        (x1,y1,z1) = bricks[i]
        tmp = set()
        for j in range(0, i):
            if j == i:
                continue
            (x2,y2,z2) = bricks[j]
            if min(z1)-1 == max(z2) and overlap(x1,x2) and overlap(y1,y2):
                tmp.add(bricks[j])
        
        under[bricks[i]] = tmp

    needed = set()
    for i in range(0, len(bricks)):
        (x1,y1,z1) = bricks[i]
        need = False
        for j in range(i, len(bricks)):
            if j == i:
                continue
            if bricks[i] in under[bricks[j]] and len(under[bricks[j]]) == 1:
                need = True
                break
        if need:
            needed.add(bricks[i])

    over = dict()
    for i in range(0, len(bricks)):
        (x1,y1,z1) = bricks[i]
        tmp = set()
        for j in range(0, len(bricks)):
            if j == i:
                continue
            (x2,y2,z2) = bricks[j]
            if max(z1)+1 == min(z2) and overlap(x1,x2) and overlap(y1,y2):
                tmp.add(bricks[j])
        
        over[bricks[i]] = tmp

    count = 0
    for n in needed:
        count += get_fallen(n, over, under)


    return count

def get_fallen(brick, over, under):
    fallen = set()
    fallen.add(brick)
    curr = over[brick]
    while curr:
        next = set()
        for n in curr:
            fall = True
            for s in under[n]:
                if s not in fallen:
                    fall = False
                    break
            if fall:
                fallen.add(n)
                for o in over[n]:
                    next.add(o)
        curr = next

    return len(fallen) - 1
            


def overlap(r1,r2):
    return r1[0] <= r2[1] and r2[0] <= r1[1]

if __name__ == "__main__":
    sys.exit(main())