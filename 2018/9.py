from collections import deque

info = [line.rstrip('\n') for line in open('9.in')]
#431 players; last marble is worth 70950 points

#part (a)
players = 431
score = [0 for i in range(players)]
marbles = deque([0])
high_marble = 70950
next_player = 0

#uses deque data structure to mimic circle motion of the game, keeping the current marble at the 0th index
def left(n):
    for i in range(n):
        marbles.appendleft(marbles.pop())
def right(n):
    for i in range(n):
        marbles.append(marbles.popleft())

for i in range(1, high_marble + 1):
    if(i % 23 == 0):
        score[next_player] += i
        left(7)
        score[next_player] += marbles.popleft()
    else:
        right(2)
        marbles.appendleft(i)
    next_player = (next_player + 1) % players
print(max(score))

#part (b)
players = 431
score = [0 for i in range(players)]
marbles = deque([0])
high_marble = 7095000
next_player = 0

for i in range(1, high_marble + 1):
    if(i % 23 == 0):
        score[next_player] += i
        left(7)
        score[next_player] += marbles.popleft()
    else:
        right(2)
        marbles.appendleft(i)
    next_player = (next_player + 1) % players
print(max(score))
