
def win(grids, s=False):
    if s:
        wins = []
        for idx, g in enumerate(grids):
            if g.get('win'):
                continue
            for grid in g.get('board'):
                l = [x for x in grid if x]
                if not l:
                    wins.append(idx)
        return wins        
    else:
        for idx, g in enumerate(grids):
            for grid in g:
                l = [x for x in grid if x]
                if not l:
                    return idx
    return None

def count_rest(grid): 
    n = 0
    for x in range(0, int(len(grid) / 2)):
        n += sum(grid[x])
    return n


def part1(plays, grids):
    for play in plays: 
        for idx, g in enumerate(grids):
            for idx1, grid in enumerate(g):
                for idx2, gr in enumerate(grid):
                    if gr == play:
                        grids[idx][idx1][idx2] = 0

        w = win(grids)
        if w:
            n = count_rest(grids[w])
            return n * play  

def part2(plays, grids):
    grids = [{"win": False, "board": x} for x in grids]
    
    for play in plays: 
        for idx, g in enumerate(grids):
            for idx1, grid in enumerate(g.get('board')):
                for idx2, gr in enumerate(grid):
                    if gr == play:
                        grids[idx].get('board')[idx1][idx2] = 0

        wins = win(grids, s=True)
        if wins:
            for w in wins: grids[w]['win'] = True
            d = [1 for x in grids if x.get('win') == False]
            if not d:
                n = count_rest(grids[wins[-1]].get('board'))
                return n * play  
              


with open('input.txt') as f:
    i = 0
    plays = []
    grids = []
    cur = []

    for line in f.readlines():
        if i == 0:
            plays = [int(x) for x in line.strip().split(',')]    
            i += 1
        else:
            if line == '\n':
                if cur:
                    tmp = []
                    for x in range(0, len(cur)):
                        col = [c[x] for c in cur]
                        tmp.append(col)
                    grids.append(cur + tmp)
                cur = []
            else:
                line = [int(x) for x in line.strip().split(' ') if x]
                cur.append(line) 
    tmp = []
    for x in range(0, len(cur)):
        col = [c[x] for c in cur]
        tmp.append(col)
    grids.append(cur + tmp)


    p1 = part1(plays, grids)
    p2 = part2(plays, grids)
    
    print(f"Part1: {p1}")
    print(f"Part2: {p2}")
