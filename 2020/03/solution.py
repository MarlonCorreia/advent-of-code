
with open("input.txt") as f:
    data = [x.strip() for x in f.readlines()]

def count_trees(step_right, step_down):
    x = 0
    y = 0
    count = 0
    while y < len(data):
        count += data[y][x % len(data[0])] == '#'
        x += step_right
        y += step_down
    return count


print(count_trees(3, 1)) # part 1

print(count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2)) # part 2