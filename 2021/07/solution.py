from statistics import mean

def _triang_sum(n):
    number = 0
    for i in range(1, n+1):
        number += i
    return number

def part1(steps):
    l = []
    for x in set(steps):
        f = 0
        for v in steps:
            f += abs(x - v)
        l.append(f)
    
    return min(l)

def part2(steps):
    m = int(mean(steps))
    n = []
    for i in range(m, m+2):
        f = 0
        for v in steps:
            f += _triang_sum(abs(i-v))
        n.append(f)

    return min(n)



with open('input.txt') as f:
    steps = [int(x) for x in f.read().split(',')]

    p1 = part1(steps)
    p2 = part2(steps)
    
    print(f"Part1 {p1}")
    print(f"Part2 {p2}")
