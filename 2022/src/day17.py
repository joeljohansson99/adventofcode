import sys

rocks = {
    0 : [(2,0),(3,0),(4,0),(5,0)],
    1 : [(2,-1),(3,-2),(3,-1),(3,0),(4,-1)],
    2 : [(2,0),(3,0),(4,-2),(4,-1),(4,0)],
    3 : [(2,-3),(2,-2),(2,-1),(2,0)],
    4 : [(2,-1),(2,0),(3,-1),(3,0)]
}

def main():
    input = []
    with open('input/day17.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append([c for c in l])
    input = input[0]
    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    objects = set()
    top = 0
    length = len(input)
    k = 0
    for i in range(0,7):
        objects.add((i,0))
    for i in range(0, 2022):
        rock = rocks[i%5]
        rock = [(x,y-top-4) for (x,y) in rock]
        while True:
            push = input[k % length]
            tmp = [x for (x,y) in rock]
            if push == '<':
                if not (0 in tmp or any(o in objects for o in [(x-1,y) for (x,y) in rock])):
                    rock = [(x-1,y) for (x,y) in rock]
            elif push == '>':
                if not (6 in tmp or any(o in objects for o in [(x+1,y) for (x,y) in rock])):
                    rock = [(x+1,y) for (x,y) in rock]
            
            k+=1

            if len([(x,y+1) for (x,y) in rock if (x,y+1) not in objects]) != len(rock):
                for (_,y) in rock:
                    if abs(y) > top: 
                        top = abs(y)
                objects.update(rock)
                break
    
            rock = [(x,y+1) for (x,y) in rock]

    return abs(top)
            
def part2(input):
    objects = set()
    top = 0
    length = len(input)
    cache = dict()
    rock_amount = 1000000000000
    k = 0
    cycled = False
    
    for i in range(0,7):
        objects.add((i,0))

    i = 0
    while i < rock_amount:
        rock = rocks[i%5]
        rock = [(x,y-top-4) for (x,y) in rock]
        while True:
            push = input[k % length]
            tmp = [x for (x,y) in rock]
            if push == '<':
                if not (0 in tmp or any(o in objects for o in [(x-1,y) for (x,y) in rock])):
                    rock = [(x-1,y) for (x,y) in rock]
            elif push == '>':
                if not (6 in tmp or any(o in objects for o in [(x+1,y) for (x,y) in rock])):
                    rock = [(x+1,y) for (x,y) in rock]
            
            k+=1
            if len([(x,y+1) for (x,y) in rock if (x,y+1) not in objects]) != len(rock):
                for (_,y) in rock:
                    if abs(y) > top: 
                        top = abs(y)

                objects.update(rock)

                if not cycled:
                    xs = "".join([str(x) for (x,_) in rock])
                    if (xs, k % length) in cache:
                        if i > 10000:
                            (last_top, last_i) = cache[(xs, k % length)]
                            tmp = top

                            top_add = (top - last_top)*5
                            i_add = (i - last_i)*5

                            while i < rock_amount - i_add:
                                i += i_add
                                top += top_add

                            changed = top - tmp
                            objects = {(x, y-changed) for (x,y) in objects}
                            cycled = True
                    
                    else:
                        cache[("".join(xs), k % length)] = (top, i)

                break
            rock = [(x,y+1) for (x,y) in rock]
        i+=1
            

    return abs(top)



if __name__ == "__main__":
    sys.exit(main())