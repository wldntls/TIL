# https://daimhada.tistory.com/181

# https://jokerldg.github.io/algorithm/2021/07/19/climb-stairs.html

import sys 

num = lambda: sys.stdin.readline().rstrip()

n = int(num())
dp = [0 for _ in range(301)] # 누적 점수를 담을 리스트
stairs = [0 for _ in range(301)] # 각 계단의 점수를 담을 리스트

# 계단의 점수 입력 받기
for i in range(n):
    stairs[i] = int(num())

dp[0] = stairs[0] # 첫번째 dp는 첫번째 계단의 점수가 될 것임
dp[1] = stairs[0] + stairs[1] # 두번째 dp는 첫번째 계단과 두번째 계단의 합이 될 것임
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
# 세번째 dp에는 첫번째와 세번째 계단을 밟은 경우와 두번째와 세번째 계단을 밟은 경우 둘 중에 합이 큰 것을 담기


# 네번째부터는 점화식
# 자신의 위치 점수 + 1칸 밑의 점수 + 3칸 밑까지 올라오는 점수
# 자신의 점수 + 2칸 밑의 점수
# 이 둘 중에서 최댓값을 골라야함
for i in range(3, n):
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

print(dp[n - 1])