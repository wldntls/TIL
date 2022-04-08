# 코드 1
n = int(input()) # 3의 거듭제곱 

def get_stars(n): # 여기서 n은 아래 star 리스트
    temp = [] 
    for i in range(len(n) * 3): # 리스트의 길이 * 3만큼 반복
        print(i)
        print(i % len(n), 'fgkfk')
        if i // len(n) == 1: # 리스트의 길이로 나눈 몫이 1일 경우(즉, '* *'일 경우)
            temp.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            temp.append(n[i % len(n)] * 3)
        print(temp)
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
    #print(star)

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
############################################

# 코드 2

# 별 찍는 재귀 함수
def draw_star(n) :
    global Map
    
    if n == 3 :
        Map[0][:3] = Map[2][:3] = [1]*3
        Map[1][:3] = [1, 0, 1]
        return

    a = n//3
    draw_star(n//3)
    for i in range(3) :
        for j in range(3) :
            if i == 1 and j == 1 :
                continue
            for k in range(a) :
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a] # 핵심 아이디어

N = int(input())      

# 메인 데이터 선언
Map = [[0 for i in range(N)] for i in range(N)]

draw_star(N)

for i in Map :
    for j in i :
        if j :
            print('*', end = '')
        else :
            print(' ', end = '')
    print()

# https://study-all-night.tistory.com/5 

