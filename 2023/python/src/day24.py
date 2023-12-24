import os
import sys
import z3

RIGHT = (0,1)
LEFT = (0,-1)
UP = (-1,0)
DOWN = (1,0)

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day24.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    hails = []
    min = 200000000000000
    max = 400000000000000
    for line in input:
        (p, v) = line.split("@")
        p = p.split(",")
        v = v.split(",")
        (x,y,z) = (int(p[0]),int(p[1]),int(p[2]))
        (dx,dy,dz) = (int(v[0]),int(v[1]),int(v[2]))
        start = (x, y)
        end = (x+dx, y+dy)
        hails.append((start, end))

    count = 0
    for i in range(0, len(hails)):
        for j in range(i+1, len(hails)):
            intersect = line_intersection(hails[i], hails[j])
            if intersect:
                (x,y) = intersect
                if x >= min and x <= max and y >= min and y <= max:
                    if x > hails[i][0][0] and hails[i][1][0] < hails[i][0][0]:
                        continue
                    if x < hails[i][0][0] and hails[i][1][0] > hails[i][0][0]:
                        continue
                    if y > hails[i][0][1] and hails[i][1][1] < hails[i][0][1]:
                        continue
                    if y < hails[i][0][1] and hails[i][1][1] > hails[i][0][1]:
                        continue

                    if x > hails[j][0][0] and hails[j][1][0] < hails[j][0][0]:
                        continue
                    if x < hails[j][0][0] and hails[j][1][0] > hails[j][0][0]:
                        continue
                    if y > hails[j][0][1] and hails[j][1][1] < hails[j][0][1]:
                        continue
                    if y < hails[j][0][1] and hails[j][1][1] > hails[j][0][1]:
                        continue
                    
                    else:
                        count+=1
                    
    return count

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return False

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

def part2(input):
    velocites = []
    starts = []
    for line in input:
        (p, v) = line.split("@")
        p = p.split(",")
        v = v.split(",")
        (x,y,z) = (int(p[0]),int(p[1]),int(p[2]))
        (dx,dy,dz) = (int(v[0]),int(v[1]),int(v[2]))
        velocites.append((dx,dy,dz))
        starts.append((x, y, z))

    x = z3.Real('x')
    y = z3.Real('y')
    z = z3.Real('z')

    dx = z3.Real('dx')
    dy = z3.Real('dy')
    dz = z3.Real('dz')

    solver = z3.Solver()

    for i in range(0, len(starts)):
        (px, py, pz) = starts[i]
        (dpx, dpy, dpz) = velocites[i]
        t = z3.Real(f't{i}')
        solver.append(x + dx*t == px + dpx*t)
        solver.append(y + dy*t == py + dpy*t)
        solver.append(z + dz*t == pz + dpz*t)

    solver.check()
    sol = solver.model()

    return int(sol[x].as_fraction().numerator) + int(sol[y].as_fraction().numerator) + int(sol[z].as_fraction().numerator)


if __name__ == "__main__":
    sys.exit(main())