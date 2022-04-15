n = int(input())

p = [0] + list(map(int, input().split()))
#print(p)

dp = [0] * (n + 1)

dp[1] = p[1]

for i in range(2, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + dp[j])
print(dp[i])
