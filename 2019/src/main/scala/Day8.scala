import scala.collection.mutable.ArrayBuffer

object Day8 {
  val input = scala.io.Source.fromFile("data/data8.txt", "UTF-8").getLines.toVector

  def part1(): Unit = {
    var list = input(0).toList
    var resTot:ArrayBuffer[ArrayBuffer[Int]] = new ArrayBuffer()
    object Done extends Exception{}
    var i = 0
    try {
      while (true){
        var res:ArrayBuffer[Int] = new ArrayBuffer()
        for (k <- 0 until 25){
          for (l <- 0 until 6){
            if (k*6+l + i*25*6 >= list.length) throw Done
            res += list(l+k*6 + i*25*6).toInt - 48
          }
        }
        resTot += res
        i+=1
      }
    }
    catch {
      case Done =>
    }
    val counting = resTot.map(xs => xs.count(_==0))
    val index = counting.indexOf(counting.min)
    val ones = resTot(index).count(_ == 1)
    val twos = resTot(index).count(_ == 2)
    println(resTot(index))
    println("ones: " + ones + " * twos: " + twos + " = " + ones*twos)
  }

  def part2(): Unit = {
    var layers = input(0).grouped(25*6).toVector

    var image:String = ""

    for (i <- layers(0).indices) {
      var quit = false
      var k = 0
      while(!quit) {
        if (layers(k)(i) == '0') {
          image += ' '
          quit = true
        } else if (layers(k)(i) == '1') {
          image += '#'
          quit = true
        }
        k+=1
      }
      if ((i+1) % 25 == 0) image += '\n'
    }
    
    println(image)
  }

  def apply() = {
    println("SOLUTION DAY 8")
    println("Running part 1")
    //part1()
    println("Running part 2")
    part2()
  }
}