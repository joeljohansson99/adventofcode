package utils;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.stream.Collectors;

public class Input {
	List<String> lines;
	
	public Input(InputStream in) {
        if (in == null) {
            throw new IllegalArgumentException("Input stream is null — resource not found");
        }
        this.lines = new BufferedReader(
            new InputStreamReader(in, StandardCharsets.UTF_8)
        ).lines().collect(Collectors.toList());
	}
	
	public List<String> getList() {
		return lines;
	}
	
	public String[] getArray() {
		String[] strArr = new String[lines.size()];
		for (int i = 0; i < lines.size(); i++) {
			strArr[i] = lines.get(i);
		}
		return strArr;
	}
}
