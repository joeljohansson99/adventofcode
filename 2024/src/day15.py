import os
import sys

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day15.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):

	grid = []
	moves = []
	for line in input:
		if "#" in line:
			grid.append(line)
		elif line == "\n":
			continue
		else:
			moves.append(line)
		
	moves = "".join(moves)

	stones = []
	walls = set()
	robot = (-1,-1)
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			if grid[r][c] == "O":
				stones.append((r,c))
			elif grid[r][c] == "#":
				walls.add((r,c))
			elif grid[r][c] == "@":
				robot = (r,c)
	
	for move in moves:
		# print("\n" + move)
		(r,c) = robot
		if move == "<":
			(can, new_stones) = step((r,c-1), (0,-1), stones, walls)
			if can:
				robot = (r,c-1)
			stones = new_stones
		if move == "^":
			(can, new_stones) = step((r-1,c), (-1,0), stones, walls)
			if can:
				robot = (r-1,c)
			stones = new_stones
		if move == ">":
			(can, new_stones) = step((r,c+1), (0,1), stones, walls)
			if can:
				robot = (r,c+1)
			stones = new_stones
		if move == "v":
			(can, new_stones) = step((r+1,c), (1,0), stones, walls)
			if can:
				robot = (r+1,c)
			stones = new_stones

	sum = 0
	for stone in stones:
		sum += stone[0]*100 + stone[1]

	return sum

		# print_map(grid, stones, walls, robot)
	# print(stones, walls, robot)
    
def step(pos, dir, stones, walls):
	if pos in walls:
		return (False, stones)
	elif pos in stones:
		(can, new_stones) = (step((pos[0]+dir[0], pos[1]+dir[1]), dir, stones, walls))
		if can:
			new_stones[stones.index(pos)] = (pos[0]+dir[0], pos[1]+dir[1])
			return (can, new_stones)
		else:
			return False, stones
	else:
		return (True, stones)

def part2(input):
	grid = []
	moves = []
	for line in input:
		if "#" in line:
			grid.append(line)
		elif line == "\n":
			continue
		else:
			moves.append(line)
		
	moves = "".join(moves)

	new_grid = []
	for r in range(len(grid)):
		row = ""
		for c in range(len(grid[0])):
			if grid[r][c] == "#":
				row += "##"
			elif grid[r][c] == 	"O":
				row += "[]"
			elif grid[r][c] == ".":
				row += ".."
			elif grid[r][c] == "@":
				row += "@."
		new_grid.append(row)
	grid = new_grid

	stones = []
	walls = set()
	robot = (-1,-1)
	for r in range(len(grid)):
		for c in range(len(grid[0])):
			if grid[r][c] == "[":
				stones.append((r,c,c+1))
			elif grid[r][c] == "#":
				walls.add((r,c))
			elif grid[r][c] == "@":
				robot = (r,c)

	for move in moves:
		(r,c) = robot
		if move == "<":
			(can, new_stones) = step_left((r,c-1), stones, walls)
			if can:
				robot = (r,c-1)
			stones = new_stones
		if move == "^":
			(can, new_stones) = step_up_down((r-1,c), (-1,0), stones, walls)
			if can:
				robot = (r-1,c)
			stones = new_stones
		if move == ">":
			(can, new_stones) = step_right((r,c+1), stones, walls)
			if can:
				robot = (r,c+1)
			stones = new_stones
		if move == "v":
			(can, new_stones) = step_up_down((r+1,c), (1,0), stones, walls)
			if can:
				robot = (r+1,c)
			stones = new_stones
	
	sum = 0
	for stone in stones:
		sum += stone[0]*100 + stone[1]
				
	return sum

def step_up_down(pos, dir, stones, walls):
	f_pos = (pos[0], pos[1], pos[1]+1)
	s_pos = (pos[0], pos[1]-1, pos[1])
	if pos in walls:
		return (False, stones)
	elif f_pos in stones:
		(can, new_stones) = step_up_down_stone((f_pos[0]+dir[0], f_pos[1]+dir[1]), dir, stones.copy(), walls)
		if can:
			new_stones[stones.index(f_pos)] = (f_pos[0]+dir[0], f_pos[1]+dir[1], f_pos[1]+dir[1]+1)
			return (can, new_stones)
		else:
			return False, stones
	elif s_pos in stones:
		(can, new_stones) = step_up_down_stone((s_pos[0]+dir[0], s_pos[1]+dir[1]), dir, stones.copy(), walls)
		if can:
			new_stones[stones.index(s_pos)] = (s_pos[0]+dir[0], s_pos[1]+dir[1], s_pos[1]+dir[1]+1)
			return (can, new_stones)
		else:
			return False, stones
	else:
		return (True, stones)

def step_up_down_stone(pos, dir, stones, walls):
	f_pos = (pos[0], pos[1], pos[1]+1)
	s_pos = (pos[0], pos[1]+1, pos[1]+2)
	t_pos = (pos[0], pos[1]-1, pos[1])
	if pos in walls or (pos[0], pos[1]+1) in walls:
		return (False, stones)
	elif t_pos in stones and s_pos in stones:
		(can, new_stones) = step_up_down_stone((t_pos[0]+dir[0], t_pos[1]+dir[1]), dir, stones.copy(), walls)
		if can:
			(can, new_stones) = step_up_down_stone((s_pos[0]+dir[0], s_pos[1]+dir[1]), dir, new_stones, walls)
			if can:
				new_stones[stones.index(t_pos)] = (t_pos[0]+dir[0], t_pos[1]+dir[1], t_pos[1]+dir[1]+1)
				new_stones[stones.index(s_pos)] = (s_pos[0]+dir[0], s_pos[1]+dir[1], s_pos[1]+dir[1]+1)
				return (can, new_stones)
		return False, stones

	elif f_pos in stones:
		(can, new_stones) = step_up_down_stone((f_pos[0]+dir[0], f_pos[1]+dir[1]), dir, stones.copy(), walls)
		if can:
			new_stones[stones.index(f_pos)] = (f_pos[0]+dir[0], f_pos[1]+dir[1], f_pos[1]+dir[1]+1)
			return (can, new_stones)
		else:
			return False, stones
	elif s_pos in stones:
		(can, new_stones) = step_up_down_stone((s_pos[0]+dir[0], s_pos[1]+dir[1]), dir, stones.copy(), walls)
		if can:
			new_stones[stones.index(s_pos)] = (s_pos[0]+dir[0], s_pos[1]+dir[1], s_pos[1]+dir[1]+1)
			return (can, new_stones)
		else:
			return False, stones
	elif t_pos in stones:
		(can, new_stones) = step_up_down_stone((t_pos[0]+dir[0], t_pos[1]+dir[1]), dir, stones.copy(), walls)
		if can:
			new_stones[stones.index(t_pos)] = (t_pos[0]+dir[0], t_pos[1]+dir[1], t_pos[1]+dir[1]+1)
			return (can, new_stones)
		else:
			return False, stones
	else:
		return (True, stones)

def step_left(pos, stones, walls):
	s_pos = (pos[0], pos[1]-1, pos[1])
	if pos in walls:
		return (False, stones)
	elif s_pos in stones:
		(can, new_stones) = step_left((s_pos[0], s_pos[1]-1), stones.copy(), walls)
		if can:
			new_stones[stones.index(s_pos)] = (s_pos[0], s_pos[1]-1, s_pos[2]-1)
			return (can, new_stones)
		else:
			return False, stones
	else:
		return (True, stones)

def step_right(pos, stones, walls):
	f_pos = (pos[0], pos[1], pos[1]+1)
	if pos in walls:
		return (False, stones)
	elif f_pos in stones:
		(can, new_stones) = step_right((f_pos[0], f_pos[1]+2), stones.copy(), walls)
		if can:
			new_stones[stones.index(f_pos)] = (pos[0], f_pos[1]+1, f_pos[2]+1)
			return (can, new_stones)
		else:
			return False, stones
	else:
		return (True, stones)

if __name__ == "__main__":
    sys.exit(main())