import aoc

def part_1(lines):
    safe = 0

    for line in lines:
        _line = [int(x) for x in line.split(" ")]
        
        if _line[0] == _line[1]:
            continue
        
        increasing = _line[0] < _line[1]

        unsafe = False
        for i in range(len(_line) - 1):
            if increasing and _line[i] >= _line[i+1]:
                unsafe = True
                break

            if not increasing and _line[i] <= _line[i+1]:
                unsafe = True
                break

            if abs(_line[i] - _line[i+1]) > 3:
                unsafe = True
                break

        if not unsafe:
            safe += 1
    
    return safe

def part_2(lines):
    safe = 0

    for line in lines:
        _full_line = [int(x) for x in line.split(" ")]
        _poss = [[*_full_line[:x], *_full_line[x+1:]] for x in range(len(_full_line))]
        _poss.append(_full_line)
        
        valid = False
        for _line in _poss:

            if _line[0] == _line[1]:
                continue
            
            increasing = _line[0] < _line[1]

            unsafe = False
            for i in range(len(_line) - 1):
                if increasing and _line[i] >= _line[i+1]:
                    unsafe = True
                    break

                if not increasing and _line[i] <= _line[i+1]:
                    unsafe = True
                    break

                if abs(_line[i] - _line[i+1]) > 3:
                    unsafe = True
                    break

            if not unsafe:
                valid = True
                break

        if valid:
            safe += 1
    
    return safe

aoc.aoc_run("files/full/day02.txt", "files/example/day02_example.txt", part_1, 2)
aoc.aoc_run("files/full/day02.txt", "files/example/day02_example.txt", part_2, 4)
