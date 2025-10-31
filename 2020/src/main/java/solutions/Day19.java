package solutions;

import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import utils.Input;

public class Day19 implements Day{
	
	Input input;
	
	public Day19() {
		this.input = new Input(getClass().getResourceAsStream("/input/day19.txt"));
	}

	@Override
	public String part1() {
		List<String> strList = input.getList();
		int idx = strList.indexOf("");
		
		List<String> ruleStrs = strList.subList(0, idx);
		List<String> words = strList.subList(idx+1, strList.size());
		Map<Integer, String> ruleStrMap = new HashMap<>();
		for (String ruleStr : ruleStrs) {
			String[] parts = ruleStr.split(":");
			ruleStrMap.put(Integer.valueOf(parts[0]), parts[1].trim());
		}

		int count = 0;
		for (String word : words) {
			Set<String> matches = parseRule2(word, 0, ruleStrMap);
			if (matches.contains("")) {
				count++;
			}
		}

		return String.valueOf(count);
	}

	@Override
	public String part2() {
		List<String> strList = input.getList();
		int idx = strList.indexOf("");
		
		List<String> ruleStrs = strList.subList(0, idx);
		List<String> words = strList.subList(idx+1, strList.size());
		Map<Integer, String> ruleStrMap = new HashMap<>();
		for (String ruleStr : ruleStrs) {
			String[] parts = ruleStr.split(":");
			int num = Integer.parseInt(parts[0]);
			String str = parts[1].trim();
			if (num == 8) {
				str = "42 | 42 8";
			} else if (num == 11) {
				str = "42 31 | 42 11 31";
			}
			ruleStrMap.put(num, str);
		}

		int count = 0;
		for (String word : words) {
			Set<String> matches = parseRule2(word, 0, ruleStrMap);
			if (matches.contains("")) {
				count++;
			}
		}

		return String.valueOf(count);
	}

	private Set<String> parseRule2(String word, int ruleNum, Map<Integer, String> ruleStrMap) {
		String ruleStr = ruleStrMap.get(ruleNum).trim();

		if ("".equals(word)) {
			return Set.of();
		}

		if (ruleStr.startsWith("\"")) {
			char c = ruleStr.charAt(1);
			if (word.length() != 0 && word.charAt(0) == c) {
				return Set.of(word.substring(1));
			}
			return new HashSet<>();
		}

		String[] sides = ruleStr.split("\\|");
		Set<String> matches = new HashSet<>();
		for (String side : sides) {
			String[] nums = side.trim().split("\\s+");
			switch (nums.length) {
				case 1 -> {
					matches.addAll(parseRule2(word, Integer.parseInt(nums[0]), ruleStrMap));
				}
				case 2 -> {
					Set<String> pmatches = parseRule2(word, Integer.parseInt(nums[0]), ruleStrMap);
					for (String match : pmatches) {
						matches.addAll(parseRule2(match, Integer.parseInt(nums[1]), ruleStrMap));
					}
				}
				default -> {
					Set<String> pmatches1 = parseRule2(word, Integer.parseInt(nums[0]), ruleStrMap);
					for (String match1 : pmatches1) {
						Set<String> pmatches2 = parseRule2(match1, Integer.parseInt(nums[1]), ruleStrMap);
						for (String match2 : pmatches2) {
							matches.addAll(parseRule2(match2, Integer.parseInt(nums[2]), ruleStrMap));
						}
					}
				}
			}
		}

		return matches;
	}
}
