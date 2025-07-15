import scala.collection.mutable.Queue

class Computer6() {
  
  var pc = 0
  var relative = 0
  var memory: Array[Long] = scala.io.Source.fromFile("data/data19.txt", "UTF-8").getLines.toVector.mkString.split(",").toArray.map(_.toLong)
  for (i <- 0 to 10000) memory = memory :+ 0.toLong

  def process(input:Queue[Long]):Long = {
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
          if (isPos(mod1)) memory(memory(pc+1).toInt + relative) = input.dequeue()
          else if (immediate(mod1)) memory(pc+1) = input.dequeue()
          else memory(memory(pc+1).toInt) = input.dequeue()
          pc += 2
        }
        case 4 => {
          val (i,j,k) = getValues(1)
          pc += 2
          return i
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
        // case 99 => {
        //   return 0
        // }
        case _ => {println("Unknown Opcode: " + op); pc+=4}
      }
    }
    println("Got all the way")
    return 0
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

object Day19 {
  val input = scala.io.Source.fromFile("data/data19.txt", "UTF-8").getLines.toVector.mkString.split(",").toArray.map(_.toLong)

  def part1(): Unit = {
    var area:Array[Array[Int]] = Array.fill(50)(Array.fill(50)(0))
    for (r <- 0 to 49; c <- 0 to 49) {
      val comp = new Computer6
      area(r)(c) = comp.process(Queue(r,c)).toInt
    }
    println(area.map(_.mkString).mkString("\n"))
    println(area.map(x => x.count(_ == 1)).sum)
  }

  def checkPos(x: Int, y: Int): Boolean = {
    val comp = new Computer6()
    comp.process(Queue(x, y)) == 1
  }

  def part2(): Unit = {
    var found = false
    var startY = 1650
    while(!found) {
      var startX = startY+150
      while (!checkPos(startX,startY)) startX += 1
      println(s"CHECKING X = $startX Y = $startY")
      if (checkPos(startX + 99, startY - 99)) {println(s"X = $startX Y = ${startY-99}"); found = true}
      startY += 1
    }
  }

  def apply() = {
    println("SOLUTION DAY 19")
    println("Running part 1")
    // part1()
    println("Running part 2")
    part2()
  }
}