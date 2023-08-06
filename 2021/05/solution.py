

def part1(points):
    grid = [[0 for _ in range(0, 1000)] for _ in range(0, 1000)]

    for point in points:
        x1, x2, y1, y2 = point
        if x1 == x2 or y1 == y2:
            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2) + 1):
                    grid[i][x1] += 1
            if y1 == y2:
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    grid[y1][i] += 1
    
    res = sum([1 for x in grid for y in x if y >= 2])
    return res


def part2(points):
    grid = [[0 for _ in range(0, 1000)] for _ in range(0, 1000)]

    for point in points:
        x1, x2, y1, y2 = point
        if x1 == x2 or y1 == y2:
            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2) + 1):
                    grid[i][x1] += 1
            if y1 == y2:
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    grid[y1][i] += 1
        else: 
            xs = range(min(x1, x2), max(x1, x2) + 1) if x1 <= x2 else reversed(range(min(x1, x2), max(x1, x2) + 1))
            ys = range(min(y1, y2), max(y1, y2) + 1) if y1 <= y2 else reversed(range(min(y1, y2), + max(y1, y2) + 1))

            for i,j in zip(xs, ys):
                grid[j][i] += 1

    res = sum([1 for x in grid for y in x if y >= 2])
    return res


with open('input.txt') as f:
    points = []

    for line in f.readlines():
        p1, p2 = line.strip().split('->')
        x1, y1 = [int(x) for x in p1.split(',')]
        x2, y2 = [int(x) for x in p2.split(',')]
        points.append([x1, x2, y1, y2])
    
    p1 = part1(points)
    p2 = part2(points)

    print(f"Part1 {p1}")
    print(f"Part2 {p2}")