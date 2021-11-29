package solutions;

import utils.Input;

public class Day11 implements Day {

	Input input;
	
	public Day11() {
		this.input = new Input("/home/joel/eclipse-workspace/AdventOfCode/input/day11.txt");
	}
	
	@Override
	public String part1() {
		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		char[][] grid = new char[strArr.length][strArr[0].length()];
		for (int i = 0; i < strArr.length; i++) {
			grid[i] = strArr[i].toCharArray();
		}
		
		boolean changed = true;
		while (changed) {
			changed = false;
			char[][] tmp = copy(grid);
			for (int r = 0; r < grid.length; r++) {
				for (int c = 0; c < grid[0].length; c++) {
					if (grid[r][c] == '#') {
						if (countAdjacent(grid, r, c, '#') >= 4) {
							tmp[r][c] = 'L';
							changed = true;
						}
					} else if (grid[r][c] == 'L') {
						if (countAdjacent(grid, r, c, '#') == 0) {
							tmp[r][c] = '#';
							changed = true;
						}
					}
				}
			}
			grid = tmp;
		}
		
		int count = 0;
		for (char[] t : grid) {
			for (char c : t) {
				if (c == '#') {
					count++;
				}
			}
		}
		return String.valueOf(count);
	}

	@Override
	public String part2() {
		String[] strArr = input.getArray();
		char[][] grid = new char[strArr.length][strArr[0].length()];
		for (int i = 0; i < strArr.length; i++) {
			grid[i] = strArr[i].toCharArray();
		}
		
		boolean changed = true;
		while (changed) {
			changed = false;
			char[][] tmp = copy(grid);
			for (int r = 0; r < grid.length; r++) {
				for (int c = 0; c < grid[0].length; c++) {
					if (grid[r][c] == '#') {
						if (countVisible(grid, r, c, '#') >= 5) {
							tmp[r][c] = 'L';
							changed = true;
						}
					} else if (grid[r][c] == 'L') {
						if (countVisible(grid, r, c, '#') == 0) {
							tmp[r][c] = '#';
							changed = true;
						}
					}
				}
			}
			grid = tmp;
		}
		
		int count = 0;
		for (char[] t : grid) {
			for (char c : t) {
				if (c == '#') {
					count++;
				}
			}
		}
		return String.valueOf(count);
	}
	
	private char[][] copy(char[][] grid) {
		char[][] ret = new char[grid.length][grid[0].length];
		for (int r = 0; r < grid.length; r++) {
			for (int c = 0; c < grid[0].length; c++) {
				ret[r][c] = grid[r][c];
			}
		}
		return ret;
	}

	private int countAdjacent(char[][] grid, int row, int col, char l) {
		int count = 0;
		for (int r = row - 1; r <= row + 1; r++) {
			for (int c = col - 1; c <= col + 1; c++) {
				if (r >= 0 && r < grid.length && c >= 0 && c < grid[0].length && !(r == row && c == col)) {
					if (grid[r][c] == l) {
						count++;
					}
				}
			}
		}
		return count;
	}
	
	private int countVisible(char[][] grid, int r, int c, char l) {
		int count = 0;
		boolean[] dirs = new boolean[8];
		for (int i = 1; i < grid.length; i++) {
			if (r-i >= 0 && grid[r-i][c] != '.' && !dirs[0]) {
				if (grid[r-i][c] == l) {
					count++;
				}
				dirs[0] = true;
			} if (r+i < grid.length && grid[r+i][c] != '.' && !dirs[1]) {
				if (grid[r+i][c] == l) {
					count++;
				}
				dirs[1] = true;
			} if (c-i >= 0 && grid[r][c-i] != '.' && !dirs[2]) {
				if (grid[r][c-i] == l) {
					count++;
				}
				dirs[2] = true;
			} if (c+i < grid[0].length && grid[r][c+i] != '.' && !dirs[3]) {
				if (grid[r][c+i] == l) {
					count++;
				}
				dirs[3] = true;
			} if (r+i < grid.length && c+i < grid[0].length && grid[r+i][c+i] != '.' && !dirs[4]) {
				if (grid[r+i][c+i] == l) {
					count++;
				}
				dirs[4] = true;
			} if (r+i < grid.length && c-i >= 0 && grid[r+i][c-i] != '.' && !dirs[5]) {
				if (grid[r+i][c-i] == l) {
					count++;
				}
				dirs[5] = true;
			} if (r-i >= 0 && c-i >= 0 && grid[r-i][c-i] != '.' && !dirs[6]) {
				if (grid[r-i][c-i] == l) {
					count++;
				}
				dirs[6] = true;
			} if (r-i >= 0 && c+i < grid[0].length && grid[r-i][c+i] != '.' && !dirs[7]) {
				if (grid[r-i][c+i] == l) {
					count++;
				}
				dirs[7] = true;
			}
		}
		return count;
	}
	
}