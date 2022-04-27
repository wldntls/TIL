# https://yabmoons.tistory.com/112

# 코드 참고
# https://dndi117.tistory.com/entry/%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-11722%EB%B2%88-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EA%B0%90%EC%86%8C%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%92%80%EC%9D%B4

# 점점 감소하는 수열의 길이를 구하는 것



n = int(input())
a = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if a[i] < a[j]:
            dp[i] = max(dp[i], dp[j] + 1)

            # 현재 인덱스 앞에서 서로가 작은지 큰지 어떻게 비교하지?

print(max(dp))