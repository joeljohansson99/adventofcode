
object Day14 {
  val input = scala.io.Source.fromFile("data/data14.txt", "UTF-8").getLines.toVector.map(_.mkString)
  var surplus: scala.collection.mutable.Map[String,Long] = scala.collection.mutable.Map.empty
  var ores:Long = 0
  var end = 1000000000000L

  def part1(): Unit = {
    println(recur("FUEL",1))
  }

  def recur(target:String, n_ : Long): Long = {
    var n:Long = n_
    if (target == "ORE") return retOre(n, target)

    val potent:Vector[(Long,String)] = input.filter(xs => xs.split(" ").last == target)(0).split("=>").take(1)(0).split(", ").toVector.map(xs => (xs.split(" ")(0).toLong,xs.split(" ")(1)))
    var m:Long = input.filter(_.split(" ").last == target)(0).split(" => ").takeRight(1)(0).split(" ")(0).toLong

    var sum:Long = 0
    for (pot <- potent) {
      var sur:Long = 0
      if (surplus.keys.toVector.contains(target)) n -= surplus(target)
      while (n % m != 0) {n+=1;sur+=1}
      surplus(target) = sur
      sum += recur(pot._2, n*pot._1/m)
    }
    sum
  }

  def part2(): Unit = {
    var i = 3281800 // value close to answer(3281800), function is too slow
    println(end)
    while ((recur("FUEL", i) - ores.toLong) < end) {i+=1;println(i)}
    println(i)
  }

  def retOre(n:Long, target:String):Long = {
    val o:Long = input.filter(x => x.contains("ORE") || x.contains(target))(0).split(" => ").take(1)(0).split(" ").take(1)(0).toLong
    var sum:Long = 0
    while (sum < n) {
      sum  += o
    }
    ores += sum-n
    sum
  }

  def apply() = {
    println("SOLUTION DAY 14")
    println("Running part 1")
    part1()
    println("Running part 2")
    //part2()
  }
}