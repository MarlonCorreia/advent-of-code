
def resolve(board, days):
    n_board = [0 for _ in range(0, 9)]
    for _ in range(0, days):
        n_board[0] = board[1]
        n_board[1] = board[2]
        n_board[2] = board[3]
        n_board[3] = board[4]
        n_board[4] = board[5]
        n_board[5] = board[6] 
        n_board[6] = board[7] + board[0]
        n_board[7] = board[8]
        n_board[8] = board[0]

        board = n_board
        n_board = [0 for x in range(0, 9)]
    
    print(sum(board))

 
with open('input.txt') as f:
    board = [0 for _ in range(0, 9)]
    for idx in f.read().split(','):
        board[int(idx)] += 1    

    p1 = resolve(board, 80)
    p2 = resolve(board, 256)