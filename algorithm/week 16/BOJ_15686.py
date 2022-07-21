# https://ssssol.tistory.com/72
# 0 = 빈칸
# 1 = 집
# 2 = 치킨집

import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken= []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append([i, j])
        if city[i][j] == 1:
            house.append([i, j])
# print("house", house, len(house))
# print("chicken", chicken, len(chicken))
comb = list(combinations(chicken, m))
# print(comb, len(comb))

distance = []
result = []

# 모든 치킨 집과 모든 집 사이의 거리를 구하고 가장 작은 값을 distance에 저장
# 각 조합별 도시의 치킨 거리의 최소값을 Distance에 저장
for i in range(len(comb)):
    for h in house:
        d = []
        for j in range(m):
            d.append(abs(h[0] - comb[i][j][0]) + abs(h[1] - comb[i][j][1]))
        distance.append(min(d))

# print(distance, len(distance))

# 도시의 치킨 거리 = 모든 집의 치킨 거리의 합
# distance에 있는 값 차례로 더하다가 갯수가 맞으면 그 합을 result에 넣기
# 그리고 result의 최솟값 구하기
distance_sum = 0
for i in range(len(distance)):
    distance_sum += distance[i]
    if (i + 1) % len(house) == 0:
        result.append(distance_sum)
        distance_sum = 0

print(min(result))