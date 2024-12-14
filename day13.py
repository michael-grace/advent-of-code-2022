import aoc
import math

"""
    to say i have a masters mathematics degree, and did an
    algebra based dissertation last year, I'm dissapointed in myself
    it took two days to notice it was a linear algebra problem, and not
    one to solve with recursion. and what i mean by "notice it was a linear
    algebra problem" is "spotted memes on the subreddit"

    apologies to anyone who ever taught me during my degree
"""

# class Node:
#     def __init__(self, x, y, targx, targy, score, switched):
#         self.x = x
#         self.y = y
#         self.targx = targx
#         self.targy = targy
#         self.score = score
#         self.switched = switched
#         # print(x, y)

#         self.solved = False
#         if self.x == self.targx and self.y == targy:
#             self.solved = True

#         if self.x != self.targx and self.y != self.targy and self.x != 0 and self.y != 0:
#             if targx / self.x == targy / self.y and targx % self.x == 0 and targy % self.y == 0:
#                 self.solved = True
#                 # print(self.x, self.y, self.score, targx/self.x)
#                 self.score = self.score * (targx//self.x)

#         if self.x > self.targx or self.y > self.targy:
#             # print("scrapping")
#             self.solved = True
#             self.score = 0
#             # return 0

#     @property
#     def calcmult(self):
#         val = self.targx - self.x
#         if val < 10000:
#             return 1
#         elif val < 100000:
#             return 10000
#         elif val < 1000000:
#             return 100000
#         elif val < 10000000:
#             return 1000000
#         elif val < 100000000:
#             return 10000000
#         elif val < 1000000000:
#             return 100000000
#         elif val < 10000000000:
#             return 1000000000
#         elif val < 100000000000:
#             return 10000000000
#         elif val < 1000000000000:
#             return 100000000000
#         else:
#             return 1000000000000
        

#     def next(self, ax, ay, bx, by):
#         # if not self.switched:
#         #     children = [
#         #         Node(self.x + ax * self.calcmult, self.y + ay * self.calcmult, self.targx, self.targy, self.score + 3 * self.calcmult, False),
#         #         Node(self.x + bx * self.calcmult, self.y + by * self.calcmult, self.targx, self.targy, self.score + 1 * self.calcmult, True)
#         #     ] 
#         # else:
#         #     children = [Node(self.x + bx * self.calcmult, self.y + by * self.calcmult, self.targx, self.targy, self.score + 1 * self.calcmult, True)]
            
#         if not self.switched:
#             children = []
#             for i in range(int(math.log10(max(self.targx - self.x, self.targy - self.y)))):
#             # for i in range(2):
#                 children.append(Node(self.x + ax * (10**i), self.y + ay * (10**i), self.targx, self.targy, self.score + 3 * (10**i), False))
#                 children.append(Node(self.x + bx * (10**i), self.y + by * (10**i), self.targx, self.targy, self.score + 1 * (10**i), True))
#             # children = [
#             #     Node(self.x + ax, self.y + ay, self.targx, self.targy, self.score + 3, False),
#             #     Node(self.x + bx, self.y + by, self.targx, self.targy, self.score + 1, True)
#             # ] 
#         else:
#             children = []
#             for i in range(int(math.log10(max(self.targx - self.x, self.targy - self.y)))):
#             # for i in range(int(math.log10(max(self.targx, self.targy))-2)):
#             # for i in range(2):
#             # children = [Node(self.x + bx, self.y + by, self.targx, self.targy, self.score + 1, True)]
#                 children.append(Node(self.x + bx * (10**i), self.y + by * (10**i), self.targx, self.targy, self.score + 1 * (10**i), True))
            

        
#         solves = [0 if not x.solved else x.score for x in children]
#         # solves = [x.next(ax, ay, bx, by) if not x.solved else x.score for x in children]
#         _scores = [x for x in solves if x != 0]
#         if len(_scores) != 0:
#             # print(_scores)
#             return min(_scores)
#         solves = [x.next(ax, ay, bx, by) if not x.solved else 0 for x in children]
#         _scores = [x for x in solves if x != 0]
#         return min(_scores) if len(_scores) != 0 else 0
#         # if min(_scores) == 81: 
#         #     print(_scores)
#         # return min(_scores) if len(_scores) != 0 else 0


class Puzzle:
    def __init__(self, a_x_inc, a_y_inc, b_x_inc, b_y_inc, targ_x, targ_y):
        self.a_x_inc = a_x_inc
        self.a_y_inc = a_y_inc
        self.b_x_inc = b_x_inc
        self.b_y_inc = b_y_inc
        self.targ_x = targ_x
        self.targ_y = targ_y

        # self.max_divisor = 1
        # for i in range(1, 10001):
        #     if self.targ_x % i == 0 and self.targ_y % i == 0 and min(self.targ_x, self.targ_y)/i > max(self.a_x_inc, self.a_y_inc, self.b_x_inc, self.b_y_inc):
        #         self.max_divisor = i

        # print(self.max_divisor)

        # self.targ_x = self.targ_x / self.max_divisor
        # self.targ_y = self.targ_y / self.max_divisor

        # print(self.targ_x, self.targ_y)

    # def solve(self):
    #     common_factors = []
    #     for i in range(1, int(min(self.targ_x ** 0.5, self.targ_y ** 0.5))):
    #         if self.targ_x % i ==  0 and self.targ_y % i == 0:
    #             common_factors.append(i)

    #     # print(common_factors)
    #     # if max(common_factors) < 10:
    #         # return 0
    #     for i in range(len(common_factors) - 1, -1, -1):
    #         # print(common_factors[i])
    #         start = Node(0, 0, self.targ_x / common_factors[i], self.targ_y / common_factors[i], 0, False)
    #         r = start.next(self.a_x_inc, self.a_y_inc, self.b_x_inc, self.b_y_inc)
    #         if r != 0:
    #             return r * common_factors[i]
    #     return 0
        
class PuzzleV2(Puzzle):
    def solve(self):
        a = (self.b_y_inc * self.targ_x - self.b_x_inc * self.targ_y) / (self.a_x_inc * self.b_y_inc - self.a_y_inc * self.b_x_inc)
        b = (self.a_x_inc * self.targ_y - self.a_y_inc * self.targ_x) / (self.a_x_inc * self.b_y_inc - self.a_y_inc * self.b_x_inc)
       
        return 3 * a + b if a == int(a) and b == int(b) else 0

def part_1(lines):
    i = 0
    puzzles = []
    while i < len(lines):
        puzzles.append(
            PuzzleV2(
                int(lines[i].split("+")[1].split(",")[0]),
                int(lines[i].split("+")[2]),
                int(lines[i + 1].split("+")[1].split(",")[0]),
                int(lines[i + 1].split("+")[2]),
                int(lines[i + 2].split("=")[1].split(",")[0]),
                int(lines[i + 2].split("=")[2])
            )
        )
        i += 4

    total = 0
    for puzzle in puzzles:
        total += puzzle.solve()
    return total


def part_2(lines):
    i = 0
    puzzles = []
    while i < len(lines):
        puzzles.append(
            PuzzleV2(
                int(lines[i].split("+")[1].split(",")[0]),
                int(lines[i].split("+")[2]),
                int(lines[i + 1].split("+")[1].split(",")[0]),
                int(lines[i + 1].split("+")[2]),
                int(lines[i + 2].split("=")[1].split(",")[0]) + 10000000000000,
                int(lines[i + 2].split("=")[2]) + 10000000000000
            )
        )
        i += 4

    total = 0
    for puzzle in puzzles:
        total += puzzle.solve()

    return total

aoc.aoc_run("files/full/day13.txt", "files/example/day13_example.txt", part_1, 480)
aoc.aoc_run("files/full/day13.txt", "files/example/day13_example.txt", part_2, 875318608908)