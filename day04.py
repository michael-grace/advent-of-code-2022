import aoc

def part_1(lines):
    def _check_xmas(start_x, start_y, x_del, y_del):
        try:
            if lines[y][x] != "X":
                return False
            if (y + y_del < 0 or x + x_del < 0) or lines[y+y_del][x+x_del] != "M":
                return False
            if (y + 2*y_del < 0 or x + 2*x_del < 0) or lines[y+2*y_del][x+2*x_del] != "A":
                return False
            if (y + 3*y_del < 0 or x + 3*x_del < 0) or lines[y+3*y_del][x+3*x_del] != "S":
                return False
        except IndexError:
            return False
        
        return True

    count = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] != "X":
                continue
            
            count += sum([
                _check_xmas(x, y, x_del, y_del) for x_del in [-1, 0, 1] for y_del in [-1, 0, 1]
            ])

    return count

def part_2(lines):
    count = 0
    for y in range(1, len(lines) - 1):
        for x in range(1, len(lines) - 1):
            if lines[y][x] != "A":
                continue
                
            if ((lines[y-1][x-1] == "M" and lines[y+1][x+1] == "S") or \
                (lines[y-1][x-1] == "S" and lines[y+1][x+1] == "M")) and \
                ((lines[y-1][x+1] == "M" and lines[y+1][x-1] == "S") or \
                 (lines[y-1][x+1] == "S" and lines[y+1][x-1] == "M")):
                 count += 1

    return count

aoc.aoc_run("files/full/day04.txt", "files/example/day04_example.txt", part_1, 18)
aoc.aoc_run("files/full/day04.txt", "files/example/day04_example.txt", part_2, 9)
            
