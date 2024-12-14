import aoc
from math import prod

def common(lines):
    if len(lines) == 12:
        MAX_X = 11
        MAX_Y = 7
    else:
        MAX_X = 101
        MAX_Y = 103

    class Robot:
        def __init__(self, x, y, xdel, ydel):
            self.x = x
            self.y = y
            self.xdel = xdel
            self.ydel = ydel

        def run(self):
            self.x = (self.x + self.xdel) % MAX_X
            self.y = (self.y + self.ydel) % MAX_Y

    robots = []
    for line in lines:
        robots.append(Robot(
            int(line.split("=")[1].split(",")[0]),
            int(line.split(",")[1].split(" ")[0]),
            int(line.split("=")[2].split(",")[0]),
            int(line.split(",")[2]),
        ))

    return robots, MAX_X, MAX_Y


def part_1(lines):
    robots, MAX_X, MAX_Y = common(lines)

    quadrants = [[],[],[],[]]

    for r in robots:
        for _ in range(100):
            r.run()

        if r.x < MAX_X // 2 and r.y < MAX_Y // 2:
            quadrants[0].append(r)
        elif r.x < MAX_X // 2 and r.y > MAX_Y // 2:
            quadrants[1].append(r)
        elif r.x > MAX_X // 2 and r.y < MAX_Y // 2:
            quadrants[2].append(r)
        elif r.x > MAX_X // 2 and r.y > MAX_Y // 2:
            quadrants[3].append(r)

    return prod([len(x) for x in quadrants])

def part_2(lines):
    robots, MAX_X, MAX_Y = common(lines)

    i = 0
    while True:
        locs = [(r.x, r.y) for r in robots]
        c = 0
        for r in locs:
            if (r[0]+1, r[1]) in locs or (r[0]-1, r[1]) in locs or (r[0], r[1]+1) in locs or (r[0], r[1]-1) in locs:
                c += 1

        if c > 150:
            for y in range(MAX_Y):
                row = ""
                for x in range(MAX_X):
                    if any([r.x == x and r.y == y for r in robots]):
                        row += "X"
                    else:
                        row += "."
                print(row)

            test = input(">")
            if test == "y":
                return i
            
        i += 1
        for r in robots:
            r.run()

        if i > 100000:
            raise ValueError

aoc.aoc_run("files/full/day14.txt", "files/example/day14_example.txt", part_1, 12)
aoc.aoc_run("files/full/day14.txt", "files/example/day14_example.txt", part_2)