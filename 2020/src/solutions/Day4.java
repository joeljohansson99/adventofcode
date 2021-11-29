package solutions;

import utils.Input;
import java.util.*;

public class Day4 implements Day {

	Input input;
	
	public Day4() {
		this.input = new Input("/home/joel/eclipse-workspace/AdventOfCode/input/day4.txt");
	}
	
	@Override
	public String part1() {
		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		List<String> ids = new ArrayList<>();
		for (String s : strArr) {
			ids.addAll(Arrays.asList(s.split(" ")));
		}
		
		var sum = 0;
		var count = 0;
		for (String s : ids) {
			if (s.isBlank()) {
				count = 0;
			}
			else if (!s.startsWith("cid")){
				count++;
			}
			if (count >= 7) {
				sum++;
				count = 0;
			}
		}
		return String.valueOf(sum);
	}

	@Override
	public String part2() {
		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		List<String> ids = new ArrayList<>();
		for (String s : strArr) {
			ids.addAll(Arrays.asList(s.split(" ")));
		}
		int count = 0;
		int sum = 0;
		for (String s : ids) {
			if (s.isBlank()) {
				count = 0;
			}
			else if (check(s)){
				count++;
			}
			if (count >= 7) {
				sum++;
				count = 0;
			}
		}
		
		return String.valueOf(sum);
	}
	
	private boolean check(String s) {
		switch(s.substring(0, 3)) {
			case ("byr"): 
				int birth = Integer.parseInt(s.split(":")[1]);
				return birth >= 1920 && birth <= 2002;
			case ("iyr"): 
				int issue = Integer.parseInt(s.split(":")[1]);
				return issue >= 2010 && issue <= 2020;
			case ("eyr"): 
				int exp = Integer.parseInt(s.split(":")[1]);
				return exp >= 2020 && exp <= 2030;
			case ("hgt"):
				String hgt = s.split(":")[1];
				if (hgt.length() < 3) {
					return false;
				}
				if (hgt.substring(hgt.length()-2).contentEquals("cm")) {
					if (hgt.length() <= 4) {
						return false;
					}
					int cm = Integer.parseInt(hgt.substring(0,3));
					return cm >= 150 && cm <= 193;
				} else if (hgt.substring(hgt.length()-2).contentEquals("in")) {
					int in = Integer.parseInt(hgt.substring(0,2));
					return in >= 59 && in <= 76; 
				}
				return false;
			case ("hcl"):
				String hcl = s.split(":")[1];
				return hcl.startsWith("#") && hcl.length() == 7;
			case ("ecl"): 
				String ecl = s.split(":")[1];
				String[] arr = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"};
				for (String t : arr) {
					if (t.contentEquals(ecl)) {
						return true;
					}
				}
				return false;
			case ("pid"): 
				try {
					int pid = Integer.parseInt(s.split(":")[1]);
					return s.split(":")[1].length() == 9;
				} catch(NumberFormatException e) {
					return false;
				}
			default:
				return false;
		}
	}
	
}
