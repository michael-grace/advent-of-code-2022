import aoc

def part_1(lines):
    blocks = []
    for i in range(len(lines[0])):
        if i % 2 == 0:
            for _ in range(int(lines[0][i])):
                blocks.append(i / 2)
        else:
            for _ in range(int(lines[0][i])):
                blocks.append(".")

    for i in range(len(blocks) - 1, -1, -1):
        if blocks[i] == ".": continue
        first_dot = blocks.index(".")
        if first_dot > i: continue
        blocks[first_dot] = blocks[i]
        blocks[i] = "."

    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] == ".": continue
        checksum += i * int(blocks[i])

    return checksum


def part_2(lines):
    blocks = []
    for i in range(len(lines[0])):
        if i % 2 == 0:
            for _ in range(int(lines[0][i])):
                blocks.append(i // 2)
        else:
            for _ in range(int(lines[0][i])):
                blocks.append(".")

    block_length = 1
    for i in range(len(blocks) - 1, -1, -1):
        if blocks[i] == ".": continue
        if i == 0: continue

        if blocks[i] == blocks[i-1]:
            block_length += 1
            continue


        first_gap = "".join(["." if x == "." else "0" for x in blocks]).find("." * block_length)
        
        if first_gap == -1:
            block_length = 1
            continue

        if first_gap > i:
            block_length = 1
            continue
        
        for j in range(first_gap, first_gap + block_length):
            blocks[j] = blocks[i]

        for j in range(i, i + block_length):
            blocks[j] = "."

        block_length = 1

    checksum = 0
    for i in range(len(blocks)):
        if blocks[i] == ".": continue
        checksum += i * int(blocks[i])

    return checksum

aoc.aoc_run("files/full/day09.txt", "files/example/day09_example.txt", part_1, 1928)
aoc.aoc_run("files/full/day09.txt", "files/example/day09_example.txt", part_2, 2858)