n = int(input())
file_name = list(input())

for i in range(n-1):
    file_names = list(input())
    for j in range(len(file_name)):
        if file_name[j] != file_names[j]:
            file_name[j] = '?'

for i in file_name:
    print(i, end="")


############################
# 코드 리뷰
# - n에 정수로 입력받기 
# - file_name에 리스트로 한글자씩 입력 받기 
############################

