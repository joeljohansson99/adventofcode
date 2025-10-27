package solutions;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import utils.Input;

public class Day10 implements Day {

	Input input;
	
	public Day10() {
		this.input = new Input(getClass().getResourceAsStream("/input/day10.txt"));
	}
	
	@Override
	public String part1() {
		List<String> strList = input.getList();
		List<Integer> jolts = new ArrayList<>();
		for (String s : strList) {
			jolts.add(Integer.parseInt(s));
		}
		
		int rate = 0;
		int count1 = 0;
		int count3 = 0;
		while (!jolts.isEmpty()) {
			for (int i = 1; i < 4; i++) {
				if (jolts.remove(Integer.valueOf(i+rate))) {
					rate += i;
					if (i == 1) {
						count1++;
					} else if (i == 3) {
						count3++;
					}
					break;
				}
			}
		}
		count3++;
		return String.valueOf(count3*count1);
	}

	@Override
	public String part2() {
		List<String> strList = input.getList();
		List<Integer> jolts = new ArrayList<>();
		for (String s : strList) {
			jolts.add(Integer.parseInt(s));
		}
		List<List<Integer>> jumps = new ArrayList<>();
		
		int rate = 0;
		List<Integer> tmp = new ArrayList<>();
		tmp.add(0);
		while (!jolts.isEmpty()) {
			for (int i = 1; i < 4; i++) {
				if (jolts.remove(Integer.valueOf(i+rate))) {
					rate += i;
					if (i == 3) {
						jumps.add(tmp);
						tmp = new ArrayList<>();
					}
					tmp.add(rate);
					break;
				}
			}
		}
		jumps.add(tmp);
		
		long sum = 1;
		
		for (List<Integer> leaps : jumps) {
			sum *= countWays(leaps, Collections.min(leaps), Collections.max(leaps));
		}
		return String.valueOf(sum);
	}
	
	private long countWays(List<Integer> jolts, int rate, int max) {
		if (rate == max) {
			return 1;
		}
		long count = 0;
		for (int i = 1; i < 4; i++) {
			if (jolts.contains(rate+i)) {	
				count += countWays(jolts, rate+i, max);
			}
		}
		return count;
	}

}