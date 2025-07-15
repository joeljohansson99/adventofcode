import scala.collection.mutable.ArrayBuffer

object Day6 {
  val input = scala.io.Source.fromFile("data/data6.txt", "UTF-8").getLines.toVector

  def part1(): Unit = {
    var sum:Long = input.length
    for (orbit <- input.reverse) {
      sum += recur(orbit)
    }
    println(sum)
  }

  def recur(start:String): Int = {
    var orbits = input.filter(x => x.take(3) == start.takeRight(3))
    var jumps = orbits.length
    for (planet <- orbits) jumps += recur(planet)
    jumps
  }

  // var youArray[String] = new ArrayBuffer()
  // var sanArray[String] = new ArrayBuffer()

  // def part2(): Unit = {
  //   rec("YOU")
  //   rec("SAN")
  //   var steps = 0
  //   youArray.foreach(println)
  //   object FoundWay extends Exception{}
  //   try {
  //     for (san <- sanArray) {
  //       if (youArray.contains(san)){
  //         for (you <- youArray) {
  //           if (sanArray.contains(you)){
  //             println(steps)
  //             throw FoundWay
  //           }
  //           steps+=1
  //         }
  //       }
  //       steps+=1
  //     }
  //   }
  //   catch {
  //     case FoundWay => 
  //   }
  // }

  // def rec(start:String, n:Int): Unit = {
  //   var orbits = input.filter(x => x.takeRight(3) == start)
  //   if (n == 1) youArray ++= orbits
  //   else sanArray +== orbits
  //   for (planet <- orbits) {
  //     rec(planet, n)
  //   }
  // }

  def apply() = {
    println("SOLUTION DAY 6")
    println("Running part 1")
    //part1()
    println("Running part 2")
    //part2()
  }
}