package solutions;

import utils.*;

public class Day1 implements Day{
	
	Input input;
	
	public Day1() {
		this.input = new Input(getClass().getResourceAsStream("/input/day1.txt"));
	}

	@Override
	public String part1() {
		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		
		int[] intArr = new int[strArr.length];
		for (int i=0; i<strArr.length; i++) {
			intArr[i] = Integer.parseInt(strArr[i]);
		}
		
		for (int i = 0; i < intArr.length; i++) {
			for (int k = 0; k < intArr.length; k++) {
				if (intArr[i] + intArr[k] == 2020) {
					return String.valueOf(intArr[i] * intArr[k]);
				}
			}
		}
		
		return null;
	}
	
	public String part2() {

		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		
		int[] intArr = new int[strArr.length];
		for (int i=0; i<strArr.length; i++) {
			intArr[i] = Integer.parseInt(strArr[i]);
		}
		
		for (int i = 0; i < intArr.length; i++) {
			for (int k = 0; k < intArr.length; k++) {
				for (int l = 0; l < intArr.length; l++) {
					if (intArr[i] + intArr[k] + intArr[l] == 2020) {
						return String.valueOf(intArr[i] * intArr[k] * intArr[l]);
					}
				}
			}
		}
		return null;
	}
	
	
}
