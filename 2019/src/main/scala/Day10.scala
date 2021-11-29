

object Day10 {
  val input = scala.io.Source.fromFile("data/data10.txt", "UTF-8").getLines.toVector

  def part1(): Unit = {
    var grid:Array[Array[Int]] = Array.fill(input.length)(Array.fill(input(0).length)(0))

    for (r <- input.indices) {
      for (c <- input(0).indices) {
        if (input(r)(c) == '#') grid(r)(c) = countRocks(r,c)
      }
    }

    grid.foreach(x => println(x.max+ " - " + x.indexOf(x.max) + "<>"+ grid.indexOf(x)))
    for (r <- grid.indices){
      for (c <- grid(0).indices) {
        print(grid(r)(c) + ",")
      }
      println("")
    }
  }

  def countRocks(x:Int, y:Int): Int =  {
    var checked:Array[Array[Boolean]] = Array.fill(input.length)(Array.fill(input(0).length)(false))
    var count = 0

    for (r <- (0 until input.length)) {
      for (c <- (0 until input.length)) {
        var row = x + r
        var col = y + c
        var found = false
        
        while (!(col >= input(0).length || row >= input.length || (x==row && y==col))) {
          if (input(row)(col) == '#' && !checked(row)(col) && !found) {
            count+=1
            found = true
          }
          checked(row)(col) = true
          row += r
          col += c
        }
      }
    }
    for (r <- (0 until input.length)) {
      for (c <- (0 until input.length)) {
        var row = x - r
        var col = y - c
        var found = false
        
        while (!(col < 0 || row < 0 || (x==row && y==col))) {
          if (input(row)(col) == '#' && !checked(row)(col) && !found) {
            count+=1
            found = true
          }
          checked(row)(col) = true
          row -= r
          col -= c
        }
      }
    }
    for (r <- (0 until input.length)) {
      for (c <- (0 until input.length)) {
        var row = x - r
        var col = y + c
        var found = false
        
        while (!(col >= input(0).length || row < 0 || (x==row && y==col))) {
          if (input(row)(col) == '#' && !checked(row)(col) && !found) {
            count+=1
            found = true
          }
          checked(row)(col) = true
          row -= r
          col += c
        }
      }
    }
    for (r <- (0 until input.length)) {
      for (c <- (0 until input.length)) {
        var row = x + r
        var col = y - c
        var found = false
        
        while (!(col < 0 || row >= input.length || (x==row && y==col))) {
          if (input(row)(col) == '#' && !checked(row)(col) && !found) {
            count+=1
            found = true
          }
          checked(row)(col) = true
          row += r
          col -= c
        }
      }
    }
    count
  }

  def part2(): Unit = {
    vaporizeRocks(20,20)
    
  }

  def vaporizeRocks(x:Int, y:Int): Unit = {
    var grid:Array[Array[Char]] = Array.fill(input.length)(Array.fill(input(0).length)('.'))
    val shots = canShoot(x,y).take(200)
    val rest = canShoot(x,y).takeRight(92)
    for ((r,c) <- shots) {
      grid(r)(c) = '#'
    }
    for ((r,c) <- rest) {
      grid(r)(c) = 'O'
    }
    grid(x)(y) = 'X'
    for (r <- grid.indices){
      for (c <- grid(0).indices) {
        print(grid(r)(c) + ",")
      }
      println("")
    }
  }



  def canShoot(x:Int, y:Int): Array[(Int,Int)] =  {
    var checked:Array[Array[Boolean]] = Array.fill(input.length)(Array.fill(input(0).length)(false))
    var pos: Array[(Int,Int)] = Array.empty
    var count = 0

    for (r <- (0 until input.length)) {
      for (c <- (0 until input.length)) {
        var row = x + r
        var col = y + c
        var found = false
        
        while (!(col >= input(0).length || row >= input.length || (x==row && y==col))) {
          if (input(row)(col) == '#' && !checked(row)(col) && !found) {
            pos :+= (row,col)
            count+=1
            found = true
          }
          checked(row)(col) = true
          row += r
          col += c
        }
      }
    }
    for (r <- (0 until input.length)) {
      for (c <- (0 until input.length)) {
        var row = x - r
        var col = y + c
        var found = false
        
        while (!(col >= input(0).length || row < 0 || (x==row && y==col))) {
          if (input(row)(col) == '#' && !checked(row)(col) && !found) {
            pos :+= (row,col)
            count+=1
            found = true
          }
          checked(row)(col) = true
          row -= r
          col += c
        }
      }
    }
    for (r <- (0 until input.length)) {
      for (c <- (0 until input.length)) {
        var row = x + r
        var col = y - c
        var found = false
        
        while (!(col < 0 || row >= input.length || (x==row && y==col))) {
          if (input(row)(col) == '#' && !checked(row)(col) && !found) {
            pos :+= (row,col)
            count+=1
            found = true
          }
          checked(row)(col) = true
          row += r
          col -= c
        }
      }
    }
    for (r <- (0 until input.length)) {
      for (c <- (0 until input.length)) {
        var row = x - r
        var col = y - c
        var found = false
        
        while (!(col < 0 || row < 0 || (x==row && y==col))) {
          if (input(row)(col) == '#' && !checked(row)(col) && !found) {
            pos :+= (row,col)
            count+=1
            found = true
          }
          checked(row)(col) = true
          row -= r
          col -= c
        }
      }
    }
    println(count + " ... " + pos.length)
    pos
  }

  def apply() = {
    println("SOLUTION DAY 10")
    println("Running part 1")
    part1()
    println("Running part 2")
    part2()
  }
}