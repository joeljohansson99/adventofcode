package solutions;

import java.util.*;

import utils.Input;

public class Day5 implements Day {

	Input input;
	
	public Day5() {
		this.input = new Input(getClass().getResourceAsStream("/input/day5.txt"));
	}
	
	@Override
	public String part1() {
		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		int maxId = 0;
		for (String s : strArr) {
			int row = 0;
			for (int i = 0; i < 7; i++) {
				if (s.charAt(i) == 'B') {
					row += Math.pow(2, 6-i);
				}
			}
			int col = 0;
			for (int i = 0; i < 3; i++) {
				if (s.charAt(7+i) == 'R') {
					col += Math.pow(2, 2-i);
				}
			}
			maxId = Math.max(maxId, row*8+col);
		}
		return String.valueOf(maxId);
	}

	@Override
	public String part2() {
		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		List<Integer> seats = new ArrayList<>();
		
		for (String s : strArr) {
			int row = 0;
			for (int i = 0; i < 7; i++) {
				if (s.charAt(i) == 'B') {
					row += Math.pow(2, 6-i);
				}
			}
			int col = 0;
			for (int i = 0; i < 3; i++) {
				if (s.charAt(7+i) == 'R') {
					col += Math.pow(2, 2-i);
				}
			}
			seats.add(row*8+col);
		}
		Collections.sort(seats);
		int prev = 0;
		for (int id : seats) {
			if (prev == id - 2) {
				return String.valueOf(id-1);
			}
			prev = id;
		}
		
		return null;
	}

}
