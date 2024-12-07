import sys

day = sys.argv[1]

with open(f"files/example/day{day}_example.txt", "w"):
    pass

with open(f"files/full/day{day}.txt", "w"):
    pass

with open(f"day{day}.py", "w") as f:
    f.write("import aoc\n\n")
    f.write("def part_1(lines):\n\n")
    f.write("# def part_2(lines):\n\n")
    f.write(f"aoc.aoc_run(\"files/full/day{day}.txt\", \"files/example/day{day}_example.txt\", part_1, FILL_OUT)\n")
    f.write(f"#aoc.aoc_run(\"files/full/day{day}.txt\", \"files/example/day{day}_example.txt\", part_2, FILL_OUT)")