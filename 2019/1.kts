import java.io.File

fun readFile(fileName: String): List<String>
        = File(fileName).readLines()

fun calcFuelRequirement(mass: String): Int {
        return (Math.floor(mass.toDouble() / 3) - 2).toInt()
}


val input = readFile("1.in")
var part1 = 0
for(line in input) {
    part1 += calcFuelRequirement(line)
}
println(part1)

fun calcFuelsFuelRequirement(mass: String): Int {
    var done = false
    var amount = 0
    while( !done ) {

    }
}
