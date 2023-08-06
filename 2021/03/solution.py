from collections import Counter

def __most_commom(l, s=False):
    tmp = []
    for i in range(0, len(l[0])):
        col = []
        for line in l:
            col.append(line[i])

        c = Counter(col).most_common(2)
        
        if len(c) == 1 or c[0][1] != c[1][1]: 
            tmp.append(c[0][0])
        else:
            tmp.append('1')
        col = []
    return tmp

def part1(l):
    gam = eps = ''
    tmp = __most_commom(l)
    gam = ''.join(tmp)
    eps = ''.join(['0' if x=='1' else '1' for x in gam])
    return int(gam, 2) * int(eps, 2)
    

def part2(l):
    ox = l
    scr = l

    for idx in range(0, len(ox[0])):
        tmp = __most_commom(ox, s=True)
        ox = [x for x in ox if x[idx] == tmp[idx]]
        if len(ox) == 1: break
    
    for idx in range(0, len(scr[0])):
        tmp = __most_commom(scr)
        scr = [x for x in scr if x[idx] != tmp[idx]]
        if len(scr) == 1: break
        
    ox = int(''.join(ox), 2)
    scr = int(''.join(scr), 2)

    return ox * scr


with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

    p1 = part1(lines)
    p2 = part2(lines)

    print(f"Part 1 {p1}")
    print(f"Part 2 {p2}")