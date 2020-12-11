from collections import defaultdict
steps = [line.rstrip('\n') for line in open('7.in')]

#part (a)
#returns the dependency in the form (a, b): "step a must be finished before step b can begin"
def parse_step(step):
    parsed =  step.lower().split('step ')
    return (parsed[1][0], parsed[2][0])

nodes = defaultdict(list)
amount = defaultdict(int)

for s in steps:
    parse = parse_step(s)
    nodes[parse[0]].append(parse[1])
    amount[parse[1]] += 1

tracker = []
for n in nodes:
    if amount[n] == 0:
        tracker.append(n)

answer = ''
while tracker:
    ele = sorted(tracker)[0]
    tracker = [e for e in tracker if e != ele]
    answer += ele
    for x in nodes[ele]:
        amount[x] -= 1
        if amount[x] == 0:
            tracker.append(x)
print(answer.upper())

#part (b)
nodes = defaultdict(list)
amount = defaultdict(int)
t = 0
work = []
queue = []

for s in steps:
    parse = parse_step(s)
    nodes[parse[0]].append(parse[1])
    amount[parse[1]] += 1

def add_task(task):
    queue.append(task)

def start_task():
    global queue
    while len(work) < 5 and queue:
        low = min(queue)
        queue = [q for q in queue if q != low]
        work.append((t+61+ord(low)-ord('a'), low))

for n in nodes:
    nodes[n] = sorted(nodes[n])
for n in nodes:
    if amount[n] == 0:
        add_task(n)
    start_task()

while work or queue:
    t, task = min(work)
    work = [w for w in work if w != (t, task)]
    for n in nodes[task]:
        amount[n] -= 1
        if amount[n] == 0:
            add_task(n)
        start_task()
print(t)
