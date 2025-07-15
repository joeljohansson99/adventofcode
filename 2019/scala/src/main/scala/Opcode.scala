// class Computer(val phase:Int, var memory:Array[Int]) {
//     var pc = 0
    
//     def run(input:Int){
//         var setting = phase
//         while (pc < memory.length && memory(pc) != 99) {
//         var op = memory(pc) % 100
//         var mode1 = (mem(pc)/100) % 10
//         var mode2 = (mem(pc)/1000) % 10
//         var mode3 = (mem(pc)/10000) % 10
//         var ret = 0
//         op match {
//           case 1 => {
//             if (immediate(mode1)) {
//               if (immediate(mode2)) {
//                 ret = memory(pc+1) + memory(pc+2)
//               }
//               else {
//                 ret = memory(pc+1) + memory(memory(pc+2))
//               }
//             }
//             else {
//               if (immediate(mode2)) {
//                 ret = memory(memory(pc+1)) + memory(pc+2)
//               }
//               else {
//                 ret = memory(memory(pc+1)) + memory(memory(pc+2))
//               }
//             }

//             if (immediate(mode3)) {
//               memory(pc+3) = ret
//             }
//             else {
//               memory(memory(pc+3)) = ret
//             }
//             pc += 4;
//           }

//           case 2 => {
//             if (immediate(mode1)) {

//               if (immediate(mode2)) {
//                 ret = memory(pc+1) * memory(pc+2)
//               }
//               else {
//                 ret = memory(pc+1) * memory(memory(pc+2))
//               }
//             }
//             else {

//               if (immediate(mode2)) {
//                 ret = memory(memory(pc+1)) * memory(pc+2)
//               }
//               else {
//                 ret = memory(memory(pc+1)) * memory(memory(pc+2))
//               }
//             }

//             if (immediate(mode3)) {
//               memory(pc+3) = ret
//             }
//             else {
//               memory(memory(pc+3)) = ret
//             }
//             pc += 4;
//           }

//           case 3 => {
//             memory(memory(pc+1)) = setting
//             setting = input
//             pc += 2;
//           }

//           case 4 => {
//             println(memory(memory(pc+1)))
//             pc += 2
//           }

//           case 5 => {
//             if (immediate(mode1)) {
//               if (memory(pc+1) != 0) {
//                 if (immediate(mode2)) pc = memory(pc+2)
//                 else pc = memory(memory(pc+2))
//               }
//               else pc += 3
//             }
//             else {
//               if (memory(memory(pc+1)) != 0) {
//                 if (immediate(mode2)) pc = memory(pc+2)
//                 else pc = memory(memory(pc+2))
//               }
//               else pc += 3
//             }
//           }

//           case 6 => {
//             if (immediate(mode1)) {
//               if (memory(pc+1) == 0) {
//                 if (immediate(mode2)) pc = memory(pc+2)
//                 else pc = memory(memory(pc+2))
//               }
//               else pc += 3
//             }
//             else {
//               if (memory(memory(pc+1)) == 0) {
//                 if (immediate(mode2)) pc = memory(pc+2)
//                 else pc = memory(memory(pc+2))
//               }
//               else pc += 3
//             }
//           }

//           case 7 => {
//             if (immediate(mode1)) {
//               if (immediate(mode2)) {
//                 if (immediate(mode3)) {
//                   if (memory(pc+1) < memory(pc+2)) memory(pc+3) = 1
//                   else memory(pc+3) = 0
//                 }
//                 else {
//                   if (memory(pc+1) < memory(pc+2)) memory(memory(pc+3)) = 1
//                   else memory(memory(pc+3)) = 0
//                 }
//               }
//               else {
//                 if (immediate(mode3)) {
//                   if (memory(pc+1) < memory(memory(pc+2))) memory(pc+3) = 1
//                   else memory(pc+3) = 0
//                 }
//                 else {
//                   if (memory(pc+1) < memory(memory(pc+2))) memory(memory(pc+3)) = 1
//                   else memory(memory(pc+3)) = 0
//                 }
//               }
//             }
//             else {
//               if (immediate(mode2)) {
//                 if (immediate(mode3)) {
//                   if (memory(memory(pc+1)) < memory(pc+2)) memory(pc+3) = 1
//                   else memory(pc+3) = 0
//                 }
//                 else {
//                   if (memory(memory(pc+1)) < memory(pc+2)) memory(memory(pc+3)) = 1
//                   else memory(memory(pc+3)) = 0
//                 }
//               }
//               else {
//                 if (immediate(mode3)) {
//                   if (memory(memory(pc+1)) < memory(memory(pc+2))) memory(pc+3) = 1
//                   else memory(pc+3) = 0
//                 }
//                 else {
//                   if (memory(memory(pc+1)) < memory(memory(pc+2))) memory(memory(pc+3)) = 1
//                   else memory(memory(pc+3)) = 0
//                 }
//               }
//             }
//             pc += 4
//           }

//           case 8 => {
//             if (immediate(mode1)) {
//               if (immediate(mode2)) {
//                 if (immediate(mode3)) {
//                   if (memory(pc+1) == memory(pc+2)) memory(pc+3) = 1
//                   else memory(pc+3) = 0
//                 }
//                 else {
//                   if (memory(pc+1) == memory(pc+2)) memory(memory(pc+3)) = 1
//                   else memory(memory(pc+3)) = 0
//                 }
//               }
//               else {
//                 if (immediate(mode3)) {
//                   if (memory(pc+1) == memory(memory(pc+2))) memory(pc+3) = 1
//                   else memory(pc+3) = 0
//                 }
//                 else {
//                   if (memory(pc+1) == memory(memory(pc+2))) memory(memory(pc+3)) = 1
//                   else memory(memory(pc+3)) = 0
//                 }
//               }
//             }
//             else {
//               if (immediate(mode2)) {
//                 if (immediate(mode3)) {
//                   if (memory(memory(pc+1)) == memory(pc+2)) memory(pc+3) = 1
//                   else memory(pc+3) = 0
//                 }
//                 else {
//                   if (memory(memory(pc+1)) == memory(pc+2)) memory(memory(pc+3)) = 1
//                   else memory(memory(pc+3)) = 0
//                 }
//               }
//               else {
//                 if (immediate(mode3)) {
//                   if (memory(memory(pc+1)) == memory(memory(pc+2))) memory(pc+3) = 1
//                   else memory(pc+3) = 0
//                 }
//                 else {
//                   if (memory(memory(pc+1)) == memory(memory(pc+2))) memory(memory(pc+3)) = 1
//                   else memory(memory(pc+3)) = 0
//                 }
//               }
//             }
//             pc += 4
//           }

//           case _ => {println("Unknown Opcode: " + op); pc+=4}
//         }
//     }
//     }

//     def immediate(n:Int):Boolean = n == 1
// }