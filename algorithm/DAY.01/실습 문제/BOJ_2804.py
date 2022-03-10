a, b = input().split()

# 두 문자열이 크로스 되는 최초의 인덱스 찾기
for i, char in enumerate(a):
    b_index = b.find(char)
    if b_index != -1:
        print(b_index)
        a_index = i
        print(a_index)
        break

# 예시처럼 출력하기
for i, char in enumerate(b):
    if i == b_index:
        print(a)
    else:
				# .을 먼저 찍고 + b 문자 한개 + 다시 남은 만큼 . 찍기
        print("." * a_index + char + "." * (len(a) - a_index - 1))

############################
# 코드 리뷰
# - 첫번째 
# - 변경된 문자를 리스트에 담기
# - for문을 통해 리스트를 돌리고, 입력 받은 croatia_alphabet에 해당 문자가 있다면 '.'으로 변경하기
# - 변경된 문자열의 길이를 재서 print
############################


# 2차원 리스트 
# 만약 m과 n이 처음으로 같다면 words[1] 출력 
# 만약 m과 n이 다르면 처음으로 같은 문자의 열에 문자를 출력 나머지는 .을 출력 
# 문자열
# 
