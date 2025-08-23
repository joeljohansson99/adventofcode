
import re

DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Right, Up, Left, Down

def ints(str):
    return list(map(int,re.findall(r'[+-]?\d+(?:\.\d+)?', str)))

def left(dir):
    idx = DIRECTIONS.index(dir)
    return DIRECTIONS[(idx + 1) % 4]

def right(dir):
    idx = DIRECTIONS.index(dir)
    return DIRECTIONS[(idx - 1) % 4]

def neighbours(r,c):
    return [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]

