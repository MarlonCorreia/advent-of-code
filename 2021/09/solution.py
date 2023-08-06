from math import prod


def find_bigger(y, x, points, res, been):
    cur = points[y][x]
    if (y, x) in been: return res - 1
    
    up = None if (y-1) < 0 else points[y-1][x]
    down = None if (y+1) > len(points) -1 else points[y+1][x]
    right = None if (x+1) > len(points[0]) -1 else points[y][x+1]
    left = None if (x-1) < 0 else points[y][x-1]    

    if up != None and up > cur and up != 9:
        res = find_bigger(y-1, x, points, res + 1, been)
        been.append((y-1,x))
    if down != None and down > cur and down != 9:
        res = find_bigger(y+1, x, points, res + 1, been)
        been.append((y+1,x))
    if right != None and right > cur and right != 9:
        res = find_bigger(y, x+1, points, res + 1, been)
        been.append((y,x+1))
    if left != None and left > cur and left != 9:
        res = find_bigger(y, x-1, points, res + 1, been)
        been.append((y,x-1))

    return res

def part1(points):
    lows = []
    for y, row in enumerate(points):
        for x, val in enumerate(row):
            up = None if (y-1) < 0 else points[y-1][x]
            down = None if (y+1) > len(points) -1 else points[y+1][x]
            right = None if (x+1) > len(points[0]) -1 else points[y][x+1]
            left = None if (x-1) < 0 else points[y][x-1]

            a = [x for x in [up, down, right, left] if x != None]

            if val < min(a):
                lows.append(val)

    return sum([x+1 for x in lows])

def part2(points):

    res = []
    for y, row in enumerate(points):
        for x, val in enumerate(row):
            up = None if (y-1) < 0 else points[y-1][x]
            down = None if (y+1) > len(points) -1 else points[y+1][x]
            right = None if (x+1) > len(points[0]) -1 else points[y][x+1]
            left = None if (x-1) < 0 else points[y][x-1]

            a = [x for x in [up, down, right, left] if x != None]

            if val < min(a):
                r = find_bigger(y, x, points, 1, [])
                res.append(r)

    return prod(sorted(res, reverse=True)[0:3])
    

with open('input.txt') as f:
    points = []

    for line in f.readlines():
        l = []
        for point in line.strip():
            l.append(int(point))
        points.append(l)
    
    p1 = part1(points)
    p2 = part2(points)

    print(f"Part1 {p1}")
    print(f"Part2 {p2}")