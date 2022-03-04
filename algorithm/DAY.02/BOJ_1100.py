board = [list(input()) for _ in range(8)]

print(board)

chess = 0

for i in range(8): # 행
    for j in range(8): # 열
        if i % 2 == 1 and j % 2 == 1 and board[i][j] == 'F': # 홀수
            chess += 1
        if i % 2 == 0 and j % 2 == 0 and board[i][j] == 'F': # 짝수
            chess += 1

        #if i % 2 == j % 2 and board[i][j] == 'F': # 조금더 간편한 코드

print(chess)

#########################################
# 생각 과정
# - 짝수행, 홀수행, 짝수열, 홀수열 나누기 
# - board를 순회하여 'F'를 찾는 방법에서 막힘
#
# 올바른 풀이 과정 방향
# - 짝수열의 짝수행은 모두 하얀칸
# - 홀수열의 홀수행은 모두 하얀칸
# - 모든칸을 순회하면서 F가 있는지 찾기
##########################################