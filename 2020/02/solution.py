
RESP_1 = 0
RESP_2 = 0

def part1(letter, passw, min, max):
    global RESP_1
    if min <= passw.count(letter) and max >= passw.count(letter):
        RESP_1 = RESP_1 + 1


def part2(letter, passw, min, max):
    global RESP_2
    if (passw[min - 1] == letter and passw[max - 1] != letter) or (passw[min - 1] != letter and passw[max - 1] == letter):
        RESP_2 = RESP_2 + 1


if __name__ == "__main__":
    with open("input.txt") as f:
        for line in f.readlines():
            letter = line.split()[1].strip(":")
            passw = line.split()[2]
            min = int(line.split()[0].split("-")[0])
            max = int(line.split()[0].split("-")[1])
        
            part1(letter, passw, min, max)
            part2(letter, passw, min, max)

    print(RESP_1)
    print(RESP_2)