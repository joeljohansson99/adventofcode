case class TPos(var x:Int, var y:Int, var z:Int) {
  def +(o:TPos): TPos = TPos(x + o.x, y + o.y, z + o.z)
  def sum: Int = Math.abs(x) + Math.abs(y) + Math.abs(z)
  def ==(o:TPos): Boolean = o.x == x && o.y == y && o.z == z
}

case class Moon(var pos:TPos) {
  var changes:Array[(TPos,TPos)] = Array.empty
  var vel:TPos = TPos(0,0,0)
  var steps = 0
  var xFound = false
  var yFound = false
  var zFound = false
  def changeVel(others:Array[Moon]):Unit = {
    for (other <- others) {
      if (other.pos.x > pos.x) vel.x += 1
      else if (other.pos.x < pos.x) vel.x -= 1

      if (other.pos.y > pos.y) vel.y += 1
      else if (other.pos.y < pos.y) vel.y -= 1

      if (other.pos.z > pos.z) vel.z += 1
      else if (other.pos.z < pos.z) vel.z -= 1
    }
  }

  def changePos():Unit = {
    pos += vel
  }
}

case class X(var pos:Int){
  var vel:Int = 0
  var init = (pos,vel)
  def changeVel(other:Array[X]): Unit = {
    for (o <- other) {
      if (o.pos > pos) vel += 1
      else if (o.pos < pos) vel -= 1
    }
  }
  def changePos():Unit = {
    pos += vel
  }
}

object Day12 {
  val input = scala.io.Source.fromFile("data/data12.txt", "UTF-8").getLines.toVector


  def part1(): Unit = {
    val distance = input.map(x => x.split(",").filter(!_.contains(" ")).toVector.map(_.toInt))
    var moons: Array[Moon] = Array(
                                    Moon(TPos(distance(0)(0), distance(0)(1), distance(0)(2))),
                                    Moon(TPos(distance(1)(0), distance(1)(1), distance(1)(2))),
                                    Moon(TPos(distance(2)(0), distance(2)(1), distance(2)(2))),
                                    Moon(TPos(distance(3)(0), distance(3)(1), distance(3)(2)))
                                  )

    for (i <- 0 until 1000){
      moons.foreach(m => m.changeVel(moons.filter(_ != m)))
      moons.foreach(_.changePos)
    }

    var pot: Array[Int] = moons.map(_.pos.sum)
    var kin: Array[Int] = moons.map(_.vel.sum)

    var sum = 0
    for (i <- moons.indices) {
      sum += kin(i) * pot(i)
    }

    println(sum)
  }

  def part2(): Unit = {
    val distance = input.map(x => x.split(",").filter(!_.contains(" ")).toVector.map(_.toInt))
    var moonsArr: Array[X] = Array(
                                    X(distance(0)(0)),
                                    X(distance(1)(0)),
                                    X(distance(2)(0)),
                                    X(distance(3)(0)),

                                    X(distance(0)(1)),
                                    X(distance(1)(1)),
                                    X(distance(2)(1)),
                                    X(distance(3)(1)),

                                    X(distance(0)(2)),
                                    X(distance(1)(2)),
                                    X(distance(2)(2)),
                                    X(distance(3)(2))
                                  )
    var i = 0
    var moons = moonsArr.take(4)
    while(!moons.forall(x => (x.pos,x.vel) == x.init) || i == 0) {
      moons.foreach(m => m.changeVel(moons.filter(_ != m)))
      moons.foreach(_.changePos)
      i+=1
    }
    var x = i

    i = 0
    moons = moonsArr.drop(4).take(4)
    while(!moons.forall(x => (x.pos,x.vel) == x.init) || i == 0) {
      moons.foreach(m => m.changeVel(moons.filter(_ != m)))
      moons.foreach(_.changePos)
      i+=1
    }
    var y = i

    i = 0
    moons = moonsArr.takeRight(4)
    while(!moons.forall(x => (x.pos,x.vel) == x.init) || i == 0) {
      moons.foreach(m => m.changeVel(moons.filter(_ != m)))
      moons.foreach(_.changePos)
      i+=1
    }
    var z = i

    println(Vector(x,y,z).mkString(" "))
  }

  def apply() = {
    println("SOLUTION DAY 12")
    println("Running part 1")
    part1()
    println("Running part 2")
    part2()
  }
}