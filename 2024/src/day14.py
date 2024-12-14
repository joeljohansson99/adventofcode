import os
import sys
import re

def main():
    input = []
    
    with open(f'{os.path.dirname(os.path.realpath(__file__))}/../input/day14.txt') as f:
        for line in f.readlines():
            input.append(line.replace("\n",""))

    print("Part 1: " + str(part1(input)))
    print("Part 2: " + str(part2(input)))

def part1(input):
	MAX_ROW = 103
	MAX_COL = 101

	robots = []
	for line in input:
		[x,y,dx,dy] = list(map(int, re.findall(r'-?\d+', line)))
		robots.append((x,y,dx,dy))

	for _ in range(100):
		next_robots = []
		for robot in robots:
			(x,y,dx,dy) = robot
			yy = (y+dy) % MAX_ROW
			xx = (x+dx) % MAX_COL
			next_robots.append((xx,yy,dx,dy))

		robots = next_robots
	
	HALF_ROW = MAX_ROW // 2
	HALF_COL = MAX_COL // 2

	top_right = 0
	top_left = 0
	bot_right = 0
	bot_left = 0

	robot_posses = [(x,y) for (x,y,_,_) in robots]
	for y in range(MAX_ROW):
		for x in range(MAX_COL):
			if (x,y) not in robot_posses:
				continue

			if y < HALF_ROW and x < HALF_COL:
				top_left += robot_posses.count((x,y))
			elif y < HALF_ROW and x > HALF_COL:
				top_right += robot_posses.count((x,y))
			elif y > HALF_ROW and x < HALF_COL:
				bot_left += robot_posses.count((x,y))
			elif y > HALF_ROW and x > HALF_COL:
				bot_right += robot_posses.count((x,y))

	return top_left*top_right*bot_left*bot_right


def part2(input):
	MAX_ROW = 103
	MAX_COL = 101

	robots = []
	for line in input:
		[x,y,dx,dy] = list(map(int, re.findall(r'-?\d+', line)))
		robots.append((x,y,dx,dy))

	seconds = 0
	while not check(robots):
		next_robots = []
		for robot in robots:
			(x,y,dx,dy) = robot
			yy = (y+dy) % MAX_ROW
			xx = (x+dx) % MAX_COL
			next_robots.append((xx,yy,dx,dy))

		robots = next_robots
		seconds += 1
	
	return seconds



def check(robots):
	robot_posses = set([(x,y) for (x,y,_,_) in robots])
	count = 0
	for (x,y) in robot_posses:
		found = False
		for (dx,dy) in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
			if (dx, dy) in robot_posses:
				found = True
				break
		if found:
			count += 1
	
	return count > len(robot_posses) // 2

if __name__ == "__main__":
    sys.exit(main())