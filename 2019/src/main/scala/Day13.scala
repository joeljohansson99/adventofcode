class Computer3(val initMemory:Array[Long]) {
  
  var pc = 0
  var relative = 0
  var memory:Array[Long] = initMemory
  memory(0) = 2
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

case class Pos(x:Int,y:Int){
  def ==(o:Pos):Boolean = {o.x == x && o.y == y}
  def *(n:Int): Pos = Pos(x*n,y*n)
}

case class Tiles(pos:Pos, var id:Int) {
  var dir = Pos(1,-1)
  def update(other:Array[Tiles]): Unit =  {
    id match {
      case 2 => if (other.count(_.id == 4) > 0){if (pos == other.filter(_.id == 4)(0).pos) id = 0}
      case 4 => {
        if (other.map(_.pos).contains(Pos(pos.x + dir.x, pos.y))) {
          dir = Pos(dir.x * -1, dir.y)
        }
        if (other.filter(_.id != 0).map(_.pos).contains(Pos(pos.x, pos.y + dir.y))) {
          dir = Pos(dir.x, dir.y * -1)
        }
      }
      case _ => 
    }
  }
}

object Day13 {
  val input = scala.io.Source.fromFile("data/data13.txt", "UTF-8").getLines.toVector.mkString.split(',').map(_.toLong).toArray

  def part1(): Unit = {
    var grid:Array[Tiles] = Array.empty
    val comp = new Computer3(input)
    var i = 0
    var score = 0
    var outputs:Array[Long] = Array.empty
    def getDir():Int = {
      if (grid.filter(_.id == 4)(0).pos.x > grid.filter(_.id == 3)(0).pos.x) {
        1
      }
      else if (grid.filter(_.id == 4)(0).pos.x > grid.filter(_.id == 3)(0).pos.x) {
        -1
      }
      else 0
    }
    while (i == 0 || outputs.last != 99) {
      outputs :+= comp.process{
        if (grid.count(_.id == 3) > 0 &&
            grid.count(_.id == 4) > 0) getDir() else 0
      }

      i+=1

      if (i % 3 == 0) {
        val cord = outputs.reverse.take(3).reverse.map(_.toInt)
        if (cord(0) == -1 && cord(1) == 0) {score = cord(2);println("Score: " + score)}
        else {
          cord(2) match {
            case 0 => {grid :+= Tiles(Pos(cord(0), cord(1)), 0);println("Empty block created")}
            case 1 => {grid :+= Tiles(Pos(cord(0), cord(1)), 1);println("Wall created")}
            case 2 => {grid :+= Tiles(Pos(cord(0), cord(1)), 2);println("Block created")}
            case 3 => {grid :+= Tiles(Pos(cord(0), cord(1)), 3);println("Paddle created")}
            case 4 => {grid :+= Tiles(Pos(cord(0), cord(1)), 4);println("Ball created")}
          }
        }
      }
      grid.foreach(b => b.update(grid.filter(_ != b)))
    }
    println(score)
  }

  def part2(): Unit = {

  }

  def apply() = {
    println("SOLUTION DAY 13")
    println("Running part 1")
    part1()
    println("Running part 2")
    //part2()
  }
}