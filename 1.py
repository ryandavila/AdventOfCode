#part (a)
lines = [int(line.rstrip('\n')) for line in open('1.in')]
print(sum(lines))

#part(b)
frequency = set()
value = 0
is_done = False
while not is_done:
    for i in range(len(lines)):
        value += lines[i]
        if(value in frequency):
            print(value)
            is_done = True
            break
        frequency.add(value)
