package utils;

import java.io.*;
import java.util.*;

public class Input {
	List<String> strList;
	
	public Input(String path) {
		File file = new File(path);
		BufferedReader br;
		try {
			br = new BufferedReader(new FileReader(file));
		} catch (FileNotFoundException e) {
			System.out.println("ERROR Failed to load file: " + e.getMessage());
			return;
		} 
		
		this.strList = new ArrayList<>();
		String st;
		try {
			while ((st = br.readLine()) != null) { 
				strList.add(st);
			}
		} catch (IOException e) {
			System.out.println("ERROR Failed to read file: " + e.getMessage());
			e.printStackTrace();
			return;
		} 
	}
	
	public List<String> getList() {
		return strList;
	}
	
	public String[] getArray() {
		String[] strArr = new String[strList.size()];
		for (int i = 0; i < strList.size(); i++) {
			strArr[i] = strList.get(i);
		}
		return strArr;
	}
}
