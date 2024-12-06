import aoc

def part_1(lines):
    grid = []
    current_guard_pos = []

    for i in range(len(lines)):
        line = lines[i]
        grid.append([x for x in line])

        if "^" in line:
            current_guard_pos = [line.find("^"), i]

    max_x = len(grid[0])
    max_y = len(grid)

    possible_guard_directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    guard_direction = 0

    while current_guard_pos[0] >= 0 and current_guard_pos[0] < max_x \
        and current_guard_pos[1] >= 0 and current_guard_pos[1] < max_y:
        grid[current_guard_pos[1]][current_guard_pos[0]] = "X"

        # try to take a step
        can_step = False
        while not can_step:
            try_step = [current_guard_pos[0] + possible_guard_directions[guard_direction][0],
                current_guard_pos[1] + possible_guard_directions[guard_direction][1]]
            if try_step[0] < 0 or try_step[0] >= max_x or \
                try_step[1] < 0 or try_step[1] >= max_y or \
                    grid[try_step[1]][try_step[0]] != "#":
                can_step = True
                current_guard_pos = try_step
                break

            guard_direction = (guard_direction + 1) % 4

    return sum([x.count("X") for x in grid])

def _run_guard(_grid, _current_guard_pos, max_x, max_y):
    # print("running func")
    # if p: print(*[[str(x) for x in y] for y in _grid], sep="\n")

    possible_guard_directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    guard_direction = 0

    while _current_guard_pos[0] >= 0 and _current_guard_pos[0] < max_x \
        and _current_guard_pos[1] >= 0 and _current_guard_pos[1] < max_y:
        # print(f"In: {_current_guard_pos}")
        if _grid[_current_guard_pos[1]][_current_guard_pos[0]] == guard_direction:
            # Guard is in loop
            # print(*[[str(x) for x in y] for y in _grid], sep="\n")
            # print("In Loop")
            return True

        _grid[_current_guard_pos[1]][_current_guard_pos[0]] = guard_direction

        # try to take a step
        can_step = False
        while not can_step:
            try_step = [_current_guard_pos[0] + possible_guard_directions[guard_direction][0],
                _current_guard_pos[1] + possible_guard_directions[guard_direction][1]]
            # print(f"Trying {try_step}")
            if try_step[0] < 0 or try_step[0] >= max_x or \
                try_step[1] < 0 or try_step[1] >= max_y or \
                    _grid[try_step[1]][try_step[0]] != "#":
                can_step = True
                # print("Can Step")
                _current_guard_pos = try_step
                # print(f"Step Now: {_current_guard_pos}")
                break
            
            can_step = False
            # print("Can't Step - Turning")
            guard_direction = (guard_direction + 1) % 4
        # print("Taking Next")
        # print(_current_guard_pos)
    
    # print("Returning False")
    # if p: print(*[[str(x) for x in y] for y in _grid], sep="\n")

    return False

def part_2(lines):
    grid = []
    current_guard_pos = []

    for i in range(len(lines)):
        line = lines[i]
        grid.append([x for x in line])

        if "^" in line:
            current_guard_pos = [line.find("^"), i]

    max_x = len(grid[0])
    max_y = len(grid)
    # print(max_x, max_y)

    
    # temp_grid = []
    count_loops = 0
    # raise ValueError(len(grid))
    for y in range(len(grid)):
        # temp_grid = []
        for x in range(len(grid[y])):
            temp_grid = []
            if grid[y][x] != ".":
                continue

            temp_grid.extend(grid[:y])
            temp_row = []
            temp_row.extend(grid[y][:x])
            temp_row.append("#")
            temp_row.extend(grid[y][x+1:])
            temp_grid.append(temp_row)
            temp_grid.extend(grid[y+1:])

            # _run_guard([[x for x in y] for y in temp_grid], current_guard_pos, max_x, max_y)
            # return 0
            # print(x, y)
            if _run_guard([[_x for _x in _y] for _y in temp_grid], current_guard_pos, max_x, max_y):
                count_loops += 1
                # return count_loops

    return count_loops

aoc.aoc_run("files/full/day06.txt", "files/example/day06_example.txt", part_1, 41)
aoc.aoc_run("files/full/day06.txt", "files/example/day06_example.txt", part_2, 6)