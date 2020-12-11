import re
from itertools import dropwhile, chain

vectors = [line.rstrip('\n') for line in open('10.in')]

STAR_REGEX = r'position=<(.*)> velocity=<(.*)>'
class Star:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
    def step(self):
       self.x += self.dx
       self.y += self.dy
    def __repr__(self):
        return f'Pos:({self.x}, {self.y}), Vel:({self.dx}, {self.dy})'

def show(stars):
    points = set([(star.x, star.y) for star in stars])
    min_x = min(star.x for star in stars)
    max_x = max(star.x for star in stars)
    min_y = min(star.y for star in stars)
    max_y = max(star.y for star in stars)
    grid = [['#' if (x, y) in points else '.' for x in range(min_x, max_x + 1)]
            for y in range(min_y, max_y + 1)]
    print('\n'.join(''.join(line) for line in grid))

def grid_size(stars):
    min_y = min(star.y for star in stars)
    max_y = max(star.y for star in stars)
    return max_y - min_y

def parse_star(info):
    return Star(*chain.from_iterable(map(
        lambda p: map(int, p.split(',')), 
        re.match(STAR_REGEX, info).groups())))

def simulate(stars):
    i = 0
    while True:
        for star in stars:
            star.step()
        i += 1
        if i > 10000: print(i) #really not ideal but...
        yield stars

stars = [parse_star(v) for v in vectors]
show(next(dropwhile(lambda stars: grid_size(stars) > 15, simulate(stars))))
