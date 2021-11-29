import scala.collection.mutable.ArrayBuffer
object Day16 {
  val input:Array[Int] = scala.io.Source.fromFile("data/data16.txt", "UTF-8").getLines.toArray.apply(0).mkString(" ").split(" ").map(_.toInt)

  def part1(): Unit = {
    var mutate:Array[Int] = Array.fill(1000)(input).flatten
    var res:Array[String] = Array.empty
    for (i <- 0 to 100) {
      println(i)
      val t = doPattern(mutate).mkString
      if (res.contains(t)) println(t)
      res :+= t
    } 
  }

  def doPattern(mutate:Array[Int]): Array[Int] = {
    var number:Array[Int] = mutate
    val base:Array[Int] = Array(0,1,0,-1)

    for (l <- 0 until 100) {
      var newNumber:Array[Int] = Array.empty
      var i = 1
      while (i <= number.length) {

        val b:ArrayBuffer[Int] = ArrayBuffer.empty

        while (number.length >= b.length) {
          base.foreach(n => b ++= ArrayBuffer.fill(i)(n))
        }
        
        newNumber :+= math.abs(number.indices.map{k => b(k+1)*number(k)}.sum) % 10

        i+=1
      }
      number = newNumber
    }
    number.take(8)
  }

  def part2(): Unit = {
    var res = Vector.fill(10000)(input.toVector).flatten
    val messageOffset = input.take(7).mkString.toInt
    res = res.slice(messageOffset, res.length)
    for (k <- 1 to 100) {
      var newRes: Vector[Int] = Vector.empty
      var sum = 0
      for (i <- res.length - 1 to 0 by -1) {
        sum += res(i)
        newRes = math.abs(sum % 10) +: newRes
      }
      res = newRes
      println(k + "/100")
    }
    println(res.take(8).mkString)
  }

  def apply() = {
    println("SOLUTION DAY 16")
    println("Running part 1")
    //part1()
    println("Running part 2")
    part2()
  }
}