

seat_ids = []

with open("input.txt") as f:
    for line in f:

        max_row = [x for x in range(0, 128)]
        max_column = [x for x in range(0, 9)]
        
        seat = list(line.strip("\n"))

        # B = UPPER
        # F = LOWER

        for letter in seat[:7]:
            if letter == "B":
                div = len(max_row) / 2
                max_row = max_row[int(div):]
    
            if letter == "F":
                div = len(max_row) / 2
                max_row = max_row[:int(div)]
                
                
        # R = UPPER
        # L = LOWER

        for letter in seat[7:]:
            if letter == "R":
                div = len(max_column) / 2
                max_column = max_column[int(div):]
    
            if letter == "L":
                div = len(max_column) / 2
                max_column = max_column[:int(div)]
                    

        seat_ids.append((max_row[0] * 8) + max_column[0])

def greates_seat_id(seat_ids):
    return max(seat_ids)

def find_my_seat(seat_ids):
    final = []
    for ele in seat_ids:
        if not (ele + 1 in seat_ids and ele - 1 in seat_ids):
            final.append(ele)

    final.remove(max(final))
    final.remove(min(final))
    return max(final) - 1

if __name__ == "__main__":
    part_1 =  greates_seat_id(seat_ids)
    part_2 = find_my_seat(seat_ids)

    print(part_1)
    print(part_2)



    