import aoc

def part_1(lines):
    # I am not using a regex

    l = "".join(lines)

    total = 0

    # 1. Split by mul
    ops = l.split("mul")

    # 2. Go through the ops
    if not l.startswith("mul"):
        ops.pop(0)

    for op in ops:
        if not op.startswith("("):
            continue
        op = op[1:]
        _br = op.split(")")[0]

        try:
            _nums = [int(x) for x in _br.split(",")]
        except ValueError:
            continue
        
        try:
            assert len(_nums) == 2
        except AssertionError:
            continue
    
        total += _nums[0] * _nums[1]

    return total

def part_2(lines):
    l = "".join(lines)

    ops_splits = l.split("don't()")
    do_splits = [ops_splits[0], *["".join(x.split("do()")[1:]) if "do()" in x else "" for x in ops_splits[1:]]]
    total = 0
    for ops in do_splits:
        total += part_1([ops])

    return total

aoc.aoc_run("files/full/day03.txt", "files/example/day03a_example.txt", part_1, 161)
aoc.aoc_run("files/full/day03.txt", "files/example/day03b_example.txt", part_2, 48)