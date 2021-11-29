package solutions;

import java.util.*;
import java.util.stream.Collectors;

import utils.*;

public class Day17 implements Day{
	
	Input input;
	
	public Day17() {
		this.input = new Input("/home/joel/eclipse-workspace/AdventOfCode/input/day17.txt");
	}

	@Override
	public String part1() {
		List<char[]> grid = input.getList().stream().map((s) -> s.toCharArray()).collect(Collectors.toList());
		// String[] strArr = input.getArray();
		Map<Point3d,Integer> cords = new HashMap<>();
		for (int y = 0; y < grid.size(); y++) {
			for (int x = 0; x < grid.get(0).length; x++) {
				if (grid.get(y)[x] == '#') cords.put(new Point3d(x,y,0), 0);
			}
		}
		for (int i = 0; i < 6; i++) {
			for (Point3d p : cords.keySet()) {
				cords.put(p, countActiveNeighbors(p, cords.keySet()));
			}
		}
		
		return String.valueOf(cords.size());
	}
	
	public String part2() {
		// List<String> strList = input.getList();
		//String[] strArr = input.getArray();
		
		return null;
	}
	
	public int countActiveNeighbors(Point3d p, Set<Point3d> other) {
		int count = 0;
		for (int x = p.getX()-1; x <= p.getX()+1; x++) {
			for (int y = p.getY()-1; y <= p.getY()+1; y++) {
				for (int z = p.getZ()-1; z <= p.getZ()+1; z++) {
					Point3d oth = new Point3d(x,y,z);
					if (other.contains(oth) && !oth.equals(p)) {
						count++;
					}
				}
			}
		}
		return count;
	}
	
	public Map<Point3d, Character> mapCopy(Map<Point3d, Character> map) {
		Map<Point3d, Character> copy = new HashMap<>();
		for (Map.Entry<Point3d, Character> e : map.entrySet()) {
			copy.put(e.getKey(), e.getValue());
		}
		return copy;
	}
}