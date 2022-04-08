# 그리디 : 현재 상황에서 가장 좋아보이는 것만을 선택하는 알고리즘
n, k = map(int, input().split())

count = 0

coin_list = []

for i in range(n):
    a = int(input())
    coin_list.append(a)

for coin in coin_list[::-1]:
    count += k//coin # 나눗셈의 몫을 count에 담기
    k %= coin # 나눗셈을 해준 나머지(남은 돈)를 k에 담습니다.

print(count)

