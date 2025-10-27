package utils;

import java.util.*;
import java.awt.Point;

public class TicketReader {

	Map<String, Map.Entry<Point, Point>> conditions = new HashMap<>();
	
	public TicketReader() {};
	
	public void addCondition(String cond, Point p1, Point p2) {
		this.conditions.put(cond, Map.entry(p1, p2));
	}
	
	public boolean check(int n) {
		for (Map.Entry<Point, Point> range : conditions.values()) {
			if (range.getKey().x <= n && range.getKey().y >= n) {
				return true;
			} else if (range.getValue().x <= n && range.getValue().y >= n) {
				return true;
			}
		}
		return false;
	}
	
	public void printConditions() {
		for (String key : conditions.keySet()) {
			Map.Entry<Point, Point> range = conditions.get(key);
			System.out.println(
				key + ": " + range.getKey().x + "-" + range.getKey().y +
				" or " + range.getValue().x + "-" + range.getValue().y
			);
		}
	}
	
	public boolean matchSpecific(int n, String key) {
		Map.Entry<Point, Point> range = conditions.get(key);
		if (range.getKey().x <= n && range.getKey().y >= n) {
			return true;
		} else if (range.getValue().x <= n && range.getValue().y >= n) {
			return true;
		}
		return false;
	}

	public List<String> conditionsList(){
		return new ArrayList<>(conditions.keySet());
	}
}
