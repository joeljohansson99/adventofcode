import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day5.txt') as f:
        for line in f.readlines():
            l = line.replace("\n","")
            input.append(l)

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))


def part1(input):
    seeds = [int(x) for x in input[0].split(":")[1].split(" ") if len(x) > 0]
    maps = []
    
    for i in range(1, len(input)):
        if input[i] == "seed-to-soil map:":
            i+=1
            sf = []
            while (input[i] != ""):
                sf.append([int(x) for x in input[i].split(" ")])
                i+=1
            maps.append(sf)
            
        elif input[i] == "soil-to-fertilizer map:":
            i+=1
            sf = []
            while (input[i] != ""):
                sf.append([int(x) for x in input[i].split(" ")])
                i+=1
            maps.append(sf)
            
        elif input[i] == "fertilizer-to-water map:":
            i+=1
            sf = []
            while (input[i] != ""):
                sf.append([int(x) for x in input[i].split(" ")])
                i+=1
            maps.append(sf)
            
        elif input[i] == "water-to-light map:":
            i+=1
            sf = []
            while (input[i] != ""):
                sf.append([int(x) for x in input[i].split(" ")])
                i+=1
            maps.append(sf)
            
        elif input[i] == "light-to-temperature map:":
            i+=1
            sf = []
            while (input[i] != ""):
                sf.append([int(x) for x in input[i].split(" ")])
                i+=1
            maps.append(sf)
            
        elif input[i] == "temperature-to-humidity map:":
            i+=1
            sf = []
            while (input[i] != ""):
                sf.append([int(x) for x in input[i].split(" ")])
                i+=1
            maps.append(sf)
            
        elif input[i] == "humidity-to-location map:":
            i+=1
            sf = []
            while (i < len(input) and input[i] != ""):
                sf.append([int(x) for x in input[i].split(" ")])
                i+=1
            maps.append(sf)
    
    maps = [x for x in maps if len(x) > 0]
    for map in maps:
        for i in range(0, len(seeds)):
            for rang in map:
                (dest, src, inc) = rang
                if src <= seeds[i] and src + inc >= seeds[i]:
                    seeds[i] = (dest + (seeds[i] - src))
                    break
            
    return min(seeds)

def part2(input):
    seeds = [int(x) for x in input[0].split(":")[1].split(" ") if len(x) > 0]
    it = iter(seeds)
    seeds = list(zip(it,it))
    seeds = list([x,x+y-1] for (x,y) in seeds)
        
    maps = []
    for i in range(1, len(input)):
        if input[i] == "seed-to-soil map:":
            i+=1
            sf = []
            while (input[i] != ""):
                sf.append([int(x) for x in input[i].split(" ")])
                i+=1
            maps.append(sorted(sf, key=lambda x: x[1]))
            
        elif input[i] == "soil-to-fertilizer map:":
            i+=1
            sf = []
            while (input[i] != ""):
                sf.append([int(x) for x in input[i].split(" ")])
                i+=1
            maps.append(sorted(sf, key=lambda x: x[1]))
            
        elif input[i] == "fertilizer-to-water map:":
            i+=1
            sf = []
            while (input[i] != ""):
                sf.append([int(x) for x in input[i].split(" ")])
                i+=1
            maps.append(sorted(sf, key=lambda x: x[1]))
            
        elif input[i] == "water-to-light map:":
            i+=1
            sf = []
            while (input[i] != ""):
                sf.append([int(x) for x in input[i].split(" ")])
                i+=1
            maps.append(sorted(sf, key=lambda x: x[1]))
            
        elif input[i] == "light-to-temperature map:":
            i+=1
            sf = []
            while (input[i] != ""):
                sf.append([int(x) for x in input[i].split(" ")])
                i+=1
            maps.append(sorted(sf, key=lambda x: x[1]))
            
        elif input[i] == "temperature-to-humidity map:":
            i+=1
            sf = []
            while (input[i] != ""):
                sf.append([int(x) for x in input[i].split(" ")])
                i+=1
            maps.append(sorted(sf, key=lambda x: x[1]))
            
        elif input[i] == "humidity-to-location map:":
            i+=1
            sf = []
            while (i < len(input) and input[i] != ""):
                sf.append([int(x) for x in input[i].split(" ")])
                i+=1
            maps.append(sorted(sf, key=lambda x: x[1]))
    
    maps = [x for x in maps if len(x) > 0]
    
    for map in maps:
        new_seeds = []
        for seed in seeds:
            for (dest, src, inc) in map:
                overlap = [max(seed[0], src), min(seed[1], src+inc)]
                if overlap[0] < overlap[1]:
                    diff = dest - src
                    new_seeds.append([overlap[0]+diff, overlap[1]+diff])
                    
                    if overlap[0] > seed[0]:
                        new_seeds.append([seed[0], overlap[1]])
                    seed[0] = overlap[1]
            
            if (seed[0] < seed[1]):
                new_seeds.append(seed)
                    
        seeds = new_seeds       
    
    return min([x for (x,y) in seeds])

if __name__ == "__main__":
    sys.exit(main())