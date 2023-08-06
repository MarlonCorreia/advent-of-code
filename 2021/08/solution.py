

def order(n):
    return ''.join(sorted(n))

def part1(m, digits):
    digits = [y for x in digits for y in x]
    r = [0 for _ in range(0, 10)]

    for d in digits:
        d = len(d)
        for idx, x in enumerate(m):
            if len(x) == d:
                r[idx] += 1

    return r[1] + r[4] + r[7] + r[8]

def part2(front, back):
    final = []
    for idx, f in enumerate(front):
        front = f 
        numbers = ['' for _ in range(0, 10)]

        for digit in front:
            if all([numbers[1], numbers[4], numbers[7], numbers[8]]): break

            elif len(digit) == 2:
                numbers[1] = order(digit)
            elif len(digit) == 4:
                numbers[4] = order(digit)
            elif len(digit) == 3:
                numbers[7] = order(digit)
            elif len(digit) == 7:
                numbers[8] = order(digit)
        
        for digit in front:
            if numbers[0]: break
            if len(digit) == 6:
                lone = set(numbers[1])
                lfour = set(numbers[4])
                if lone.issubset(set(digit)) and not lfour.issubset(set(digit)):
                    numbers[0] = order(digit)

        for digit in front:
            if numbers[6] and numbers[9]: break
            if len(digit) == 6 and order(digit) != order(numbers[0]):
                one = set(numbers[1])
                if one.issubset(digit):
                    numbers[9] = order(digit)
                else:
                    numbers[6] = order(digit)
        for digit in front:
            if all([numbers[2], numbers[3], numbers[5]]): break

            if len(digit) == 5:
                lsete = set(numbers[7])
                lnine = set(numbers[9])
                if lsete.issubset(set(digit)):
                    numbers[3] = order(digit)
                elif lnine.issuperset(set(digit)):
                    numbers[5] = order(digit)
                elif not lsete.issubset(set(digit)):
                    numbers[2] = order(digit)
        

        n = ''
        for digit in back[idx]:
            digit = order(digit)
            for idx, i in enumerate(numbers):
                if order(digit) == i:
                    n += str(idx)
                    break
        final.append(n)

    return sum([int(x) for x in final])

    
        
with open('input.txt') as f:
    m = [
        'abcefg',
        'cf',
        'acdeg', 
        'acdfg', 
        'bcdf', 
        'abdfg', 
        'abdefg', 
        'acf', 
        'abcdefg', 
        'abcdfg'
    ]

    front = []
    back = []
    for line in f.readlines():
        s, e = line.split('|')
        s = [x.strip() for x in s.split()]
        e = [x.strip() for x in e.split()]

        front.append(s)
        back.append(e)

    p1 = part1(m, back)
    p2 = part2(front, back)

    print(f"Part1 {p1}")
    print(f"Part2 {p2}")
        