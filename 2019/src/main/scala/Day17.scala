import scala.collection.mutable.Queue

class Computer5(val initMemory:Array[Long]) {
  
  var pc = 0
  var relative = 0
  var memory:Array[Long] = initMemory
  var last:Long = 0
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
          last = i
          print(i.toChar)
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

object Day17 {
  val input = scala.io.Source.fromFile("data/data17.txt", "UTF-8").getLines.toVector.mkString.split(",").toArray.map(_.toLong)
  
  var gridLength = 0
  def part1(): Unit = {
    val comp = new Computer5(input)
    var output = 0
    var grid:Array[Char] = Array.empty
    var i = 1
    while (output != 99) {
      output = comp.process(Queue(1)).toInt
      if (output != 99) {
        grid :+= output.toChar
      }
      i+=1
    }
    gridLength = grid.indexOf('\n') + 1
    val intersections = countIntersect(grid)

    // intersections.foreach(p => grid(p.x + p.y*gridLength) = 'X')
    println(grid.mkString)
    println(intersections.map(p => p.x *p.y).sum)
    
  }

  case class Posit(y:Int, x:Int)

  def countIntersect(grid:Array[Char]):Array[Posit] = {
    var intersects: Array[Posit] = Array.empty
    for (i <- grid.indices) {
      if (i > gridLength) {
        if (grid(i) == '#' && grid(i-1) == '#' && grid(i+1) == '#' 
            && grid(i-gridLength) == '#' && grid(i+gridLength) == '#') {
          intersects :+= Posit(i/gridLength, i % gridLength)
        }
      }
    }
    intersects
  }

  def part2(): Unit = {
    val comp = new Computer5(input)
    var mainRut = "A,C,A,C,B,C,B,A,C,B\n"

    var a = "R,4,R,1,9,R,8,R,4\n"
    var b = "R,4,L,9,3,R,6,L,9,3\n"
    var c = "R,9,1,R,6,R,4\n"

    /* Did following in REPL

    var all:Vector[String] = "R,4,R,10,R,8,R,4,R,10,R,6,R,4,R,4,R,10,R,8,R,4,R,10,R,6,R,4,R,4,L,12,R,6,L,12,R,10,R,6,R,4,R,4,L,12,R,6,L,12,R,4,R,10,R,8,R,4,R,10,R,6,R,4,R,4,L,12,R,6,L,12".split(",").toVector
    /*                       |       A        |      C     |        A       |      C     |        B        |      C     |        B        |        A       |      C     |        B        |                    */
    var comb = (2 to 10).map(all.sliding(_).toVector).flatten
    comb.combinations(3).find(p => all.mkString.replaceAll(p(0).mkString, "").replaceAll(p(1).mkString,"").replaceAll(p(2).mkString, "") == "").get.foreach(println)

    */
    var video = "y\n"
    var queue:Queue[Long] = Queue.empty
    comp.memory(0) = 2
    (mainRut+a+b+c+video).toCharArray.foreach(s => queue += s.toLong)
    println(comp.process(queue))
    println(comp.last)
  }

  def apply() = {
    println("SOLUTION DAY 17")
    println("Running part 1")
    part1()
    println("Running part 2")
    part2()
  }
}