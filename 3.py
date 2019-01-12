elves = [line.rstrip('\n') for line in open('3.in')]

# part (a)
Matrix = [[0 for x in range(1000)] for y in range(1000)]
counter = 0
unclaimed = []

for elf in elves:
    info = elf.split(" ")
    xi = int(info[2].split(",")[0])
    dx = int(info[3].split("x")[0])
    yi = int(info[2].split(",")[1][:-1])
    dy = int(info[3].split("x")[1])

    for x in range(xi, xi+dx):
        for y in range(yi, yi+dy):
            Matrix[x][y] += 1
            if (Matrix[x][y] == 2):
                counter += 1
print(counter)

#part (b)
new_elves = []
for elf in elves:
    unclaimed = True
    info = elf.split(" ")
    xi = int(info[2].split(",")[0])
    dx = int(info[3].split("x")[0])
    yi = int(info[2].split(",")[1][:-1])
    dy = int(info[3].split("x")[1])

    for x in range(xi, xi+dx):
        for y in range(yi, yi+dy):
            if (Matrix[x][y] == 1):
                continue
            else:
                unclaimed = False
    new_elves.append(unclaimed)
print(new_elves.index(True)+1)    #prints the index of the True element, need to add 1 since the answer is 1-indexed
