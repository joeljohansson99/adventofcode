package solutions;

import java.util.*;

import utils.Input;

public class Day7 implements Day {

	Input input;
	
	public Day7() {
		this.input = new Input(getClass().getResourceAsStream("/input/day7.txt"));
	}
	
	@Override
	public String part1() {
		List<String> strList = input.getList();
		
		Map<String,String> map = new HashMap<>();
		for (String s : strList) {
			String[] pair = s.split(" contain ");
			map.put(pair[0], pair[1]);
		}
		
		Set<String> found = new HashSet<>(contain("shiny gold bag", map));
		
		int size = 0;
		
		while (found.size() != size) {

			while (found.size() != size) {
				size = found.size();
				Set<String> tmp = new HashSet<>();
				for (String s : found) {
					tmp.addAll(contain(s.substring(s.length()-1).equals("s") ? s.substring(0, s.length()-1) : s, map));
				}
				found.addAll(tmp);
			}
		}
		
		return String.valueOf(found.size());
	}

	@Override
	public String part2() {
		List<String> strList = input.getList();
		
		Map<String,String> map = new HashMap<>();
		for (String s : strList) {
			String[] pair = s.split(" contain ");
			map.put(pair[0], pair[1]);
		}
		
		return String.valueOf(countBags("shiny gold bags", map));
	}
	
	private int countBags(String bag, Map<String,String>map) {
		for (Map.Entry<String, String> entry : map.entrySet()) {
			if (entry.getKey().equals(bag)) {
				String[] bags = entry.getValue().split(", ");
				int sum = 0;
				for (String b : bags) {
					if (b.startsWith("no")) {
						return 0;
					}
					sum += Integer.parseInt(b.substring(0,1)) + 
							Integer.parseInt(b.substring(0,1)) * 
							countBags(b.substring(b.length()-1).equals("s") ? b.substring(2) : b.substring(2) + "s", map);
				}
				return sum;
			}
		}
		return 1;
	}

	public List<String> contain(String s, Map<String,String>map) {
		List<String> ret = new ArrayList<>();
		for (Map.Entry<String, String> entry : map.entrySet()) {
			if (entry.getValue().contains(s)) {
				ret.add(entry.getKey());
			}
		}
		return ret;
	}
}
