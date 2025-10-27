package solutions;

import java.util.*;

import utils.Input;

public class Day8 implements Day {

	Input input;
	
	public Day8() {
		this.input = new Input(getClass().getResourceAsStream("/input/day8.txt"));
	}
	
	@Override
	public String part1() {
		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		
		return String.valueOf(execute(strArr));
	}

	@Override
	public String part2() {
		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		for (int i = 0; i < strArr.length; i++) {
			if (strArr[i].substring(0,3).equals("nop")) {
				strArr[i] = "jmp" + strArr[i].substring(3);
				int n = executeTest(strArr);
				if (n != -1) {
					return String.valueOf(n);
				}
				strArr[i] = "nop" + strArr[i].substring(3);
			} else if (strArr[i].substring(0,3).equals("jmp")) {
				strArr[i] = "nop" + strArr[i].substring(3);
				int n = executeTest(strArr);
				if (n != -1) {
					return String.valueOf(n);
				}
				strArr[i] = "jmp" + strArr[i].substring(3);
			}
		}
		return null;
	}
	
	public int execute(String instr[]) {
		List<Integer> mem = new ArrayList<>();
		int pc = 0;
		int acc = 0;
		while (!mem.contains(pc) || pc == 0) {
			mem.add(pc);
			
			String[] pair = instr[pc].split(" ");
			String code = pair[0];
			int n = Integer.parseInt(pair[1]);
			
			if (code.equals("nop")) {
				pc+=1;
			} else if (code.equals("acc")) {
				acc+=n;
				pc+=1;
			} else if (code.equals("jmp")) {
				pc+=n;
			}
		}
		return acc;
	}
	
	public int executeTest(String instr[]) {
		List<Integer> mem = new ArrayList<>();
		int pc = 0;
		int acc = 0;
		while (pc < instr.length) {
			if (mem.contains(pc)) {
				return -1;
			}
			mem.add(pc);
			
			String[] pair = instr[pc].split(" ");
			String code = pair[0];
			int n = Integer.parseInt(pair[1]);
			
			if (code.equals("nop")) {
				pc+=1;
			} else if (code.equals("acc")) {
				acc+=n;
				pc+=1;
			} else if (code.equals("jmp")) {
				pc+=n;
			}
		}
		return acc;
	}

}
