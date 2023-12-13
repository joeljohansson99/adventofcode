import os
import sys
import math

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day13.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    mirrors = []
    i = 0
    tmp = []
    while i < len(input):
        if len(input[i]) == 0:
            mirrors.append(tmp)
            tmp = []
        else:
            tmp.append(input[i])
        i+=1
    mirrors.append(tmp)    
    
    ret = 0
    for mirror in mirrors:
        hor = checkHor(mirror)
        ver = checkVert(mirror)
        if hor > 0:
            ret += hor * 100
        elif ver > 0:
            ret += ver
    return ret

def checkHor(mirror):
    for i in range(0,len(mirror)-1):
        reflection = True
        for r in range (1,len(mirror)):
            if i+r >= len(mirror) or i-r+1 < 0:
                break
            if mirror[i+r] != mirror[i-r+1]:
                reflection = False
                break
        if reflection:
            return i + 1
    return 0


def checkVert(mirror):
    for i in range(0,len(mirror[0])-1):
        reflection = True
        for c in range(0,len(mirror[0])):
            if i+c >= len(mirror[0]) or i-c+1 < 0:
                break
            for r in range(0, len(mirror)):
                if mirror[r][i+c] != mirror[r][i-c+1]:
                    reflection = False
                    break
            if not reflection:
                break
        if reflection:
            return i+1
    return 0

def part2(input):
    mirrors = []
    i = 0
    tmp = []
    while i < len(input):
        if len(input[i]) == 0:
            mirrors.append(tmp)
            tmp = []
        else:
            tmp.append(input[i])
        i+=1
    mirrors.append(tmp)    
    ret = 0
    for i in range(0,len(mirrors)):
        found = False
        
        oldHor = checkHor(mirrors[i])
        oldVer = checkVert(mirrors[i])
        
        for r in range(0,len(mirrors[i])):
            for c in range(0,len(mirrors[i][0])):
                hor = checkHor2(mirrors[i], (r,c), oldHor)
                ver = checkVert2(mirrors[i], (r,c), oldVer)
                    
                if (hor > 0 or ver > 0):
                    found = True
                    break
                
            if found:
                break
        
        if hor > 0:
            ret += hor * 100
        elif ver > 0:
            ret += ver
    return ret


def checkHor2(mirror, smudge, old):
    for i in range(0,len(mirror)-1):
        reflection = True
        for r in range (1,len(mirror)):
            if i+r >= len(mirror) or i-r+1 < 0:
                break
            for c in range(0, len(mirror[r])):
                if mirror[i+r][c] != mirror[i-r+1][c]:
                    if (i+r, c) != smudge and (i-r+1, c) != smudge:
                        reflection = False
                        break
        if reflection and i+1 != old:
            return i + 1
    return 0


def checkVert2(mirror,smudge,old):
    ret = []
    for i in range(0,len(mirror[0])-1):
        reflection = True
        for c in range(0,len(mirror[0])):
            if i+c >= len(mirror[0]) or i-c+1 < 0:
                break
            for r in range(0, len(mirror)):
                if mirror[r][i+c] != mirror[r][i-c+1]:
                    if (r, i+c) != smudge and (r, i-c+1) != smudge:
                        reflection = False
                        break       
                    
            if not reflection:
                break
        if reflection and i+1 != old:
            return i+1
    return 0

if __name__ == "__main__":
    sys.exit(main())