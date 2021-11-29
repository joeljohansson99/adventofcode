package utils;

import java.util.Set;

public class Point3d implements Point {
	int x;
	int y;
	int z;
	
	public Point3d(int x, int y, int z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}
	
	@Override
	public boolean equals(Object obj) {
		Point3d other = (Point3d) obj;
		return other.x == x && other.y == y && other.z == z;
	}
	
	@Override
    public int hashCode() {
		return z*(x+y);
	}
	
	public int getX() {
		return x;
	}

	public int getY() {
		return y;
	}

	public int getZ() {
		return z;
	}
	
}
