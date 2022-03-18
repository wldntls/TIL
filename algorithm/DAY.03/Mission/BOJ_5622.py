dial = {'ABC': 3,
        'DEF': 4,
        'GHI': 5,
        'JKL': 6,
        'MNO': 7,
        'PQRS': 8,
        'TUV': 9,
        'WXYZ': 10} # 숫자와 문자가 각각 1:1로 매핑되어 있기 때문에 딕셔너리로 각각의 값을 입력해줌

word = input() # 문자열을 입력받기

min_time = 0 # for문 안에서 숫자를 더하기 위한 변수

for key, value in dial.items(): # items를 활용하여 key값과 value값을 동시에 받아 for문 돌리기
    for i in word: # 입력받은 word를 for문을 돌려 알파벳 하나씩 돌리기
        if i in key: # 만약에 i가 key값에 있다면
            min_time += value # min_time에 value값을 더해줌
print(min_time) # 최종값을 출력


