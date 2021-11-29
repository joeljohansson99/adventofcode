package solutions;

import utils.Input;

public class Day3 implements Day{
	
	Input input;
	
	public Day3() {
		this.input = new Input("/home/joel/eclipse-workspace/AdventOfCode/input/day3.txt");
	}
	
	@Override
	public String part1() {
		// List<String> strList = input.getList();
		// String[] strArr = input.getArray();
		
		return String.valueOf(countPath(1,3));
	}

	@Override
	public String part2() {
		// List<String> strList = input.getList();
		// String[] strArr = input.getArray();
		return String.valueOf(countPath(1,1)*countPath(1,3)*countPath(1,5)*countPath(1,7)*countPath(2,1));
	}
	
	long countPath(int r, int c) {
		String[] strArr = input.getArray();
		int count = 0;
		int k = 0;
		for (int i = r; i < strArr.length; i+=r) {
			k += c;

			if (strArr[i].length() <= k) {
				k = k - strArr[i].length();
			}
			if (strArr[i].charAt(k) == '#') {
				count++;
			}
		}
		return count;
	}

}
