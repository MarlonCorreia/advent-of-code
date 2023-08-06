from statistics import median

def part1(lines, inversed_char):
    score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    final_score = 0
    for line in lines:
        stack = []
        for c in  line:
            if c in '([{<': stack.append(c)
            else:
                if not stack: return final_score             
                k = stack[-1]
                expected_inverse = inversed_char.get(k)
                if c != expected_inverse:
                    final_score += score.get(c)
                    break
                else:
                    stack.pop()
    return final_score

def part2(lines, inversed_char):
    score = {')': 1, ']': 2, '}': 3, '>': 4}
    final_score = []

    for line in lines:
        cur_score = 0
        stack = []
        for c in  line:
            if c in '([{<': stack.append(c)
            else:
                if not stack: break
                k = stack[-1]

                expected_inverse = inversed_char.get(k)
                if c != expected_inverse:
                    stack = []
                    break
                else:
                    stack.pop()
        if not stack: continue

        r = [inversed_char.get(x) for x in reversed(stack)]   
        for x in r:
            cur_score = (cur_score * 5) + score.get(x)
        final_score.append(cur_score)

    return median(final_score)


with open('input.txt') as f:
    lines = []
    for line in f.readlines():
        lines.append(line.strip())
    inversed_char = {'(':')', ')':'(', '[': ']', ']': '[', '{': '}', '}': '{', '<': '>', '>': '<'}
  
    p1 = part1(lines, inversed_char)
    p2 = part2(lines, inversed_char)
    
    print(f'Part1 {p1}')
    print(f'Part2 {p2}')
