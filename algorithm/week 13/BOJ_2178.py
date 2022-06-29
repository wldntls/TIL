# 1: 이동 가능
# 0: 이동 불가능

import sys 
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def bfs(x, y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 이동 불가능한 경우 무시
            if matrix[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리를 기록
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append((nx, ny))

    return matrix[n-1][m-1]


n, m = map(int, input().split())
matrix = [list(map(int,input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))