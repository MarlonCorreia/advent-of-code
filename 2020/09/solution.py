
def valid(last_25, number):
    for n in last_25:
        for m in last_25:
            if n + m == number:
                return True
    return False

def part1(all_lines):
    part1_res = 0
    last_25 = []
    qtd = 0
    for numb in all_lines:
        last_25.append(int(numb.split("\n")[0]))

        if qtd >= 25:
            res = valid(last_25[:25], last_25[-1])
            if res == False:
                part1_res = int(numb.strip())
                break
            last_25 = last_25[1:]
        qtd += 1
    
    return part1_res

def part2(all_lines, part1_solution):
    seq = []
    _max = 2
    stop = False
    
    while(not stop):
        for line in all_lines:
            numb = int(line.strip())
            seq.append(numb)

            if len(seq) > _max:
                seq = seq[1:]

            if len(seq) > 1 and sum(seq) == part1_solution:
                return min(seq) + max(seq)
        _max += 1
        seq = []



if __name__=="__main__":


    with open("day-9/inputs.txt") as f:
        all_lines = f.readlines()

        part1_solution = part1(all_lines)
        print(part1_solution)    
        
        part2_solution = part2(all_lines, part1_solution)
        print(part2_solution)
        
        