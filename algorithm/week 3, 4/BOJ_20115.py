n = int(input())

drinks = list(map(int, input().split())) # 에너지 드링크의 양을 공백으로 구분하여 정수로 입력받고, 리스트에 담기
drinks.sort(reverse=True) # 내림차순으로 정렬

drink = drinks[0] # for문 안에서 활용하기 위해 가장 많이 남은 음료의 양을 drink에 담기

for i in drinks[1:]: # 두번째로 양이 많은 음료부터 for문 돌리기
    half = i / 2 # 음료의 양을 반으로 나눔(원래 양의 절반은 바닥에 들리기 때문에) 그리고 half에 담기
    drink += half # 그리고 가장 많은 양의 음료에 담기
print('%g'%drink) # %f(부동소수형 실수)와 %e (소문자 'e' 지수 표기) 의 단축형 표기/ 소수점의 여부에 따라 정수, 실수 자동 표시


