package solutions;

import java.text.StringCharacterIterator;
import java.util.ArrayList;
import java.util.List;

import utils.Input;

public class Day18 implements Day {
	
	Input input;
	
	public Day18() {
		this.input = new Input(getClass().getResourceAsStream("/input/day18.txt"));
	}

	@Override
	public String part1() {
		List<String> lines = input.getList();
		long sum = 0;
		for (String line : lines) {
			sum += parse(new StringCharacterIterator(line.replaceAll("\\s+", ""))).eval();
		}

		return String.valueOf(sum);
	}

	@Override
	public String part2() {
		List<String> lines = input.getList();
		long sum = 0;
		for (String line : lines) {
			sum += parse2(new StringCharacterIterator(line.replaceAll("\\s+", ""))).eval();
		}

		return String.valueOf(sum);
	}

	private Expr parse(StringCharacterIterator it) {
		Expr expr = new NumExpr(0);
		char op = '+';
    	for (char c = it.current(); c != StringCharacterIterator.DONE; c = it.next()) {
			if (c == '+' || c == '*') op = c;
			else if (c == '(') {
				it.next();
				expr = applyOp(expr, op, parse(it));
			}
			else if (c == ')') break;
			else expr = applyOp(expr, op, new NumExpr(Character.getNumericValue(c)));
		}
		return expr;
	}

	private Expr parse2(StringCharacterIterator it) {
		List<Expr> addExprs = new ArrayList<>();
		char op = '*';
    	for (char c = it.current(); c != StringCharacterIterator.DONE; c = it.next()) {
			if (c == '+' || c == '*') op = c;
			else if (c == '(') {
				it.next();
				if (op == '+') {
					addExprs.add(applyOp(addExprs.removeLast(), op, parse2(it)));
				} else {
					addExprs.add(parse2(it));
				}
			}
			else if (c == ')') break;
			else {
				if (op == '+') {
					addExprs.add(applyOp(addExprs.removeLast(), op, new NumExpr(Character.getNumericValue(c))));
				} else {
					addExprs.add(new NumExpr(Character.getNumericValue(c)));
				}
			}
		}
		Expr base = new NumExpr(1);
		for (Expr exp : addExprs) {
			base = new MulExpr(base, exp);
		}	
		return base;
	}

	private Expr applyOp(Expr left, char op, Expr right) {
		return op == '+' ? new AddExpr(left, right) : new MulExpr(left, right);
	}

	sealed interface Expr permits AddExpr, MulExpr, NumExpr {
		long eval();
	}

	private final class AddExpr implements Expr {
		private Expr left;
		private Expr right;

		public AddExpr(Expr left, Expr right) {
			this.left = left;
			this.right = right;
		}

		@Override
		public long eval() {
			return left.eval() + right.eval();
		}
	}

	private final class MulExpr implements Expr {
		private Expr left;
		private Expr right;

		public MulExpr(Expr left, Expr right) {
			this.left = left;
			this.right = right;
		}

		@Override
		public long eval() {
			return left.eval() * right.eval();
		}
	}

	private final class NumExpr implements Expr {
		private long val;

		public NumExpr(long val) {
			this.val = val;
		}

		@Override
		public long eval() {
			return val;
		}
	}
}
