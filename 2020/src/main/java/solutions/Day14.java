package solutions;


import java.util.*;

import utils.Input;

public class Day14 implements Day {

	Input input;
	
	public Day14() {
		this.input = new Input(getClass().getResourceAsStream("/input/day14.txt"));
	}
	
	@Override
	public String part1() {
		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		String mask = "";
		Map<Long,Long> mem = new HashMap<>();
		String zeros = "000000000000000000000000000000000000";
		for (String s : strArr) {
			String[] pair = s.split(" = ");
			if (pair[0].equals("mask")) {
				mask = pair[1];
			} else {
				long index = Long.parseLong(pair[0].substring(s.indexOf("[") + 1, s.indexOf("]")));
				StringBuilder sb = new StringBuilder();
				String tmp = Long.toBinaryString(Long.parseLong(pair[1]));
				String value = zeros.substring(tmp.length()) + tmp;
				for (int i = 0; i < value.length(); i++) {
					sb.append(mask.charAt(i) == 'X' ? value.charAt(i) : mask.charAt(i));
				}
				mem.put(index, Long.parseLong(sb.toString(), 2));
			}
		}
		
		long sum = 0;
		
		for (Long l : mem.values()) {
			sum += l;
		}
		
		return String.valueOf(sum);
	}

	@Override
	public String part2() {
		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		String mask = "";
		Map<Long,Long> mem = new HashMap<>();
		String zeros = "000000000000000000000000000000000000";
		for (String s : strArr) {
			String[] pair = s.split(" = ");
			if (pair[0].equals("mask")) {
				mask = pair[1];
			} else {
				String tmp = Long.toBinaryString(Long.parseLong(pair[0].substring(s.indexOf("[") + 1, s.indexOf("]"))));
				String address = zeros.substring(tmp.length()) + tmp;
				StringBuilder sb = new StringBuilder();
				for (int i = 0; i < address.length(); i++) {
					sb.append(mask.charAt(i) == '0' ? address.charAt(i) : mask.charAt(i));
				}
				List<String> result = combinations(sb.toString());
				for (String key : result) {
					mem.put(Long.parseLong(key,2), Long.parseLong(pair[1]));
				}
			}
		}
		
		long sum = 0;
		
		for (Long l : mem.values()) {
			sum += l;
		}
		
		return String.valueOf(sum);
	}

	private List<String> combinations(String address) {
		List<String> res = new ArrayList<>();
		if (!address.contains("X")) {
			res.add(address);
			return res;
		}
		StringBuilder sb = new StringBuilder(address);
		for (int i = 0; i < address.length(); i++) {
			if (address.charAt(i) == 'X') {
				sb.setCharAt(i, '0');
				res.addAll(combinations(sb.toString()));
				sb.setCharAt(i, '1');
				res.addAll(combinations(sb.toString()));
				return res;
			}
		}
		return null;
	}
	
}