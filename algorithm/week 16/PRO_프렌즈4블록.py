# https://my-coding-notes.tistory.com/226

def solution(m, n, board):
    board = [list(i) for i in board]
    answer = 0
    check = set()
    while True:
        for i in range(m-1):
            for j in range(n-1):
                t = board[i][j]
                if t == []:
                    continue
                
                if board[i+1][j] == board[i][j+1] == board[i+1][j+1] == t:
                    check.add((i,j))
                    check.add((i+1, j))
                    check.add((i, j+1))
                    check.add((i+1, j+1))
        
        if check:
            answer += len(check)
            for i, j in check:
                board[i][j] = []
            check = set()
        else:
            return answer

        print(board)
        
        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and not board[i+1][j]:
                        print(board[i][j])
                        board[i+1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved == 0:
                break

m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(solution(m, n, board))