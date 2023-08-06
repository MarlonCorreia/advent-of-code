from collections import Counter

def part1(file):
    qtd = 0 
    for line in file:
        line = set(line.replace("\n", ""))    
        qtd += len(line) 
        
    return qtd

def part2(file):
    qtd = 0
    for line in file:
        commom_ids = [item for item, repetition in Counter([val for x in line.split("\n") for val in x]).items() if repetition == len(line.split("\n"))]
        qtd += len(commom_ids)

    return qtd

if __name__ == "__main__":
    with open("input.txt") as f:
        file = f.read().split("\n\n")
        solution_1 = part1(file)
        solution_2 = part2(file)

    print(solution_1)
    print(solution_2)

 
