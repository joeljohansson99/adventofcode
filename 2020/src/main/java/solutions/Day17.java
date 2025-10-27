package solutions;

import java.util.*;

import utils.*;

public class Day17 implements Day{
	
	Input input;
	
	public Day17() {
		this.input = new Input(getClass().getResourceAsStream("/input/day17.txt"));
	}

	@Override
	public String part1() {
		List<String> strList = input.getList();
		Set<Point3D> cubes = new HashSet<>();
		for (int y = 0; y < strList.size(); y++) {
			for (int x = 0; x < strList.get(y).length(); x++) {
				if (strList.get(y).charAt(x) == '#') {
					cubes.add(new Point3D(x, y, 0));
				}
			}
		}
		
		for (int i = 0; i < 6; i++) {
			Set<Point3D> checks = new HashSet<>();
			for (Point3D cube : cubes) {
				checks.add(cube);
				checks.addAll(cube.neighbours());
			}
			Set<Point3D> newCubes = new HashSet<>();
			for (Point3D cube : checks) {
				int count = 0;
				for (Point3D neigh : cube.neighbours()) {
					if (cubes.contains(neigh)) {
						count++;
					}
				}
				if (cubes.contains(cube)) {
					if (count >= 2 && count <= 3) {
						newCubes.add(cube);
					}
				} else {
					if (count == 3) {
						newCubes.add(cube);
					}
				}
			}
			cubes = newCubes;
		}

		return String.valueOf(cubes.size());
	}
	
	public String part2() {
		List<String> strList = input.getList();
		Set<Point4D> cubes = new HashSet<>();
		for (int y = 0; y < strList.size(); y++) {
			for (int x = 0; x < strList.get(y).length(); x++) {
				if (strList.get(y).charAt(x) == '#') {
					cubes.add(new Point4D(x, y, 0, 0));
				}
			}
		}
		
		for (int i = 0; i < 6; i++) {
			Set<Point4D> checks = new HashSet<>();
			for (Point4D cube : cubes) {
				checks.add(cube);
				checks.addAll(cube.neighbours());
			}
			Set<Point4D> newCubes = new HashSet<>();
			for (Point4D cube : checks) {
				int count = 0;
				for (Point4D neigh : cube.neighbours()) {
					if (cubes.contains(neigh)) {
						count++;
					}
				}
				if (cubes.contains(cube)) {
					if (count >= 2 && count <= 3) {
						newCubes.add(cube);
					}
				} else {
					if (count == 3) {
						newCubes.add(cube);
					}
				}
			}
			cubes = newCubes;
		}

		return String.valueOf(cubes.size());
	}

	private record Point3D(int x, int y, int z) {
		private Set<Point3D> neighbours() {
			Set<Point3D> neighs = new HashSet<>();
			for (int dx = x-1; dx <= x+1; dx++) {
				for (int dy = y-1; dy <= y+1; dy++) {
					for (int dz = z-1; dz <= z+1; dz++) {
						if (dx != x || dy != y || dz != z) {
							neighs.add(new Point3D(dx, dy, dz));
						}
					}
				}
			}
			return neighs;
		}
	}

	private record Point4D(int x, int y, int z, int w) {
		private Set<Point4D> neighbours() {
			Set<Point4D> neighs = new HashSet<>();
			for (int dx = x-1; dx <= x+1; dx++) {
				for (int dy = y-1; dy <= y+1; dy++) {
					for (int dz = z-1; dz <= z+1; dz++) {
						for (int dw = w-1; dw <= w+1; dw++) {
							if (dx != x || dy != y || dz != z || dw != w) {
								neighs.add(new Point4D(dx, dy, dz, dw));
							}
						}
					}
				}
			}
			return neighs;
		}
	}
}