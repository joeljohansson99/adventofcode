// import scala.collection.mutable.Map

// class Computer2(val initMemory:Array[Long]) {
  
//   var pc = 0
//   var relative = 0

//   var memory:Array[Long] = initMemory
//   for (i <- 0 to 10000) memory = memory :+ 0.toLong
//   def process(input:Long):Long = {
//       while (pc < memory.length) {
//       var op = memory(pc) % 100
//       var mod1 = memory(pc)/100 % 10
//       var mod2 = memory(pc)/1000 % 10
//       var mod3 = (memory(pc)/10000) % 10
//       op match {
//         case 1 => {
//           val (i,j,k) = getValues()
//           memory(k) = i+j
//           pc += 4
//         }
//         case 2 => {
//           val (i,j,k) = getValues()
//           memory(k) = i*j
//           pc += 4
//         }
//         case 3 => {
//           if (isPos(mod1)) memory(memory(pc+1).toInt + relative) = input
//           else if (immediate(mod1)) memory(pc+1) = input
//           else memory(memory(pc+1).toInt) = input
//           pc += 2
//         }
//         case 4 => {
//           val (i,j,k) = getValues(1)
//           pc += 2
//           return (i)
//         }
//         case 5 => {
//           val (i,j,k) = getValues(2)
//           if (i != 0) pc = j.toInt
//           else pc += 3
//         }
//         case 6 => {
//           val (i,j,k) = getValues(2)
//           if (i == 0) pc = j.toInt
//           else pc += 3
//         }
//         case 7 => {
//           val (i,j,k) = getValues()
//           memory(k) = if (i < j) 1 else 0
//           pc += 4
//         }
//         case 8 => {
//           val (i,j,k) = getValues()
//           memory(k) = if (i == j) 1 else 0
//           pc += 4
//         }
//         case 9 => {
//           val (i,j,k) = getValues(1)
//           relative += i.toInt
//           pc += 2
//         }
//         case 99 => {
//           return 99
//         }
//         case _ => {println("Unknown Opcode: " + op); pc+=4}
//       }
//     }
//     println("Got all the way")
//     return 0
//   }

//   def getValues(l:Int = 3):(Long,Long,Int) = {
//     var modes = memory(pc).toString.substring(0,math.max(memory(pc).toString.length() - 2,0)).map(_.toInt -48).toArray
//     while(modes.length != 3) modes = 0 +: modes
//     val i = if (modes(2) == 2) memory(memory(pc+1).toInt + relative) else if (modes(2) == 1) memory(pc+1) else memory(memory(pc+1).toInt)
//     var j:Long = 0
//     if (l > 1) j = if (modes(1) == 2) memory(memory(pc+2).toInt + relative) else if (modes(1) == 1) memory(pc+2) else memory(memory(pc+2).toInt)
//     var k = 0
//     if (l > 2) k = if (modes(0) == 2) (memory(pc+3).toInt + relative) else if (modes(0) == 1) pc+3 else memory(pc+3).toInt
//     (i,j,k)
//   }

//   def immediate(n:Long):Boolean = n == 1
//   def isPos(n:Long):Boolean = n == 2
// }

// case class Pos(x:Int,y:Int) {
//   def +(other:Pos): Pos = Pos(other.x + x, other.y + y)
// }

// object Day11 {
//   val input = scala.io.Source.fromFile("data/data11.txt", "UTF-8").getLines.toVector.mkString.split(',').map(_.toLong).toArray
//   var pos = Pos(0,0)
//   var dir = Pos(0,-1)
//   var grid:Array[Pos] = Array(pos)
//   var colors:Map[Pos, Int] = Map(grid(0) -> 1)

//   val UP = Pos(0,-1) 
//   val DOWN = Pos(0,1)  
//   val RIGHT = Pos(1,0)  
//   val LEFT = Pos(-1,0) 

//   def part1(): Unit = {
//     val intcode = new Computer2(input)
//     class Halt extends Exception{}
//     var painting = true
//     try {
//       while (true) {
//         if (painting) {
//           var output = intcode.process(if(colors.keys.toVector.contains(pos)) colors(pos) else 0.toLong)
//           if (output == 99) throw new Halt
//           colors(pos) = output.toInt
//           painting = false
//         } else {
//           var output = intcode.process(if(colors.keys.toVector.contains(pos)) colors(pos) else 0.toLong)
//           if (output == 99) throw new Halt
//           handleDir(output.toInt)
//           pos+=dir
//           grid :+= pos
//           painting = true
//         }
//       }
//     }
//     catch {
//       case h:Halt => {
//         var dim = Pos(grid.map(_.x).max - grid.map(_.x).min, grid.map(_.y).max - grid.map(_.y).min)
//         var paint:Array[Array[Char]] = Array.fill(dim.y+1)(Array.fill(dim.x+1)(' '))
//         for (p <- grid.reverse.tail) {
//           if (colors(p) == 1) paint(p.y)(p.x) = '#'
//         }
//         for (y <- paint.indices) {
//           for (x <- paint(0).indices) {
//             print(paint(y)(x))
//           }
//           println("")
//         }
//       }
//     }

//     def handleDir(n:Int):Unit = {
//       dir match {
//         case UP    => dir = if (n == 1) Pos(1,0) else Pos(-1,0)
//         case DOWN  => dir = if (n == 1) Pos(-1,0) else Pos(1,0)
//         case RIGHT => dir = if (n == 1) Pos(0,1) else Pos(0,-1)
//         case LEFT  => dir = if (n == 1) Pos(0,-1) else Pos(0,1)
//       }
//     }
//   }

//   def apply() = {
//     println("SOLUTION DAY 11")
//     println("Running part 1")
//     part1()
//     println("Running part 2")
//     //part2()
//   }
// }

