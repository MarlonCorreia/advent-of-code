
dic = {}
my_bag = "shiny gold"

with open("input.txt") as f:
    for line in f:
        if "no other" in line:
            l = line.split("contain")[0].split(",")[0].rsplit()
            dic[l[0] + " " + l[1]] = set({})
            continue

        l = line.split("contain")[0].split(",")[0].rsplit()
        dic[l[0] + " " + l[1]] = set({})

        for x in line.split("contain")[1].split(","):
            dic[l[0] + " " + l[1]].add(x.strip().split()[1] + " " + x.strip().split()[2])
        



def part1(group, query):
    found = []
    for k in group.keys():
        if query in dic[k]:
            found.append(k)
            found.extend(part1(group, k))
    return found
            



res = part1(dic, my_bag)
print(len(set(res)))