
# https://pacific-ocean.tistory.com/278

n, m = map(int, input().split())
s = [[0] * n for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    s[a - 1][b - 1] = 1
    s[b - 1][a - 1] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif s[i][k] and s[k][j]:
                if s[i][j] == 0:
                    s[i][j] = s[i][k] + s[k][j]
                else:
                    s[i][j] = min(s[i][j], s[i][k] + s[k][j])
result = 100000000
for i in range(n):
    sum = 0
    for j in range(n):
        sum += s[i][j]
    if result > sum:
        result = sum
        p = i
print(p + 1)


# https://claude-u.tistory.com/337

#입력
N, M = map(int, input().split())
friend_map = [[N for _ in range(N)] for _ in range(N)]

for _ in range(M):
    friend_A, friend_B = map(int, input().split())
    friend_map[friend_A-1][friend_B-1] = 1
    friend_map[friend_B-1][friend_A-1] = 1


#플로이드-워셜 알고리즘
for k in range(N): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(N):
        for j in range(N): 
            if i == j:
                friend_map[i][j] = 0 #자기 자신과는 친구가 되지 못한다
            else:
                friend_map[i][j] = min(friend_map[i][j],
                                       friend_map[i][k] + friend_map[k][j])


#출력
bacon = []
for row in friend_map:
    bacon.append(sum(row))
print(bacon.index(min(bacon)) + 1)