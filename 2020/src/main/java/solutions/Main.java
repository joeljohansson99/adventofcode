package solutions;
public class Main {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.err.println("Usage: java solutions.Main <dayNumber>");
            System.exit(1);
        }

        String dayNumber = args[0];
        if (dayNumber.length() == 1) dayNumber = "0" + dayNumber; // handle single-digit days
        String className = "solutions.Day" + dayNumber;

        try {
            Class<?> clazz = Class.forName(className);
            Day day = (Day) clazz.getDeclaredConstructor().newInstance();

            String part1 = day.part1();
            String part2 = day.part2();

            if (part1 != null) {
                System.out.println("Part 1 : " + part1);
            } else {
                System.out.println("\nNull value received for part 1");
            }
            if (part2 != null) {
                System.out.println("Part 2 : " + part2);
            } else {
                System.out.println("\nNull value received for part 2");
            }

        } catch (ClassNotFoundException e) {
            System.err.println("❌ Could not find class: " + className);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}