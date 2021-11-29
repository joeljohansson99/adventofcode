package solutions;

import utils.*;

public class Day12 implements Day {

	Input input;
	
	public Day12() {
		this.input = new Input("/home/joel/eclipse-workspace/AdventOfCode/input/day12.txt");
	}
	
	@Override
	public String part1() {
		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		Point2d loc = new Point2d(0,0);
		Point2d dir = new Point2d(1,0);
		
		for (String s : strArr) {
			double n = Integer.parseInt(s.substring(1));
			switch (s.charAt(0)) {
			case 'N':
				loc.move(loc.getX(), loc.getY()+n);
				break;
			case 'S':
				loc.move(loc.getX(), loc.getY()-n);
				break;
			case 'E':
				loc.move(loc.getX()+n, loc.getY());
				break;
			case 'W':
				loc.move(loc.getX()-n, loc.getY());
				break;
			case 'L':
				n = Math.toRadians(n);
				double lX = dir.getX() * Math.cos(n) - dir.getY() * Math.sin(n);
				double lY = dir.getX() * Math.sin(n) + dir.getY() * Math.cos(n);
				dir.move(lX,lY);
				break;
			case 'R':
				n = Math.toRadians(n);
				double rX = dir.getX() * Math.cos(n) + dir.getY() * Math.sin(n);
				double rY =  - dir.getX() * Math.sin(n) + dir.getY() * Math.cos(n);
				dir.move(rX,rY);
				break;
			case 'F':
				loc.move(loc.getX() + dir.getX()*n, loc.getY() + dir.getY()*n);
				break;
			}
		}
		
		return String.valueOf(Math.abs(loc.getX()) + Math.abs(loc.getY()));
	}

	@Override
	public String part2() {
		// List<String> strList = input.getList();
		String[] strArr = input.getArray();
		Point2d loc = new Point2d(0,0);
		Point2d way = new Point2d(10,1);
		
		for (String s : strArr) {
			double n = Integer.parseInt(s.substring(1));
			switch (s.charAt(0)) {
			case 'N':
				way.move(way.getX(), way.getY()+n);
				break;
			case 'S':
				way.move(way.getX(), way.getY()-n);
				break;
			case 'E':
				way.move(way.getX()+n, way.getY());
				break;
			case 'W':
				way.move(way.getX()-n, way.getY());
				break;
			case 'L':
				n = Math.toRadians(n);
				double lX = way.getX() * Math.cos(n) - way.getY() * Math.sin(n);
				double lY = way.getX() * Math.sin(n) + way.getY() * Math.cos(n);
				way.move(lX,lY);
				break;
			case 'R':
				n = Math.toRadians(n);
				double rX = way.getX() * Math.cos(n) + way.getY() * Math.sin(n);
				double rY =  - way.getX() * Math.sin(n) + way.getY() * Math.cos(n);
				way.move(rX,rY);
				break;
			case 'F':
				loc.move(loc.getX() + way.getX()*n, loc.getY() + way.getY()*n);
				break;
			}
		}
		
		return String.valueOf(Math.abs(loc.getX()) + Math.abs(loc.getY()));
	}

}