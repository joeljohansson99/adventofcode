
import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day24.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
    values = dict()
    exprs = dict()
    for line in input:
        if ":" in line:
            [val,bit] = line.split(":")
            values[val] = int(bit.strip())
        elif len(line) > 1:
            [A, op, B, _, C] = line.split(" ")
            exprs[C] = (A,op,B)
    
    all = list(set(values.keys()).union(set(exprs.keys())))
    
    word = ""
    for v in sorted(all, reverse=True):
        if v[0] == "z":
            x = eval(v, values, exprs)
            word += str(x)
    print(word)
    return int(word, 2)


def part2(input):
    values = dict()
    exprs = dict()
    for line in input:
        if ":" in line:
            [val,bit] = line.split(":")
            values[val] = int(bit.strip())
        elif len(line) > 1:
            [A, op, B, _, C] = line.split(" ")
            exprs[C] = (A,op,B)
    
    all = list(set(values.keys()).union(set(exprs.keys())))

    swap("z07", "shj", exprs)
    swap("z27", "kcd", exprs)
    swap("z23", "pfn", exprs)
    checked = set()
    for w1 in exprs.keys():
        checked.add(w1)
        found = False
        for w2 in exprs.keys():
            tmp = dict(exprs)
            try:
                if w2 in checked:
                    continue
                values = dict()
                for line in input:
                    if ":" in line:
                        [val,bit] = line.split(":")
                        values[val] = int(bit.strip())

                swap(w1,w2,tmp)

                xs = ""
                ys = ""
                for v in sorted(all, reverse=True):
                    if v[0] == "x":
                        x = eval(v, values, tmp)
                        xs += str(x)
                    elif v[0] == "y":
                        y = eval(v, values, tmp)
                        ys += str(y)

                x = int(xs, 2)
                y = int(ys, 2)

                addition = add_binary(x,y)

                word = ""
                for v in sorted(all, reverse=True):
                    eval(v, values, tmp)
                    if v[0] == "z":
                        x = eval(v, values, tmp)
                        word += str(x)

                if word == addition and w1[0] != "z" and w2[0] != "z":
                    f1 = w1
                    f2 = w2
                    print("FOUND", w1,w2)
                    found = True
                    break
            except:
                pass
        if found:
            break

    return ",".join(sorted(["z07","z27", "z23","shj","kcd","pfn",f1,f2]))

def swap(A,B,exprs):
    tmp = exprs[A]
    exprs[A] = exprs[B]
    exprs[B] = tmp

def add_binary(a,b):
    return bin(a+b)[2:]

def deval(V, exprs, values, l):
    if V not in exprs:
        return str(V)+ "," + str(values[V])
    (A, op, B) = exprs[V]
    if l == 0:
        return str(V)
    # or V == "wwv" or V == "gnj"
    # if V == "hbd":
    # #     return V + "," + str(values[V])
    # if A[0] == "x" or A[0] == "y":
    #     # print("HERE", V, A, B)
    #     return str(V) + "," + str(values[V])
    return "("+deval(A, exprs, values,l-1) + " " +op +" "+ deval(B, exprs, values,l-1)+")"


def eval(V, values, exprs):
    if V in values:
        return values[V]
    (A, op, B) = exprs[V]
    if A in values:
        val_A = values[A]
    else:
        val_A = eval(A, values, exprs)
        values[A] = val_A
    if B in values:
        val_B = values[B]
    else:
        val_B = eval(B, values, exprs)
        values[B] = val_B
    
    if op == "AND":
        values[V] = 1 if val_A == 1 and val_B == 1 else 0
    elif op == "OR":
        values[V] = 1 if val_A == 1 or val_B == 1 else 0
    elif op == "XOR":
        values[V] = 1 if val_A != val_B else 0

    return values[V]

if __name__ == "__main__":
    sys.exit(main())