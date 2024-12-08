import aoc

def part_1(lines):
    antennas = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == ".": continue
            try:
                antennas[lines[y][x]].append((x, y))
            except KeyError:
                antennas[lines[y][x]] = [(x, y)]

    antinodes = set()
    for ants in antennas.values():
        for ant1 in ants:
            for ant2 in ants:
                if ant1 == ant2: continue

                del_x = ant2[0] - ant1[0]
                del_y = ant2[1] - ant1[1]

                new_nodes = [
                    (ant1[0] - del_x, ant1[1] - del_y),
                    (ant2[0] + del_x, ant2[1] + del_y)
                ]

                for node in new_nodes:
                    if not (node[0] < 0 or node[1] < 0 or node[0] >= len(lines[0]) or node[1] >= len(lines)):
                        antinodes.add(node)

    return len(antinodes)

def part_2(lines):
    antennas = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == ".": continue
            try:
                antennas[lines[y][x]].append((x, y))
            except KeyError:
                antennas[lines[y][x]] = [(x, y)]

    antinodes = set()
    for ants in antennas.values():
        for ant1 in ants:
            for ant2 in ants:
                if ant1 == ant2: continue

                del_x = ant2[0] - ant1[0]
                del_y = ant2[1] - ant1[1]

                new_nodes = [
                    (ant1[0] + i * del_x, ant1[1] + i * del_y)
                    for i in range(-len(lines), len(lines))
                ]

                for node in new_nodes:
                    if not (node[0] < 0 or node[1] < 0 or node[0] >= len(lines[0]) or node[1] >= len(lines)):
                        antinodes.add(node)

    return len(antinodes)

aoc.aoc_run("files/full/day08.txt", "files/example/day08_example.txt", part_1, 14)
aoc.aoc_run("files/full/day08.txt", "files/example/day08_example.txt", part_2, 34)