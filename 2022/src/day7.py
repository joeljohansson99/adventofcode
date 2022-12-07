import sys
from copy import deepcopy

def main():
    input = []
    with open('input/day7.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)
    
    folders = dict()
    folders = parse(folders, input, "")
    folders = sum(folders, "//")

    print("Part 1: " + str(part1(folders)))
    print("Part 2: " + str(part2(folders)))

def part1(folders):
    total = 0
    for space in folders.values():
        if space <= 100000:
            total += space
    return total


def part2(folders):
    need = 30000000 - (70000000 - folders["//"])
    best = -folders["//"]
    deleted = 0
    for space in folders.values():
        overfreed = (need - space)
        if overfreed < 0 and overfreed > best:
            best = overfreed
            deleted = space
    return deleted

def sum(folders, curr):
    if isinstance(folders[curr], int):
        return folders

    space = 0
    for cont in folders[curr]:
        if cont.isdigit():
            space += int(cont)
        else:
            folders = sum(folders, cont)
            space += folders[cont]

    folders[curr] = space

    return folders

def parse(folders, commands, curr):

    if len(commands) == 0:
        return folders

    cmd = commands.pop(0).split(" ")
    
    if cmd[0] == "$":
        if cmd[1] == "cd":
            if cmd[2] == "..":
                return folders
            else:
                folders = parse(folders, commands, (curr + "/" + cmd[2]))
        
        elif cmd[1] == "ls":
            folders[curr] = []
            while True:
                if len(commands) == 0:
                    break
                cmd = commands[0].split(" ")
                if cmd[0] == "$":
                    break
                else:
                    if cmd[0] == "dir":
                        folders[curr].append(curr + "/" + cmd[1])
                    else:
                        folders[curr].append(cmd[0])
                    commands.pop(0)
    
        folders = parse(folders, commands, curr)
    
    return folders

if __name__ == "__main__":
    sys.exit(main())