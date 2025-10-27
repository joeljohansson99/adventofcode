package solutions;

import java.util.*;

import utils.Input;

public class Day13 implements Day {

	Input input;
	
	public Day13() {
		this.input = new Input(getClass().getResourceAsStream("/input/day13.txt"));
	}
	
	@Override
	public String part1() {
		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		String[] busses = strArr[1].split(",");
		long minTime = Long.parseLong(strArr[0]);
		long dif = Long.MAX_VALUE;
		long bestBus = 0;
		for (String bus : busses) {
			if (bus.equals("x")) {
				continue;
			}
			long id = Long.parseLong(bus);
			long time = 0;
			while (time < minTime) time += id;
			if (time-minTime < dif) {
				dif = time-minTime;
				bestBus = id;
			}
		}
		return String.valueOf(dif*bestBus);
	}

	@Override
	public String part2() {
		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		String[] busses = strArr[1].split(",");
		List<Long> remainders = new ArrayList<>();
		List<Long> ids = new ArrayList<>();
		
		long step = 0;
		for (String bus : busses) {
			step++;
			if (bus.equals("x")) continue;
			remainders.add(Long.parseLong(bus) - step + 1);
			ids.add(Long.parseLong(bus));
		}
		
		List<Long> numbers = new ArrayList<> ();
		long mod = 1;
		
		for (long l : ids) {
			mod*=l;
		}
		
		for (int i = 0; i < ids.size(); i++) {
			long b = remainders.get(i);
			long n = mod / ids.get(i);
			long x = inverse(n, ids.get(i));
			numbers.add(b*n*x);
		}
		
		
		long sum = numbers.stream()
				.mapToLong(Long::longValue)
				.sum();
		
		System.out.println(sum + " % " + mod);
		
		return String.valueOf(sum%mod);
	}
	
	private long inverse(long n, long m) {
		long k = 1;
		while ((n*k)%m != 1) k++;
		return k;
	}
}


