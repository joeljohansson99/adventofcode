import sys


def main():

    input = []
    with open('input/day14.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","").split(" -> ")
            for i in range(0, len(l)-1):
                p1 = l[i].split(",")
                p1 = (int(p1[0]), int(p1[1]))
                p2 = l[i+1].split(",")
                p2 = (int(p2[0]), int(p2[1]))
                input.append((p1,p2))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    objects = set()
    for (p1,p2) in input:
        if p1[0] == p2[0]:
            ymin = min(p1[1], p2[1])
            ymax = max(p1[1], p2[1])
            for i in range(ymin, ymax+1):
                objects.add((p1[0], i))
        elif p1[1] == p2[1]:
            xmin = min(p1[0], p2[0])
            xmax = max(p1[0], p2[0])
            for i in range(xmin, xmax+1):
                objects.add((i, p1[1]))

    lowest = max([y for (_,y) in objects])
    rocks = len(objects)
    start = (500,0)
    rest = True

    while rest:
        (x,y) = start
        while True:
            if y >= lowest:
                rest = False
                break
            elif (x,y+1) not in objects:
                (x,y) = (x,y+1)
            elif (x-1,y+1) not in objects:
                (x,y) = (x-1,y+1)
            elif (x+1,y+1) not in objects:
                (x,y) = (x+1,y+1)
            else:
                objects.add((x,y))
                (x,y) = start
    
    return len(objects) - rocks




def part2(input):
    objects = set()
    for (p1,p2) in input:
        if p1[0] == p2[0]:
            ymin = min(p1[1], p2[1])
            ymax = max(p1[1], p2[1])
            for i in range(ymin, ymax+1):
                objects.add((p1[0], i))
        elif p1[1] == p2[1]:
            xmin = min(p1[0], p2[0])
            xmax = max(p1[0], p2[0])
            for i in range(xmin, xmax+1):
                objects.add((i, p1[1]))

    lowest = max([y for (_,y) in objects]) + 2
    rocks = len(objects)
    start = (500,0)
    rest = True

    while rest:
        (x,y) = start
        while True:
            if y+1 != lowest:
                if (x,y+1) not in objects:
                    (x,y) = (x,y+1)
                elif (x-1,y+1) not in objects:
                    (x,y) = (x-1,y+1)
                elif (x+1,y+1) not in objects:
                    (x,y) = (x+1,y+1)
                elif (x,y) == start:
                    objects.add((x,y))
                    rest = False
                    break
                else:
                    objects.add((x,y))
                    (x,y) = start
            else:
                objects.add((x,y))
                (x,y) = start
    
    return len(objects) - rocks

if __name__ == "__main__":
    sys.exit(main())
