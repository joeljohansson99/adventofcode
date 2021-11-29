package solutions;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import utils.Input;

public class Day6 implements Day {

	Input input;
	
	public Day6() {
		this.input = new Input("/home/joel/eclipse-workspace/AdventOfCode/input/day6.txt");
	}
	
	@Override
	public String part1() {
		String[] strArr = input.getArray();
		
		int sum = 0;
		String group = "";
		for (int i = 0; i < strArr.length; i++) {
			group += strArr[i];
			if (strArr[i].isBlank() || i == strArr.length - 1) {
				char[] chars = group.toCharArray();
				Set<Character> charSet = new LinkedHashSet<Character>();
				for (char c : chars) {
				    charSet.add(c);
				}
				sum += charSet.size();
				group = "";
			}
		}
		
		return String.valueOf(sum);
	}

	@Override
	public String part2() {
		String[] strArr = input.getArray();
		
		int sum = 0;
		String group = "";
		for (int i = 0; i < strArr.length; i++) {
			group += strArr[i] + " ";
			if (strArr[i].isBlank() || i == strArr.length - 1) {
				String[] ans = group.split(" ");
				Set<Character> common = new HashSet<>();
				for (char c : ans[0].toCharArray()) {
					common.add(c);
				}
				for (int k = 1; k < ans.length; k++) {
					Set<Character> tmp = new HashSet<>();
					for (char c : ans[k].toCharArray()) {
						tmp.add(c);
					}
					common.retainAll(tmp);
				}
				sum += common.size();
				group = "";
			}
		}
		
		return String.valueOf(sum);
	}

}
