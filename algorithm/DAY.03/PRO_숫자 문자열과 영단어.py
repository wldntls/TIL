s = input()

numbers = {"0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine"}


for key, value in numbers.items():
    s = s.replace(value, key)
print(s)

################################################

def solution(s):
    numbers = {"0": "zero", 
    "1": "one", 
    "2": "two", 
    "3": "three", 
    "4": "four",
    "5": "five", 
    "6": "six", 
    "7": "seven", 
    "8": "eight", 
    "9": "nine"}
    
    for key, value in numbers.items():
        s = s.replace(value, key)
        answer = s
    return int(answer)

######################################
# 생각 과정
# - 주어진 자료 딕셔너리로 매핑 (하드코딩으로)
# - items()으로 key, value 각각 받아서 replace로 변경하기 
# - 마지막에 출력에서 막힘
# - 다른 변수(answer)에 s를 다시 넣었더니 반복문 계속 다시 출력
# - s를 그대로 s에 출력했더니 원하는 출력값 나옴
######################################