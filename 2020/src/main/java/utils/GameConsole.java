package utils;

public class GameConsole {
	
	private String[] mem;
	private int pc = 0;
	private int acc = 0;
	
	public GameConsole(String[] mem) {
		this.mem = mem;
	}
	
	public void execute() {
		while (pc < mem.length) {
			
			String[] pair = mem[pc].split(" ");
			String code = pair[0];
			int n = Integer.parseInt(pair[1]);
			
			switch (code) {
			
			case "nop":
				pc++;
				break;
				
			case "acc":
				pc++;
				acc+=n;
				break;
				
			case "jmp":
				pc+=n;
				break;
				
			default:
				
			}
		}
	}
	
	public int getAcc() {
		return acc;
	}
	
	public int getPc() {
		return pc;
	}
}
