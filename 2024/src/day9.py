import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day9.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    disk = []
    id = 0
    length = 0
    for i in range(len(input[0])):
        if i % 2 == 0:
            disk.append((str(id), int(input[0][i])))
            id+=1
            length+=1
        else:
            disk.append((-1, int(input[0][i])))
    
    free = 0
    while len(disk) > length:
        (id, size) = disk[len(disk)-1]
        disk = disk[:len(disk)-1]
        if id == -1:
            continue
        else:
            done = False
            for i in range(free, len(disk)):
                (did, dl) = disk[i]
                if did != -1:
                    continue
                if dl == size:
                    disk[i] = (id, size)
                    free = i
                    done = True
                    break
                elif dl > size:
                    disk[i] = (id, size)
                    disk.insert(i+1, (-1, dl-size))
                    free = i
                    done = True
                    break
                else:
                    disk[i] = (id, dl)
                    size = (size - dl)
            
            if not done:
                disk.append((id,size))
                break
    
    sum = 0
    idx = 0
    for i in range(len(disk)):
        (id, size) = disk[i]
        if id != -1:
            for i in range(idx, idx+size):
                sum += (int(id)*i)
                idx+=1

    return sum



def part2(input):
    disk = []
    id = 0
    length = 0
    for i in range(len(input[0])):
        if i % 2 == 0:
            disk.append((str(id), int(input[0][i])))
            id+=1
            length+=1
        else:
            disk.append((-1, int(input[0][i])))
    
    next = 1
    seen = set()
    while next <= len(disk):
        idx = len(disk)-next
        (id, size) = disk[idx]
        next += 1
        if id == -1:
            continue
        else:
            if (id,size) in seen:
                continue
            seen.add((id,size))
            done = False
            for i in range(idx):
                (did, dl) = disk[i]
                if did != -1:
                    continue
                if dl == size:
                    disk[i] = (id, size)
                    done = True
                    break
                elif dl > size:
                    disk[i] = (id, size)
                    disk.insert(i+1, (-1, dl-size))
                    idx+=1
                    next+=1
                    done = True
                    break
            
            if done:
                disk[idx] = (-1, size)
    
    sum = 0
    idx = 0
    for i in range(len(disk)):
        (id, size) = disk[i]
        if id != -1:
            for i in range(idx, idx+size):
                sum += (int(id)*i)
                idx+=1
        else:
            idx += size

    return sum


if __name__ == "__main__":
    sys.exit(main())