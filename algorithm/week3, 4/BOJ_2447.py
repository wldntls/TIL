n = int(input()) # 3의 거듭제곱 

def get_stars(n):
    temp = []
    for i in range(len(n) * 3):
        #print(i)
        #print(i % len(n), 'fgkfk')
        if i // len(n) == 1:
            temp.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            temp.append(n[i % len(n)] * 3)
        #print(temp)
    return temp

star = ["***", "* *", "***"]
count = 0

while n != 3:
    #print(n) # 27
    n //= 3
    count += 1
    #print(count) # 27 -> 1, 9 -> 2

for _ in range(count):
    star = get_stars(star)
    print(star)

for j in star:
   print(j)

'''
연산자 %는 나머지를 구해준다.
첫번째 나머지에서 구해지지 않으면 그 값을 그대로 나머지로 출력한다.
print(1/3)
print(1%3) # 결과 1
print(1//3)

print(2/3)
print(2%3) # 결과 2
print(2//3)

print(3/15)
print(3%15) # 결과 3
'''

# https://ji-gwang.tistory.com/225

