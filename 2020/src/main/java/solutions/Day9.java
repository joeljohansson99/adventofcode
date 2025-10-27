package solutions;

import java.util.ArrayList;
import java.util.List;

import utils.Input;

public class Day9 implements Day {

	Input input;
	
	public Day9() {
		this.input = new Input(getClass().getResourceAsStream("/input/day9.txt"));
	}
	
	@Override
	public String part1() {
		List<String> strList = input.getList();
		List<Long> numbers = new ArrayList<>();
		for (String s : strList) {
			numbers.add(Long.parseLong(s));
		}
		
		int k = 0;
		while (true) {
			boolean valid = false;
			for (int i = k; i < k+25; i++) {
				for (int j = k; j < k+25; j++) {
					if (numbers.get(i) + numbers.get(j) == numbers.get(k+25)) {
						valid = true;
					}
				}
			}
			if (!valid) {
				return String.valueOf(numbers.get(k+25));
			}
			k++;
		}
		
	}

	@Override
	public String part2() {
		List<String> strList = input.getList();
		List<Long> numbers = new ArrayList<>();
		for (String s : strList) {
			numbers.add(Long.parseLong(s));
		}
		
		for (int i = 0; i < numbers.size(); i++) {
			long sum = 0;
			long max = 0;
			long min = Long.MAX_VALUE;
			for (int k = i; k < numbers.size(); k++) {
				sum += numbers.get(k);
				if (max < numbers.get(k)) {
					max = numbers.get(k);
				}
				if (min > numbers.get(k)) {
					min = numbers.get(k);
				}
				if (sum == 2089807806) {
					return String.valueOf(min+max);
				} else if (sum > 2089807806) {
					break;
				}
			}
		}
		
		return null;
	}

}
