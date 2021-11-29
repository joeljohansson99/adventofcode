class Computer4(val initMemory:Array[Long]) {
  
  var pc = 0
  var relative = 0
  var memory:Array[Long] = initMemory
  for (i <- 0 to 10000) memory = memory :+ 0.toLong
  def process(input:Long):Long = {
      while (pc < memory.length) {
      var op = memory(pc) % 100
      var mod1 = memory(pc)/100 % 10
      var mod2 = memory(pc)/1000 % 10
      var mod3 = (memory(pc)/10000) % 10
      op match {
        case 1 => {
          val (i,j,k) = getValues()
          memory(k) = i+j
          pc += 4
        }
        case 2 => {
          val (i,j,k) = getValues()
          memory(k) = i*j
          pc += 4
        }
        case 3 => {
          if (isPos(mod1)) memory(memory(pc+1).toInt + relative) = input
          else if (immediate(mod1)) memory(pc+1) = input
          else memory(memory(pc+1).toInt) = input
          pc += 2
        }
        case 4 => {
          val (i,j,k) = getValues(1)
          pc += 2
          return (i)
        }
        case 5 => {
          val (i,j,k) = getValues(2)
          if (i != 0) pc = j.toInt
          else pc += 3
        }
        case 6 => {
          val (i,j,k) = getValues(2)
          if (i == 0) pc = j.toInt
          else pc += 3
        }
        case 7 => {
          val (i,j,k) = getValues()
          memory(k) = if (i < j) 1 else 0
          pc += 4
        }
        case 8 => {
          val (i,j,k) = getValues()
          memory(k) = if (i == j) 1 else 0
          pc += 4
        }
        case 9 => {
          val (i,j,k) = getValues(1)
          relative += i.toInt
          pc += 2
        }
        case 99 => {
          return 99
        }
        case _ => {println("Unknown Opcode: " + op); pc+=4}
      }
    }
    println("Got all the way")
    return -1
  }

  def getValues(l:Int = 3):(Long,Long,Int) = {
    var modes = memory(pc).toString.substring(0,math.max(memory(pc).toString.length() - 2,0)).map(_.toInt -48).toArray
    while(modes.length != 3) modes = 0 +: modes
    val i = if (modes(2) == 2) memory(memory(pc+1).toInt + relative) else if (modes(2) == 1) memory(pc+1) else memory(memory(pc+1).toInt)
    var j:Long = 0
    if (l > 1) j = if (modes(1) == 2) memory(memory(pc+2).toInt + relative) else if (modes(1) == 1) memory(pc+2) else memory(memory(pc+2).toInt)
    var k = 0
    if (l > 2) k = if (modes(0) == 2) (memory(pc+3).toInt + relative) else if (modes(0) == 1) pc+3 else memory(pc+3).toInt
    (i,j,k)
  }

  def immediate(n:Long):Boolean = n == 1
  def isPos(n:Long):Boolean = n == 2
}


case class Pos1(x:Int, y:Int) {
  def +(o:Pos1):Pos1 = Pos1(o.x+x,o.y+y)
  def -(o:Pos1):Pos1 = Pos1(x-o.x,y-o.y)
  def *(i:Int):Pos1 = Pos1(x*i,y*i)
}

case class Block(p:Pos1,c:Char)

object Day15 {
  val input = scala.io.Source.fromFile("data/data15.txt", "UTF-8").getLines.toVector(0).split(',').map(_.toLong).toArray
  val comp = new Computer4(input)
  var pos = Pos1(0,0)
  var positions:Set[(Pos1,Int)] = Set((pos,0))

  val UP = Pos1(0,-1)
  val DOWN = Pos1(0,1)
  val LEFT = Pos1(-1,0)
  val RIGHT = Pos1(1,0)

  def part1() = {
    recur()
  }

  def recur():Unit = {
    var i = 0
    while (i < 2000000) {
      val input = scala.util.Random.nextInt(4) + 1
      val output = comp.process(input)

      if (output == 2) {
        positions += ((nextPos(input),0))
        pos = nextPos(input)
      }
      else if (output == 1) {
        positions += ((nextPos(input),0))
        pos = nextPos(input)
      }
      else if (output == 0) {
        positions += ((nextPos(input),1))
      }
      i+=1
    }
    printBoard
  }

  def nextPos(n:Int):Pos1 = {
    n match {
      case 1 => pos + UP
      case 2 => pos + DOWN
      case 3 => pos + LEFT
      case 4 => pos + RIGHT
      case _ => pos
    }
  }
  def endState() {
    println("END")
    System.exit(1)
  }

  def printBoard():Unit = {
    var b = ""
    if (!positions.isEmpty) b = board
    print("\u001b[2J")
    if (!positions.isEmpty) println(b)
  }

  def board():String = {
    var sur = Array.fill(positions.map(_._1.y).max - positions.map(_._1.y).min + 1)(Array.fill(positions.map(_._1.x).max - positions.map(_._1.x).min + 1)(1))
    for (p <- positions) {
      sur(p._1.y - positions.map(_._1.y).min)(p._1.x - positions.map(_._1.x).min) = p._2
    }
    val start = Pos1(21,21)
    val finish = Pos1(39,39)
    val steps = findClosest(sur, finish.x,finish.y)
    sur.map(xs => xs.mkString).mkString("\n") + "\n" + steps
  }

   def findClosest(grid:Array[Array[Int]],x:Int, y:Int):Int = {
    grid(y)(x) = 2
    var i = -1
    var running = true

    while (running) {
      var copy:Array[Array[Int]] = Array.fill(grid.length)(Array.fill(grid(0).length)(0))
      for (r <- grid.indices) {
        for (c <- grid(0).indices) {
          copy(r)(c) = grid(r)(c)
        }
      }
      var oxy:Array[Pos1] = Array.empty
      for (r <- grid.indices) {
        for (c <- grid(0).indices) {
          if (grid(r)(c) == 2) {
            oxy :+= Pos1(c,r)
          }
        }
      }
      for (p <- oxy) {
        for (r <- p.y-1 to p.y+1) {
          for (c <- p.x-1 to p.x+1) {
            if (grid(r)(c) == 0) {
              if (r == p.y || c == p.x) grid(r)(c) = 2
            }
          }
        }
      }
      running = false
      for (r <- grid.indices) {
        for (c <- grid(0).indices) {
          if (copy(r)(c) != grid(r)(c)){
            running = true
          }
        }
      }
      i+=1
    }
    i
   }


  def part2(): Unit = {

  }

  def apply() = {
    println("SOLUTION DAY 15")
    println("Running part 1")
    part1()
    println("Running part 2")
    //part2()
  }
}