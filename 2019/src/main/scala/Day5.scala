object Day5 {
  val input = scala.io.Source.fromFile("data/data5.txt", "UTF-8").getLines.toVector(0).split(',').toVector

  def part1(): Unit = {
    val list = input.map(x=>x.toInt).toArray
    var pc = 0
    while (pc < list.length && list(pc) != 99) {
        var op = list(pc) % 100
        var mode1 = (list(pc)/100) % 10
        var mode2 = (list(pc)/1000) % 10
        var mode3 = (list(pc)/10000) % 10
        var tmp = pc+3
        var ret = 0
        op match {
          case 1 => {
            if (immediate(mode1)) {
              if (immediate(mode2)) {
                ret = list(pc+1) + list(pc+2)
              }
              else {
                ret = list(pc+1) + list(list(pc+2))
              }
            }
            else {
              if (immediate(mode2)) {
                ret = list(list(pc+1)) + list(pc+2)
              }
              else {
                ret = list(list(pc+1)) + list(list(pc+2))
              }
            }

            if (immediate(mode3)) {
              list(pc+3) = ret
            }
            else {
              list(list(pc+3)) = ret
            }
            pc += 4;
          }

          case 2 => {
            if (immediate(mode1)) {

              if (immediate(mode2)) {
                ret = list(pc+1) * list(pc+2)
              }
              else {
                ret = list(pc+1) * list(list(pc+2))
              }
            }
            else {

              if (immediate(mode2)) {
                ret = list(list(pc+1)) * list(pc+2)
              }
              else {
                ret = list(list(pc+1)) * list(list(pc+2))
              }
            }

            if (immediate(mode3)) {
              list(pc+3) = ret
            }
            else {
              list(list(pc+3)) = ret
            }
            pc += 4;
          }

          case 3 => {
            list(list(pc+1)) = scala.io.StdIn.readInt()
            pc += 2;
          }

          case 4 => {
            println(list(list(pc+1)))
            pc += 2
          }

          case 5 => {
            if (immediate(mode1)) {
              if (list(pc+1) != 0) {
                if (immediate(mode2)) pc = list(pc+2)
                else pc = list(list(pc+2))
              }
              else pc += 3
            }
            else {
              if (list(list(pc+1)) != 0) {
                if (immediate(mode2)) pc = list(pc+2)
                else pc = list(list(pc+2))
              }
              else pc += 3
            }
          }
          case 6 => {
            if (immediate(mode1)) {
              if (list(pc+1) == 0) {
                if (immediate(mode2)) pc = list(pc+2)
                else pc = list(list(pc+2))
              }
              else pc += 3
            }
            else {
              if (list(list(pc+1)) == 0) {
                if (immediate(mode2)) pc = list(pc+2)
                else pc = list(list(pc+2))
              }
              else pc += 3
            }
          }
          case 7 => {
            if (immediate(mode1)) {
              if (immediate(mode2)) {
                if (immediate(mode3)) {
                  if (list(pc+1) < list(pc+2)) list(pc+3) = 1
                  else list(pc+3) = 0
                }
                else {
                  if (list(pc+1) < list(pc+2)) list(list(pc+3)) = 1
                  else list(list(pc+3)) = 0
                }
              }
              else {
                if (immediate(mode3)) {
                  if (list(pc+1) < list(list(pc+2))) list(pc+3) = 1
                  else list(pc+3) = 0
                }
                else {
                  if (list(pc+1) < list(list(pc+2))) list(list(pc+3)) = 1
                  else list(list(pc+3)) = 0
                }
              }
            }
            else {
              if (immediate(mode2)) {
                if (immediate(mode3)) {
                  if (list(list(pc+1)) < list(pc+2)) list(pc+3) = 1
                  else list(pc+3) = 0
                }
                else {
                  if (list(list(pc+1)) < list(pc+2)) list(list(pc+3)) = 1
                  else list(list(pc+3)) = 0
                }
              }
              else {
                if (immediate(mode3)) {
                  if (list(list(pc+1)) < list(list(pc+2))) list(pc+3) = 1
                  else list(pc+3) = 0
                }
                else {
                  if (list(list(pc+1)) < list(list(pc+2))) list(list(pc+3)) = 1
                  else list(list(pc+3)) = 0
                }
              }
            }
            pc += 4
          }
          case 8 => {
            if (immediate(mode1)) {
              if (immediate(mode2)) {
                if (immediate(mode3)) {
                  if (list(pc+1) == list(pc+2)) list(pc+3) = 1
                  else list(pc+3) = 0
                }
                else {
                  if (list(pc+1) == list(pc+2)) list(list(pc+3)) = 1
                  else list(list(pc+3)) = 0
                }
              }
              else {
                if (immediate(mode3)) {
                  if (list(pc+1) == list(list(pc+2))) list(pc+3) = 1
                  else list(pc+3) = 0
                }
                else {
                  if (list(pc+1) == list(list(pc+2))) list(list(pc+3)) = 1
                  else list(list(pc+3)) = 0
                }
              }
            }
            else {
              if (immediate(mode2)) {
                if (immediate(mode3)) {
                  if (list(list(pc+1)) == list(pc+2)) list(pc+3) = 1
                  else list(pc+3) = 0
                }
                else {
                  if (list(list(pc+1)) == list(pc+2)) list(list(pc+3)) = 1
                  else list(list(pc+3)) = 0
                }
              }
              else {
                if (immediate(mode3)) {
                  if (list(list(pc+1)) == list(list(pc+2))) list(pc+3) = 1
                  else list(pc+3) = 0
                }
                else {
                  if (list(list(pc+1)) == list(list(pc+2))) list(list(pc+3)) = 1
                  else list(list(pc+3)) = 0
                }
              }
            }
            pc += 4
          }
          case _ => {println("Ogiltig: " + op); pc+=4}
        }
    }
  }
  def part2(): Unit = {

  }

  def apply() = {
    println("SOLUTION DAY 5")
    println("Running part 1")
    part1()
    println("Running part 2")
    //part2()
  }
  def immediate(n:Int):Boolean = n == 1
}