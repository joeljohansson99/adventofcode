package solutions;

import java.util.*;
import utils.*;

public class Day2 implements Day{
	
	Input input;
	
	public Day2() {
		this.input = new Input("/home/joel/eclipse-workspace/AdventOfCode/input/day2.txt");
	}

	@Override
	public String part1() {
		
		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		
		int sum = 0;
		for (String s : strArr) {
			String[] splitted = s.split(":");
			String[] info = splitted[0].split("-");
			int lower = Integer.parseInt(info[0]);
			String[] other = info[1].split(" ");
			int higher = Integer.parseInt(other[0]);
			char letter = other[1].toCharArray()[0];
			int count = 0;
			for (char c : splitted[1].toCharArray()) {
				if (c == letter) {
					count++;
				}
			}
			if (count >= lower && count <= higher) {
				sum++;
			}
		}
		
		return String.valueOf(sum);
	}
		
	public String part2() {

		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		
		int sum = 0;
		for (String s : strArr) {
			String[] splitted = s.split(":");
			String[] info = splitted[0].split("-");
			int i1 = Integer.parseInt(info[0]);
			String[] other = info[1].split(" ");
			int i2 = Integer.parseInt(other[0]);
			char letter = other[1].toCharArray()[0];
			String word = splitted[1].substring(1);
			
			if (word.charAt(i1-1) == letter ^ word.charAt(i2-1) == letter) {
				sum++;
			}
		}
		
		return String.valueOf(sum);
	}
		
		
	}