import aoc

def part_1(lines):
    stones = [int(x) for x in lines[0].split(" ")]

    for b in range(25):
        new_stones = []
        for i in range(len(stones)):
            if stones[i] == 0:
                new_stones.append(1)
            elif len(str(stones[i])) % 2 == 0:
                new_stones.append(int(str(stones[i])[:len(str(stones[i]))//2]))
                new_stones.append(int(str(stones[i])[len(str(stones[i]))//2:]))
            else:
                new_stones.append(stones[i] * 2024)
        stones = new_stones

    return len(stones)
    
def part_2(lines):
    stones = [int(x) for x in lines[0].split(" ")]
    
    heat_map = {}
    for i in stones:
        try:
            heat_map[i] += 1
        except KeyError:
            heat_map[i] = 1
    
    for i in range(75):
        new_hm = {}
        for k, v in heat_map.items():
            if k == 0:
                try:
                    new_hm[1] += v
                except KeyError:
                    new_hm[1] = v
            elif len(str(k)) % 2 == 0:
                try:
                    new_hm[int(str(k)[:len(str(k))//2])] += v
                except KeyError:
                    new_hm[int(str(k)[:len(str(k))//2])] = v

                try:
                    new_hm[int(str(k)[len(str(k))//2:])] += v
                except KeyError:
                    new_hm[int(str(k)[len(str(k))//2:])] = v
            else:
                try:
                    new_hm[k * 2024] += v
                except KeyError:
                    new_hm[k * 2024] = v
            heat_map = new_hm

    return sum(x for x in heat_map.values())

aoc.aoc_run("files/full/day11.txt", "files/example/day11_example.txt", part_1, 55312)
aoc.aoc_run("files/full/day11.txt", "files/example/day11_example.txt", part_2)