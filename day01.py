import aoc

def common(lines):
    lst_l = []
    lst_r = []

    for line in lines:
        _line_split = line.split(" ")
        lst_l.append(int(_line_split[0]))
        lst_r.append(int(_line_split[-1]))

    lst_l.sort()
    lst_r.sort()

    assert len(lst_l) == len(lst_r)

    return lst_l, lst_r

def part_a(lines):
    lst_l, lst_r = common(lines)

    total_distance = 0
    for i in range(len(lst_l)):
        total_distance += max(lst_l[i], lst_r[i]) - min(lst_l[i], lst_r[i])

    return total_distance

def part_b(lines):
    lst_l, lst_r = common(lines)

    sim_score = 0

    for x in lst_l:
        _count = 0
        for y in lst_r:
            if y > x:
                break
            elif y == x:
                _count += 1

        sim_score += _count * x

    return sim_score

aoc.aoc_run("files/full/day01.txt", "files/example/day01_example.txt", part_a, 11)
aoc.aoc_run("files/full/day01.txt", "files/example/day01_example.txt", part_b, 31)