import scala.collection.mutable.Map
import scala.collection.mutable.ArrayBuffer

object Day18 {
  var input:Array[Array[String]] = scala.io.Source.fromFile("data/data18.txt", "UTF-8").getLines.toArray.map(_.split("").toArray)
  var alphabet:Array[String] = "abcdefghijklmnopqrstuvwxyz".split("")
  var keys:ArrayBuffer[Key] = ArrayBuffer(Key("@",Place(input.filter(_.contains("@"))(0).indexOf("@"), input.indexOf(input.filter(_.contains("@"))(0)))))
  alphabet.map(k => if(input.filter(_.contains(k)).length != 0)
     keys += Key(k,Place(input.filter(_.contains(k))(0).indexOf(k), input.indexOf(input.filter(_.contains(k))(0))))
  )

  case class Place(x:Int,y:Int)
  
  case class Key(key:String,pos:Place) {
    var keyToKey:Map[String,Int] = Map.empty
    var doors:Map[String,ArrayBuffer[String]] = Map.empty
    def minLength:Int = keyToKey.values.min
  }

  def part1(): Unit = {
    println("Getting info from key to key")
    for (fromKey <- keys; toKey <- keys) if (fromKey != toKey && toKey.key != "@") getKeyInfo(fromKey,toKey.key)

    val visitedInit:Array[Boolean] = Array.fill(keys.length)(false)

    var currentMin:Int = Int.MaxValue

    def recur(key:Key, unlocked:ArrayBuffer[String], steps_ :Int, visited:Array[Boolean]): Unit = {
      var steps = steps_

      unlocked += key.key.toUpperCase
      visited(keys.indexOf(key)) = true

      if (!visited.contains(false)) if (steps < currentMin){currentMin = steps; println(currentMin)}
      
      for (i <- keys.indices) {
        if (!visited(i) && key.doors(keys(i).key).diff(unlocked).isEmpty) {
          recur(keys(i), unlocked.clone, steps + key.keyToKey(keys(i).key), visited.clone)
        }
      }
    }

    println("Going into recursive")
    recur(keys(0),ArrayBuffer.empty, 0, visitedInit)
    println(currentMin)
  }

  def getKeyInfo(fromKey:Key, toKeyString:String):Unit = {
    val visited:Array[Array[Boolean]] = Array.fill(input.length)(Array.fill(input(0).length)(false))

    def recur(pos:Place):(Array[Place],Boolean) = {
      visited(pos.y)(pos.x) = true
      var positions:Array[Place] = Array(pos)

      for (r <- pos.y-1 to pos.y+1; c <- pos.x-1 to pos.x+1) {
        if (input(r)(c) == toKeyString) return (positions,true)
        else if (!visited(r)(c) && input(r)(c) != "#" && (pos.x == c || pos.y == r)) {
          val res = recur(Place(c,r))
          if (res._2) {
            return (positions ++ res._1,true)
          }
        }
      }
      (positions,false)
    }

    var path:Array[Place] = recur(fromKey.pos)._1
    var doors:ArrayBuffer[String] = ArrayBuffer.empty
    fromKey.keyToKey += (toKeyString -> path.length)
    for (p <- path) {
      if (alphabet.map(_.toUpperCase).contains(input(p.y)(p.x))) doors += input(p.y)(p.x)
    }
    fromKey.doors += (toKeyString -> doors)
  }

  def part2(): Unit = {

  }

  def apply() = {
    println("SOLUTION DAY 18")
    println("Running part 1")
    part1()
    println("Running part 2")
    //part2()
  }
}