# 다이니믹 프로그래밍 : 큰 문제를 부분 문제로 나누고, 이미 연산을 끝낸 값들에 대해선 그 값들을 재활용하는 것이다.
# n이 1일 때부터 1씩 추가하여 각 n을 1로 만드는 최소 연산의 횟수를 구한다.
# n이 1일 때는 이미 1이므로 연산이 필요하지 않다. d[1] = 0 -> for문 2로 시작


n = int(input())

dp = [0] * (n+1)
print(dp)

for i in range(2, n+1):
    print(i)
    # 현재의 수에서 1을 빼는 경우
    dp[i] = dp[i - 1] + 1
    if n % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if n % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    print(dp)

print(dp[n])

########################
# 내가 풀이 이해한 것
# 1. 작은 수부터 차례로 계산
# 2. 작은 수에서 계산된 횟수는 dp에 저장 
# 3. 횟수 중에서 최소한의 횟수를 뽑아서 dp에 저장하는 것
# 4. 그러므로 dp[n]에는 연산 횟수의 최솟값이 저장
