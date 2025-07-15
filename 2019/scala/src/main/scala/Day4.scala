object Day4 {
  val input = scala.io.Source.fromFile("data/data4.txt", "UTF-8").getLines.toVector

  def part1(): Unit = {
    var ans:Array[Int] = Array.empty

    for (i <- 123257 to 647015) {
      
      var adjacent = false
      var increase = true
      var n = i.toString.map(_.asDigit)
      for (i <- 0 to n.length - 2) {
        if (n(i) == n(i+1)) {
          adjacent = true
        }
        else if(n(i) < n(i+1)) {}
        else increase = false
        
      }
      if (adjacent && increase) {
        ans :+= i
      }
    }
    println(ans.length)
  }

  def part2(): Unit = {
        var ans:Array[Int] = Array.empty
    for (i <- 123257 to 647015) {
      var adjacent = false
      var increase = true
      var adjOver = false
      var last = -1
      var adj = 0
      var n = i.toString.map(_.asDigit)
      
      for (i <- 0 to n.length - 2) {
        if (n(i) == n(i+1)) {
          adj +=1
          if (last != n(i) && adjacent) {
            adjOver = true
          }
          last = n(i)
          if (adj == 1) adjacent = true
          if (adj > 1) adjacent = false
        }
        else if(n(i) < n(i+1)) {
          adj = 0
        }
        else increase = false
      }
      if ((adjacent || adjOver) && increase) {
        ans :+= i
      }
    }
    println(ans.length)
  }

  def apply() = {
    println("SOLUTION DAY 4")
    println("Running part 1")
    part1()
    println("Running part 2")
    part2()
  }
}