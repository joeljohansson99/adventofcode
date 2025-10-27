package solutions;

import java.util.*;
import java.util.stream.Collectors;

import utils.Input;
import utils.TicketReader;

import java.awt.Point;


public class Day16 implements Day {

	Input input;
	
	public Day16() {
		this.input = new Input(getClass().getResourceAsStream("/input/day16.txt"));
	}
	
	@Override
	public String part1() {
		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		TicketReader tr = new TicketReader();
		List<Integer> invalid = new ArrayList<>();
		boolean reading = true;
		boolean checking = false;
		for (String s : strArr) {
			if (reading) {
				if (s.isBlank()) {
					reading = false;
					continue;
				}
				String[] values = s.split(": ");
				String cond = values[0];
				String[] range = values[1].split(" or ");
				String[] first = range[0].split("-");
				String[] second = range[1].split("-");
				tr.addCondition(cond, new Point(Integer.parseInt(first[0]), Integer.parseInt(first[1])),
									  new Point(Integer.parseInt(second[0]), Integer.parseInt(second[1])));
			} else {
				if (checking) {
					for (String value : s.split(",")) {
						int n = Integer.parseInt(value);
						if (!tr.check(n)) {
							invalid.add(n);
						}
					}
				} else {
					checking = s.startsWith("nearby");
				}
				
			}
		}
		
		long sum = 0;
		for (int n : invalid) {
			sum += n;
		}
		
		return String.valueOf(sum);
	}

	@Override
	public String part2() {
		String[] strArr = input.getArray();
		TicketReader tr = new TicketReader();
		List<String> valid = new ArrayList<>();
		String myTicket = "";
		boolean readingMine = false;
		boolean reading = true;
		boolean checking = false;
		for (String s : strArr) {
			if (reading) {
				if (s.isBlank()) {
					reading = false;
					continue;
				}
				String[] values = s.split(": ");
				String cond = values[0];
				String[] range = values[1].split(" or ");
				String[] first = range[0].split("-");
				String[] second = range[1].split("-");
				tr.addCondition(cond, new Point(Integer.parseInt(first[0]), Integer.parseInt(first[1])),
									  new Point(Integer.parseInt(second[0]), Integer.parseInt(second[1])));
			} else {
				if (checking) {
					boolean ok = true;
					for (String value : s.split(",")) {
						int n = Integer.parseInt(value);
						if (!tr.check(n)) {
							ok = false;
						}
					}
					if (ok) {
						valid.add(s);
					}
				} else {
					if (s.startsWith("your")) {
						readingMine = true;
					}
					else if (readingMine) {
						myTicket = s;
						readingMine = false;
					}
					checking = s.startsWith("nearby");
				}
				
			}
		}
		//tr.printConditions();
		
		List<String[]> splitted = valid.stream().map((s) -> s.split(",")).collect(Collectors.toList());
		List<List<String>> mapped = new ArrayList<>();
		List<String> conditions = tr.conditionsList().stream().collect(Collectors.toList());
		
		
		for (int i = 0; i < splitted.get(0).length; i++) {
			List<String> matches = new ArrayList<>();
			for (String c : conditions) {
				boolean match = true;
				for (int j = 0; j < valid.size(); j++) {
					if (!tr.matchSpecific(Integer.parseInt(splitted.get(j)[i]), c)) {
						match = false;
					}
				}
				if (match) {
					matches.add(c);
				}
			}
			mapped.add(matches);
		}
		
		filterMatches(mapped);
		
		String[] numbers = myTicket.split(",");
		long sum = 1;
		
		for (List<String> list : mapped) {
			if (list.get(0).startsWith("departure")) {
				sum *= Integer.parseInt(numbers[mapped.indexOf(list)]);
			}
		}
		
		return String.valueOf(sum);
	}
	
	private void filterMatches(List<List<String>> mapped) {
		boolean changed = true;
        while (changed) {
            changed = false;
            for (int i = 0; i < mapped.size(); i++) {
                if (mapped.get(i).size() == 1) {
                    for (int j = 0; j < mapped.size(); j++) {
                        if (j != i) {
                            int sizeBefore = mapped.get(j).size();
                            mapped.get(j).removeAll(mapped.get(i));
                            if (sizeBefore != mapped.get(j).size()) {
                                changed = true;
                            }
                        }
                    }
                }
            }
        }
		
	}

}