# 보관 후 하루 지나면 상, 하, 좌, 우 -> 토마토가 같이 익음
# 1 - 익은 토마토
# 2 - 익지 않은 토마토
# -1 - 토마토가 들어있지 않은 칸

import sys 
input = lambda: sys.stdin.readline().rstrip()

# 상, 하, 좌, 우 탐색
def search(x, y):

    if x < 0 or x >= m or y < 0 or y >= n:
        return

    if tomato_box[x][y] == 0: # 탐색한 배추는 0으로 갱신
        tomato_box[x][y] == 1

    # 동서남북 탐색
    search(x+1, y)
    search(x, y+1)
    search(x-1, y)
    search(x, y-1)

    return

# 입력받기
m,n= map(int, input().split())
tomato_box = [list(map(int, input().split())) for _ in range(n)]
cnt = 0 

for i in range(n):
    for j in range(m):
        if tomato_box[i][j] == 1:
            search(i, j)
            cnt += 1
print(cnt)
