# 2 * 0 = 1
# 2 * 1 = 3 
# 2 * 2 = 7 (1 + 3 + 3)
# 2 * 3 = 17 (3 + 7 + 7)
# 2 * 4 = 41 (7 + 17 + 17)

import sys 

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dp = [0] *100001
dp[0] = 1
dp[1] = 3

for i in range(2, 100001):
    dp[i] = (dp[i-2] + dp[i-1] + dp[i-1]) % 9901

print(dp[n])