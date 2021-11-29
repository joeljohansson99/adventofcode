object Day20 {
  var inputInit:Array[Array[String]] = scala.io.Source.fromFile("data/data20.txt", "UTF-8").getLines.toArray.map(_.split("").toArray)

  case class Pos6(x:Int,y:Int) {
    def +(o:Pos6):Pos6 = Pos6(o.x+x,o.y+y)
  }

  def part1(): Unit = {
    var usedTeleports:Array[String] = Array.empty
    val visited:Array[Array[Boolean]] = Array.fill(input.length)(Array.fill(input(0).length)(false))
    var steps = 0
    var map:Array[Array[String]] = input.map(_.clone).clone
    map(128)(45) = "o"
    var running = true
    while (running) {
      val n = scala.io.StdIn.readLine()
      if (n == "q") running = false
      var posses:Array[Pos6] = Array.empty
      for (r <- map.indices) {
        for (c <- map(0).indices) {
          if (map(r)(c) == "o") {
            posses :+= Pos6(c,r)
          }
        }
      }
      for (p <- posses) {
        for (r <- p.y-1 to p.y+1) {
          for (c <- p.x-1 to p.x+1) {
            var dir = Pos6(c-p.x, r-p.y)
            if (r == p.y || c == p.x) {
              if (map(r)(c)== "!") running = false
              else if (map(r)(c)== ".") map(r)(c) = "o"
              else if (map(r)(c) != "#") checkTeleport(Pos6(c,r), dir)
            }
          }
        }
      }
      println(map.map(_.mkString).mkString("\n"))
      steps += 1
    }
    println(steps-1)

    def checkTeleport(pos1:Pos6, dir:Pos6):Unit = {
      var pos2 = pos1 + dir
      val cantBe:Array[String] = Array(" ","!",".","@","#","o")
      if (!cantBe.contains(map(pos1.y)(pos1.x))) {
        val first:String = map(pos1.y)(pos1.x)
        val second:String = map(pos2.y)(pos2.x)
        var toT1:Pos6 = Pos6(0,0)
        var toT2:Pos6 = Pos6(0,0)
        for (r <- map.indices; c <- map(0).indices) {
          if (second == map(r)(c) && (r != pos1.y && c != pos1.x)) {
            var startR = if (r-1 <= 0) 1 else r-1
            var startC = if (c-1 <= 0) 1 else c-1
            var endR = if (r+1 >= map.length) map.length-1 else r+1
            var endC = if (c+1 >= map(0).length) map(0).length-1 else c+1
            for (row <- startR to endR; col <- startC to endC) {
              if (input(row)(col) == first) {
                toT2 = Pos6(c,r)
                toT1 = Pos6(col,row)
              }
            }
          }
        }
        if (toT1.x > 0 && toT1.x < map(0).length-1 && toT1.y > 0 && toT1.y < map.length-1) {
          for (r <- toT1.y-1 to toT1.y+1; c <- toT1.x-1 to toT1.x+1) {
            if (map(r)(c) == ".") map(r)(c) = "o"
          }
        }
        if (toT2.x > 0 && toT2.x < map(0).length-1 && toT2.y > 0 && toT2.y < map.length-1) {
          for (r <- toT2.y-1 to toT2.y+1; c <- toT2.x-1 to toT2.x+1) {
            if (map(r)(c) == ".") map(r)(c) = "o"
          }
        }
      }
    }
  }

  def part2(): Unit = {
  }

  def apply() = {
    println("SOLUTION DAY 20")
    println("Running part 1")
    part1()
    println("Running part 2")
    //part2()
  }
}