board = [list(input()) for _ in range(8)]

print(board)

chess = 0

for i in range(8): # 행
    for j in range(8): # 열
        if i % 2 == 1 and j % 2 == 1 and board[i][j] == 'F': # 홀수
            chess += 1
        if i % 2 == 0 and j % 2 == 0 and board[i][j] == 'F': # 짝수
            chess += 1

print(chess)