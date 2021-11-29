package solutions;

import java.util.*;
import java.util.Map.Entry;

import utils.Input;

public class Day15 implements Day {

	Input input;
	
	public Day15() {
		this.input = new Input("/home/joel/eclipse-workspace/AdventOfCode/input/day15.txt");
	}
	
	@Override
	public String part1() {
		// List<String> strList = input.getList();
		String[] strArr = input.getArray()[0].split(",");
		Map<Integer,Integer> map = new HashMap<>();
		
		int turn = 0;
		int lastSpoken = 0;
		
		for (String s : strArr) {
			turn++;
			lastSpoken = Integer.parseInt(s);
			map.put(lastSpoken, turn);
		}
		
		int newSpoken = lastSpoken;
		
		while (turn <= 2020) {
			lastSpoken = newSpoken;
			
			newSpoken = turn - map.getOrDefault(lastSpoken, turn);
			
			map.put(lastSpoken, turn);
			
			turn++;
		}
		
		return String.valueOf(lastSpoken);
	}

	@Override
	public String part2() {
		String[] strArr = input.getArray()[0].split(",");
		Map<Integer,Integer> map = new HashMap<>();
		
		int turn = 0;
		int lastSpoken = 0;
		
		for (String s : strArr) {
			turn++;
			lastSpoken = Integer.parseInt(s);
			map.put(lastSpoken, turn);
		}
		
		int newSpoken = lastSpoken;
		
		while (turn <= 30000000) {
			lastSpoken = newSpoken;
			
			newSpoken = turn - map.getOrDefault(lastSpoken, turn);
			
			map.put(lastSpoken, turn);
			
			turn++;
		}
		
		return String.valueOf(lastSpoken);
	}

}