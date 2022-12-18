import sys

def main():

    input = []
    with open('input/day18.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            [x,y,z] = [int(p) for p in l.split(",")]
            input.append((x,y,z))
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    points = set(input)
    count = 0
    
    for (x,y,z) in points:
        if not (x-1, y, z) in points:
            count +=1
        if not (x+1, y, z) in points:
            count +=1
        if not (x, y+1, z) in points:
            count +=1
        if not (x, y-1, z) in points:
            count +=1
        if not (x, y, z-1) in points:
            count +=1
        if not (x, y, z+1) in points:
            count +=1
    
    return count

def part2(input):
    points = set(input)
    count = 0
    xs = [x for (x,_,_) in points]
    ys = [y for (_,y,_) in points]
    zs = [z for (_,_,z) in points]
    xlimit = (min(xs),max(xs))
    ylimit = (min(ys),max(ys))
    zlimit = (min(zs),max(zs))

    bubbles = air_bubbles(points, xlimit, ylimit, zlimit)

    for (x,y,z) in points:
        if not (x-1, y, z) in points and not any([(x-1, y, z) in b for b in bubbles]):
            count +=1
        if not (x+1, y, z) in points and not any([(x+1, y, z) in b for b in bubbles]) :
            count +=1
        if not (x, y+1, z) in points and not any([(x, y+1, z) in b for b in bubbles]):
            count +=1
        if not (x, y-1, z) in points and not any([(x, y-1, z) in b for b in bubbles]):
            count +=1
        if not (x, y, z-1) in points and not any([(x, y, z-1) in b for b in bubbles]):
            count +=1
        if not (x, y, z+1) in points and not any([(x, y, z+1) in b for b in bubbles]):
            count +=1
    return count
            
def air_bubbles(points, xlimit, ylimit, zlimit):
    bubbles = []
    for sx in range(xlimit[0]-1, xlimit[1]):
        for sy in range(ylimit[0]-1, ylimit[1]):
            for sz in range(zlimit[0]-1, zlimit[1]):
                if (sx,sy,sz) not in points and not any([(sx,sy,sz) in b for b in bubbles]):
                    queue = set()
                    queue.add((sx,sy,sz))
                    surface = False
                    bubble = set()
                    bubble.add((sx,sy,sz))
                    while len(queue) != 0 and not surface:
                        next = set()
                        for (x,y,z) in queue:
                            neighbours = {
                                (x-1, y, z),
                                (x+1, y, z),
                                (x, y-1, z),
                                (x, y+1, z),
                                (x, y, z-1),
                                (x, y, z+1)
                            }
                            for (nx,ny,nz) in neighbours:
                                if nx < xlimit[0] or nx > xlimit[1] or ny < ylimit[0] or ny > ylimit[1] or nz < zlimit[0] or nz > zlimit[1]:
                                    surface = True
                                    break
                                if (nx,ny,nz) not in bubble and (nx,ny,nz) not in points:
                                    bubble.add((nx,ny,nz))
                                    next.add((nx,ny,nz))
                        queue = next
                    
                    if not surface:
                        bubbles.append(bubble)

    return bubbles

if __name__ == "__main__":
    sys.exit(main())