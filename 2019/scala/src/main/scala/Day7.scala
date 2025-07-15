class Computer(val initMemory:Array[Int], val phase:Int) {
  
  var first = true
  var pc = 0
  var memory:Array[Int] = initMemory
  def process(input:Int):Int = {
      while (pc < memory.length && memory(pc) != 99) {
      var op = memory(pc) % 100
      var mode1 = (memory(pc)/100) % 10
      var mode2 = (memory(pc)/1000) % 10
      var mode3 = (memory(pc)/10000) % 10
      var ret = 0
      op match {
        case 1 => {
          val (i,j) = getValues()
          memory( memory(pc + 3)) = i + j
          pc += 4
        }
        case 2 => {
            val (i,j) = getValues()
            memory(memory(pc + 3)) = i * j
            pc += 4
        }
        case 3 => {
            if (first) {
                memory(memory(pc + 1)) = phase
                var first = false
            } else memory(memory(pc + 1)) = input
            pc += 2
        }
        case 4 => {var res = memory(memory(pc + 1)); pc += 2;return res}
        case 5 => {
          val (i,j) = getValues()
          if (i != 0) pc = j
          else pc += 3
        }
        case 6 => {
          val (i,j) = getValues()
          if (i == 0) pc = j
          else pc += 3
        }
        case 7 => {
          val (i,j) = getValues()
          memory(memory(pc + 3)) = if (i < j) 1 else  0
          pc += 4
        }
        case 8 => {
          val (i,j) = getValues()
          memory(memory(pc + 3)) = if (i == j) 1 else  0
          pc += 4
        }
        case 99 => {
          return 0
        }
        case _ => {println("Unknown Opcode: " + op); pc+=4}
      }
    }
    return 0
  }
  def getValues(): (Int,Int) = {
        var isPosModes = memory(pc).toString.substring(0,math.max(memory(pc).toString.length() - 2,0)).map(_ == '0')
        for (i <- 0 until 2 - isPosModes.length) isPosModes = true +: isPosModes
        val i = if (isPosModes(1)) memory(memory(pc + 1)) else memory(pc + 1)
        val j = if (isPosModes(0)) memory(memory(pc + 2)) else memory(pc + 2)
        (i,j)
      }

  def immediate(n:Int):Boolean = n == 1
}


object Day7 {
  val initMem = scala.io.Source.fromFile("data/data7.txt", "UTF-8").getLines.toVector(0).split(',').map(_.toInt).toArray

  def part1(): Unit = {
    var sum:Int = 0
    for (one <- 5 to 9;two <- 5 to 9; three <- 5 to 9; four <- 5 to 9; five <- 5 to 9) {
      val xs = Vector(one,two,three,four,five)
      if (xs == xs.distinct) {
        val amps = Array(
          new Computer(initMem,one),
          new Computer(initMem,two),
          new Computer(initMem,three),
          new Computer(initMem,four),
          new Computer(initMem,five)
        )
        var first = true
        var output:Int = 0
        var i = 0
          while(output != 0 || first) {
              output = amps(i).process(output)
              if (amps(i) == amps.last) {if (sum<output)sum=output;i=0}
              i+=1
              first = false
          }
      }
    }
    println(sum)
  }

  def part2(): Unit = {

  }

  def apply() = {
    println("SOLUTION DAY 7")
    println("Running part 1")
    part1()
    println("Running part 2")
    //part2()
  }
}