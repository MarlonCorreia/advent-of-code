TARGET = 2020

def part1():
    ids = {}
    with open("input.txt") as inputed_file:
        for line in inputed_file.readlines():
            line = int(line)
            ids[line] = line

            try:
                want = TARGET - line
                rest = ids[want]
                print(line * rest)
                break
            except:
                continue

def part2():
    ids = {}
    with open("input.txt") as inputed_file:
        for value in inputed_file.readlines():
            value = int(value)
            ids[value] = value

            for val in ids:
                try:
                    want = TARGET - value - val
                    rest = ids[want]
                    print(val * value * rest)
                    break
                except:
                    pass
                

if __name__ == "__main__":
    part1()
    part2()