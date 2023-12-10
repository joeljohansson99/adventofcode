import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day10.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))


def part1(input):
    start = 0
    for r in range(0, len(input)):
        for c in range(0, len(input[r])):
            if input[r][c] == 'S':
                start = (r,c)
                break
            
    return bfs(start, input)

def bfs(start, map):
    done = set(start)
    curr = [start]
    steps = 0
    while (True):
        new = []
        found = False
        for (r,c) in curr:
            cc = map[r][c]
            if cc == '|':
                next = [(r+1, c),(r-1, c)]
                for n in next: 
                    if not n in done and n[0] >= 0 and n[0] < len(map) and n[1] >= 0 and n[1] < len(map[0]):
                        found = True
                        new.append(n)
                        done.add(n)
                        
            elif cc == '-':
                next = [(r, c+1),(r, c-1)]
                for n in next: 
                    if not n in done and n[0] >= 0 and n[0] < len(map) and n[1] >= 0 and n[1] < len(map[0]):
                        found = True
                        new.append(n)
                        done.add(n)
                        
            elif cc == 'L':
                next = [(r-1, c),(r, c+1)]
                for n in next: 
                    if not n in done and n[0] >= 0 and n[0] < len(map) and n[1] >= 0 and n[1] < len(map[0]):
                        found = True
                        new.append(n)
                        done.add(n)
            
            elif cc == 'J':
                next = [(r-1, c),(r, c-1)]
                for n in next: 
                    if not n in done and n[0] >= 0 and n[0] < len(map) and n[1] >= 0 and n[1] < len(map[0]):
                        found = True
                        new.append(n)
                        done.add(n)
                        
            elif cc == '7':
                next = [(r+1, c),(r, c-1)]
                for n in next: 
                    if not n in done and n[0] >= 0 and n[0] < len(map) and n[1] >= 0 and n[1] < len(map[0]):
                        found = True
                        new.append(n)
                        done.add(n)
                
            elif cc == 'F':
                next = [(r+1, c),(r, c+1)]
                for n in next: 
                    if not n in done and n[0] >= 0 and n[0] < len(map) and n[1] >= 0 and n[1] < len(map[0]):
                        found = True
                        new.append(n)
                        done.add(n)
            elif cc == 'S':
                next = [(r+1, c),(r, c+1)]
                
                for n in next: 
                    if n[0] >= 0 and n[0] < len(map) and n[1] >= 0 and n[1] < len(map[0]):
                        found = True
                        new.append(n)
                        done.add(n)
        
        curr = new
        if not found:
            break
        steps+=1
        
    return steps
                

def part2(input):
    start = 0
    tmp = []
    for r in range(0,len(input)):
        tmp.append(input[r])
        exp = ""
        for c in range(0,len(input[r])):
            if input[r][c] == '|' or input[r][c] == '7' or input[r][c] == 'F' or input[r][c] == 'S':
                if input[r][c] == '|' or input[r][c] == '7' or input[r][c] == 'F' or input[r][c] == 'S':
                    exp += '|'
            else:
                exp += '.'
        tmp.append(exp)
    input = tmp
    tmp = ["" for r in input]
    for c in range(0,len(input[0])):
        for r in range(0, len(input)):
            tmp[r] += input[r][c]
            if input[r][c] == '-' or input[r][c] == 'L' or input[r][c] == 'F' or input[r][c] == 'S':
                tmp[r] += '-' 
            else:
                tmp[r] += '*'
    input = tmp
    
    for r in range(0, len(input)):
        for c in range(0, len(input[r])):
            if input[r][c] == 'S':
                start = (r,c)
                break
            
    walls = bfs2(start,input)
    
    rs = [r for (r,c) in walls]
    minR = min(rs)
    maxR = max(rs)
    
    areas = set()
    for r in range(minR, maxR+1):
        for (r,c) in reg(r, len(input[r]), walls):
            areas.add((r,c))
    
    fields = group(areas)
    
    tmp = []
    for f in fields:
        for x in f:
            tmp.append(x)
            
    sum = 0
    enclosed = set()
    for f in fields:
        encl = True
        for (r,c) in f:
            adj = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            
            for (nr, nc) in adj:
                if nr < len(input) and nr >= 0 and nc < len(input[0]) and nc >= 0:
                    if not (nr, nc) in walls and not (nr, nc) in f:
                        encl = False
                        break
                else:
                    encl = False
                    break
            if not encl:
                break
        if encl:
            for n in f:
                if n[0] % 2 == 0 and n[1] % 2 == 0:
                    enclosed.add(n)
    
    for r in range(0, len(input)):
        for c in range(0, len(input[r])):
            if (r,c) in enclosed:
                sum += 1
                
    return sum

def group(areas):
    groups = []
    done = set()
    while len(areas) != 0:
        next = areas.pop()
        group = set()
        group.add(next)
        while (True):
            found = False
            for (r,c) in areas:
                adj = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for a in adj:
                    if a in group:
                        done.add((r,c))
                        group.add((r,c))
                        found = True
                        break
                    
            if not found:
                break

            for g in group:
                if g in areas:
                    areas.remove(g)
        
        groups.append(group)
    return groups

    
def reg(r, max, walls):
    before = 0
    for c in range(0, max):
        if (r, c) in walls:
            break
        before += 1
    after = 0
    for c in range(max-1, -1, -1):
        if (r, c) in walls:
            break
        after += 1
    
    ret = []
    for i in range(before, max-after):
        if (r, i) not in walls:
            ret.append((r,i))
    
    return ret

def bfs2(start, map):
    done = set()
    done.add(start)
    curr = [start]
    steps = 0
    while (True):
        new = []
        found = False
        for (r,c) in curr:
            cc = map[r][c]
            if cc == '|':
                next = [(r+1, c),(r-1, c)]
                for n in next: 
                    if not n in done and n[0] >= 0 and n[0] < len(map) and n[1] >= 0 and n[1] < len(map[0]):
                        found = True
                        new.append(n)
                        done.add(n)
                        
            elif cc == '-':
                next = [(r, c+1),(r, c-1)]
                for n in next: 
                    if not n in done and n[0] >= 0 and n[0] < len(map) and n[1] >= 0 and n[1] < len(map[0]):
                        found = True
                        new.append(n)
                        done.add(n)
                        
            elif cc == 'L':
                next = [(r-1, c),(r, c+1)]
                for n in next: 
                    if not n in done and n[0] >= 0 and n[0] < len(map) and n[1] >= 0 and n[1] < len(map[0]):
                        found = True
                        new.append(n)
                        done.add(n)
            
            elif cc == 'J':
                next = [(r-1, c),(r, c-1)]
                for n in next: 
                    if not n in done and n[0] >= 0 and n[0] < len(map) and n[1] >= 0 and n[1] < len(map[0]):
                        found = True
                        new.append(n)
                        done.add(n)
                        
            elif cc == '7':
                next = [(r+1, c),(r, c-1)]
                for n in next: 
                    if not n in done and n[0] >= 0 and n[0] < len(map) and n[1] >= 0 and n[1] < len(map[0]):
                        found = True
                        new.append(n)
                        done.add(n)
                
            elif cc == 'F':
                next = [(r+1, c),(r, c+1)]
                for n in next: 
                    if not n in done and n[0] >= 0 and n[0] < len(map) and n[1] >= 0 and n[1] < len(map[0]):
                        found = True
                        new.append(n)
                        done.add(n)
            elif cc == 'S':
                next = [(r+1, c),(r, c+1)]
                
                for n in next: 
                    if  n[0] >= 0 and n[0] < len(map) and n[1] >= 0 and n[1] < len(map[0]):
                        found = True
                        new.append(n)
                        done.add(n)
        
        curr = new
        if not found:
            break
        
    return done

if __name__ == "__main__":
    sys.exit(main())