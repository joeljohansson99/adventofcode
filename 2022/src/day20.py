import sys
import os

def main():

    input = []
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day20.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))


    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    file = [(i,int(num)) for i,num in enumerate(input)]
    
    for i in range(len(file)):
        for j in range(len(file)):
            if file[j][0] == i:
                num = file[j][1]
                break
        k = (j+num) % (len(file)-1)
        
        del file[j]
        file.insert(k, (i, num))
    
    zi = [f[1] for f in file].index((0))
    return file[(zi+1000)%len(file)][1] + file[(zi+2000)%len(file)][1] + file[(zi+3000)%len(file)][1]
        
def part2(input):
    file = [(i,int(num)*811589153) for i,num in enumerate(input)]
    for _ in range(10):
        for i in range(len(file)):
            for j in range(len(file)):
                if file[j][0] == i:
                    num = file[j][1]
                    break
            k = (j+num) % (len(file)-1)
            
            del file[j]
            file.insert(k, (i, num))
    
    zi = [f[1] for f in file].index((0))
    return file[(zi+1000)%len(file)][1] + file[(zi+2000)%len(file)][1] + file[(zi+3000)%len(file)][1]

if __name__ == "__main__":
    sys.exit(main())