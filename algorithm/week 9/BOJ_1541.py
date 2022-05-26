# 모든 경우의 수를 다 계산해봐야함
# '-' 뒤에 괄호를 치고 계산을 하면 최소값을 뽑을 수 있음

exp = input().split('-')

num = []  

for i in exp:
    if '+' in i:
        num_sum = 0
        s = i.split('+')
        for j in s:
            num_sum += int(j)
        num.append(num_sum)
    else:
        num.append(i)

num = list(map(int, num))

for z in range(1, len(num)):
    num[0] -= int(num[z])

print(num[0])