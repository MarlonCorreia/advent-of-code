import copy

ACCUMULATOR = 0
acc = "acc"
jmp = "jmp"
nop = "nop"


def part1(instructions):
    ACCUMULATOR = 0
    idx = 0

    while(True):
        if instructions[idx]["visited"]:
            return ACCUMULATOR
        elif instructions[idx]["cmd"] == nop:
            instructions[idx]["visited"] = True
            idx += 1
        elif instructions[idx]["cmd"] == acc:
            op = int(instructions[idx]["op"])
            instructions[idx]["visited"] = True            
            ACCUMULATOR += op
            idx += 1
        elif instructions[idx]["cmd"] == jmp:
            instructions[idx]["visited"] = True
            idx += int(instructions[idx]["op"])

def interate_to_end(instruc_t):
    ACCUMULATOR = 0
    idx = 0

    while(True):
        if instruc_t[idx]["visited"]:
            return False
        elif instruc_t[idx]["cmd"] == nop:
            instruc_t[idx]["visited"] = True
            idx += 1
        elif instruc_t[idx]["cmd"] == acc:
            op = int(instruc_t[idx]["op"])
            instruc_t[idx]["visited"] = True            
            ACCUMULATOR += op
            idx += 1
        elif instruc_t[idx]["cmd"] == jmp:
            instruc_t[idx]["visited"] = True
            j = int(instruc_t[idx]["op"])
            idx += j

        if idx == len(instruc_t):
            return ACCUMULATOR

def part2(instructions):
    idx = 0
    
    while(True):
        if idx == len(instructions):
            return 
        elif instructions[idx]["cmd"] == nop:
            tmp_instruc = copy.deepcopy(instructions)
            tmp_instruc[idx]["cmd"] = jmp
            resp = interate_to_end(tmp_instruc)
            if resp == False:
                idx += 1
                continue
            else:
                return resp
        elif instructions[idx]["cmd"] == jmp:
            tmp_instruc = copy.deepcopy(instructions)
            tmp_instruc[idx]["cmd"] = nop
            resp = interate_to_end(tmp_instruc)
            if resp == False:
                idx += 1
                continue
            else:
                return resp
        
        idx += 1
        


if __name__ == "__main__":
    instructions = {}
    with open("day-8/input.txt") as f:
        i = 0
        for line in f.readlines():
            command, ope = line.split()
            instructions[i] = {
                "cmd": command,
                "op": ope,
                "visited": False
            }
            i += 1

    instructions_two = copy.deepcopy(instructions)
    print(part1(instructions))
    print(part2(instructions_two))