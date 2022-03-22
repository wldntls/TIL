n = int(input())

drinks = list(map(int, input().split()))
drinks.sort(reverse=True)

drink = drinks[0]

for i in drinks[1:]:
    half = i / 2
    drink += half
print('%g'%drink) # %f(부동소수형 실수)와 %e (소문자 'e' 지수 표기) 의 단축형 표기/ 소수점의 여부에 따라 정수, 실수 자동 표시


