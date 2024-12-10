import aoc

def part_1(lines):
    grid = [[int(x) for x in y] for y in lines]
    reachable = 0

    max_x = len(grid[0])
    max_y = len(grid)

    def _walk(x, y, required):
        if required == 9:
            return {(x, y)}

        def _in_grid(_x, _y):
            return _x >= 0 and _y >= 0 and _x < max_x and _y < max_y

        reachables = set()
        if _in_grid(x + 1, y) and grid[y][x+1] == required + 1: reachables = reachables.union(_walk(x + 1, y, required + 1))
        if _in_grid(x - 1, y) and grid[y][x-1] == required + 1: reachables = reachables.union(_walk(x - 1, y, required + 1))
        if _in_grid(x, y + 1) and grid[y+1][x] == required + 1: reachables = reachables.union(_walk(x, y + 1, required + 1))
        if _in_grid(x, y - 1) and grid[y-1][x] == required + 1: reachables = reachables.union(_walk(x, y - 1, required + 1))

        return reachables
        
    for gy in range(len(grid)):
        for gx in range(len(grid[gy])):
            if grid[gy][gx] == 0:
                reachable += len(_walk(gx, gy, 0))

    return reachable

def part_2(lines):
    grid = [[int(x) for x in y] for y in lines]
    reachable = 0

    max_x = len(grid[0])
    max_y = len(grid)

    def _walk(x, y, required):
        if required == 9:
            return 1

        def _in_grid(_x, _y):
            return _x >= 0 and _y >= 0 and _x < max_x and _y < max_y

        reachables = 0
        if _in_grid(x + 1, y) and grid[y][x+1] == required + 1: reachables += _walk(x + 1, y, required + 1)
        if _in_grid(x - 1, y) and grid[y][x-1] == required + 1: reachables += _walk(x - 1, y, required + 1)
        if _in_grid(x, y + 1) and grid[y+1][x] == required + 1: reachables += _walk(x, y + 1, required + 1)
        if _in_grid(x, y - 1) and grid[y-1][x] == required + 1: reachables += _walk(x, y - 1, required + 1)

        return reachables
        
    for gy in range(len(grid)):
        for gx in range(len(grid[gy])):
            if grid[gy][gx] == 0:
                reachable += _walk(gx, gy, 0)

    return reachable

aoc.aoc_run("files/full/day10.txt", "files/example/day10_example.txt", part_1, 36)
aoc.aoc_run("files/full/day10.txt", "files/example/day10_example.txt", part_2, 81)