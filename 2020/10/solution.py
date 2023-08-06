

def part1(data):
    one_j = 1
    three_j = 0 

    all_nu = [int(x.strip()) for x in data]
    all_nu.sort()
    l = len(all_nu) - 1

    for idx, numb in enumerate(all_nu):
        if idx == l:
            three_j += 1
            break
        if (all_nu[idx + 1] - numb) == 1:
            one_j += 1
        elif (all_nu[idx+1] - numb) == 3:
            three_j += 1 

    return one_j * three_j

if __name__=="__main__":
    with open("day-10/input.txt") as f:
        data = f.readlines()

        res_1 = part1(data)
        print(res_1)
