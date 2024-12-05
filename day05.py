import aoc
import functools

def common(lines):
    rules = []
    manuals = []

    reachedBlank = False
    for line in lines:
        if line == "":
            reachedBlank = True
            continue

        if reachedBlank:
            manuals.append([int(x) for x in line.split(",")])
        else:
            rules.append([int(x) for x in line.split("|")])

    return rules, manuals

def _check_rule(rule, manual):
    try:
        lft_pos = manual.index(rule[0])
        rght_pos = manual.index(rule[1])
    except ValueError:
        return True

    if lft_pos < rght_pos:
        return True

    return False


def part_1(lines):
    rules, manuals = common(lines)

    total = 0
    for manual in manuals:
        if all([_check_rule(r, manual) for r in rules]):
            total += manual[len(manual) // 2]

    return total

def part_2(lines):
    rules, manuals = common(lines)

    def _sorter(left, right):
        if [left, right] in rules:
            return -1
        
        if [right, left] in rules:
            return 1

        return -1

    total = 0
    for manual in manuals:
        if not all([_check_rule(r, manual) for r in rules]):
            _new = sorted(manual, key=functools.cmp_to_key(_sorter))
            total += _new[len(_new)//2]

    return total

aoc.aoc_run("files/full/day05.txt", "files/example/day05_example.txt", part_1, 143)
aoc.aoc_run("files/full/day05.txt", "files/example/day05_example.txt", part_2, 123)
    