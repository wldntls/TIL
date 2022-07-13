# 방법 1(dfs)
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
map = [list(map(int, input())) for _ in range(n)]

result = [] # 단지내의 집의 수를 담을 리스트 -> 길이가 단지의 갯수
cnt = 0 # 단지내의 집의 수

def search(x, y):
    global cnt
    # 종료조건
    if x < 0 or x >= n or y < 0 or y >= n:
        return

    if map[x][y] == 0: # 탐색한 배추는 0으로 갱신
        return

    map[x][y] = 0
    cnt += 1

     # 동서남북 탐색
    search(x+1, y)
    search(x, y+1)
    search(x-1, y)
    search(x, y-1)

for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            search(i, j)
            result.append(cnt)
            cnt = 0

print(len(result))
for i in sorted(result):
    print(i)

# 방법 2(dfs)
# # 출력
# # 총 단지수 
# # 단지내 집수 오름차순 차례로
# import sys
# input = lambda: sys.stdin.readline().rstrip()

# n = int(input())
# map = [list(map(int, input())) for _ in range(n)]

# result = [] # 단지내의 집의 수를 담을 리스트 -> 길이가 단지의 갯수
# cnt = 0 # 단지내의 집의 수

# # 서 동 남 북
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# # 상, 하, 좌, 우 탐색
# def dfs(x, y):
#     global cnt
#     if x < 0 or x >= n or y < 0 or y >= n:
#         return False

#     if map[x][y] == 1: 
#         cnt += 1
#         map[x][y] = 0
#         for i in range(4):
#             dfs(x+dx[i], y+dy[i]) # 상하좌우를 탐색
#         return True
#     return False

# for i in range(n):
#     for j in range(n):
#         if dfs(i,j) == True: # 만약 모두 0으로 바뀌면 True를 return
#             result.append(cnt)
#             cnt = 0 # 다음 단지의 집의 갯수를 세기 위해 리셋

# print(len(result)) # 단지의 갯수
# result.sort()
# for i in result:
#     print(i)