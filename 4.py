from collections import defaultdict
shifts = [line.rstrip('\n') for line in open('4.txt')]
shifts.sort()
#'[1518-03-16 00:04] Guard #1973 begins shift'
#'[1518-03-16 00:34] falls asleep'
#'[1518-03-16 00:39] wakes up'
#'[1518-03-16 00:52] falls asleep'
#'[1518-03-16 00:53] wakes up'

#part a
guards = defaultdict(int)
times = defaultdict(lambda: defaultdict(int))
for shift in shifts:
    if 'begins shift' in shift:
        guard = shift.split(' ')[3][1:]
    elif 'falls asleep' in shift:
       starting_minute = int(shift.split(' ')[1][3:-1])
    elif 'wakes up' in shift:
        for t in range(starting_minute, int(shift.split(' ')[1][3:-1])):
            times[guard][t] += 1
            guards[guard] += 1

def findMax(d):
    best = None
    for k,v in d.items():
        if best is None or v > d[best]:
            best = k
    return best

best_guard = findMax(guards)
best_time = findMax(times[best_guard])

print(best_guard, best_time, int(best_guard) * int(best_time))

#part b
guards = defaultdict(int)
times = defaultdict(int)
for shift in shifts:
    if 'begins shift' in shift:
        guard = shift.split(' ')[3][1:]
    elif 'falls asleep' in shift:
       starting_minute = int(shift.split(' ')[1][3:-1])
    elif 'wakes up' in shift:
        for t in range(starting_minute, int(shift.split(' ')[1][3:-1])):
            times[(guard, t)] += 1
            guards[guard] += 1

def findMax(d):
    best = None
    for k,v in d.items():
        if best is None or v > d[best]:
            best = k
    return best

best_guard, best_time = findMax(times)

print(best_guard, best_time, int(best_guard) * int(best_time))
