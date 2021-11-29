package utils;

public class Point2d implements Point{
	
	private double x,y;
	
	public Point2d(double x, double y) {
		this.x = x;
		this.y = y;
	}
	
	public double getX() {
		return x;
	}
	
	public double getY() {
		return y;
	}
	
	public void move(double dx, double dy) {
		this.x = dx;
		this.y = dy;
	}
	
	public String toString() {
		return "x: " + x + " <==> y: " + y;
	}
}
