
import solutions.Day17;
import solutions.Day;

public class Main {
	
	static public void main(String[] args) {
		Day day = new Day17();
		String part1 = day.part1();
		String part2 = day.part2();
		if (part1 != null) {
			System.out.println("Part 1 : " + part1);
		} else {
			System.out.println("\nNull value recieved part 1");
		}
		if (part2 != null) {
			System.out.println("Part 2 : " + part2);
		} else {
			System.out.println("\nNull value recieved part 2");
		}
	}
}
