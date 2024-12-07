import aoc

def part_1(lines):
    valid_count = 0
    for line in lines:
        answer = int(line.split(":")[0])
        values = [int(x) for x in line.split(": ")[1].split(" ")]

        determinator = 2 ** (len(values) - 1)
        for i in range(determinator):
            calc_result = values[0]
            for vi in range(len(values)):
                if vi == 0: continue

                if i & (2 ** (vi -1 )) == 0:
                    calc_result += values[vi]
                elif i & (2 ** (vi -1)) == 2 ** (vi-1):
                    calc_result *= values[vi]
                else:
                    raise ValueError
            
            if calc_result == answer:
                valid_count += answer
                break

    return valid_count

def part_2(lines):
    def _ternary_bitwise_and_ish(val, three_to_power):
        def _numberToBase(n):
            # https://stackoverflow.com/a/28666223
            if n == 0:
                return [0]
            digits = []
            while n:
                digits.append(int(n % 3))
                n //= 3
            return digits[::-1]
        
        val3 = _numberToBase(val)

        try:
            return val3[-(three_to_power+1)]
        except IndexError:
            return 0

    valid_count = 0
    for line in lines:
        answer = int(line.split(":")[0])
        values = [int(x) for x in line.split(": ")[1].split(" ")]

        determinator = 3 ** (len(values) - 1)
        for i in range(determinator):
            calc_result = values[0]
            for vi in range(len(values)):
                if vi == 0: continue

                if _ternary_bitwise_and_ish(i, vi - 1) == 0:
                    calc_result += values[vi]
                elif _ternary_bitwise_and_ish(i, vi - 1) == 1:
                    calc_result *= values[vi]
                elif _ternary_bitwise_and_ish(i, vi - 1) == 2:
                    calc_result = int(f"{calc_result}{values[vi]}")
                else:
                    print(_ternary_bitwise_and_ish(i, 3 ** (vi - 1)))
                    raise ValueError
            
            if calc_result == answer:
                valid_count += answer
                break

    return valid_count

aoc.aoc_run("files/full/day07.txt", "files/example/day07_example.txt", part_1, 3749)
aoc.aoc_run("files/full/day07.txt", "files/example/day07_example.txt", part_2, 11387)