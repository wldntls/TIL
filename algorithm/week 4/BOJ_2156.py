n = int(input())
w = [0]
for i in range(n):
    w.append(int(input()))
#print(w)

# DP : 한 번 계산한 문제는 다시 계산하지 않도록 하는 알고리즘
dp = [0]
dp.append(w[1]) # 첫번째 포도주 와인잔의 양을 dp 변수에 담기
#print(dp)

if n > 1:
    dp.append(w[1] + w[2]) # 첫번재 포도주의 양과 두번째 포도주의 양을 더한 누적 값이 담기게 됩니다.
    #print(dp,'ㅇㄹ')

# 세번째부터는 규칙성이 발견되어 규칙성 코드를 작성 
for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i])) # 4번째 부터의 dp의 규칙성
    #print(dp)
print(dp[n])
