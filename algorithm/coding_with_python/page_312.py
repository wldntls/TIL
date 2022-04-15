# 곱하기 혹은 더하기
# Facebook 인터뷰

n = input()

lst = [int(i) for i in n]

result = lst[0]

for i in lst[1:]:
    print(i)
    if i <= 1 or result <= 1: # 둘 중에 하나가 '0' 이거나 '1'일 인 경우, 더하기 수행
        result += i
    else: # 그게 아니라면 곱하기 수행
        result *= i

print(result)






# 리스트에 숫자 하나씩 담아서
# 더하기 하고 곱하기 해서 큰 값 담기
# 그 값을 갱신
# 또 더하기 하고 곱하기 해서 큰 값 담기