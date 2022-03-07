croatia_alphabet = input()

croatia =['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


for i in croatia:
    if i in croatia_alphabet:
        croatia_alphabet = croatia_alphabet.replace(i, '.')
print(len(croatia_alphabet))


# 크로아티아 알파벳 갯수 세기 (한개로 처리하여)
# 그냥 알파벳 세기

############################
# 코드 리뷰
# - 문자열 입력 받기
# - 변경된 문자를 리스트에 담기
# - for문을 통해 리스트를 돌리고, 입력 받은 croatia_alphabet에 해당 문자가 있다면 '.'으로 변경하기
# - 변경된 문자열의 길이를 재서 print
############################
