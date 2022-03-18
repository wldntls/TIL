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
# - n-1만큼 for문 돌리기
# - file_names에 리스트로 문자열 입력 받기
# - file_name 길이 만큼 for문 돌리기
# - 만약 file_name과 file_names의 같은 위치의 문자가 다르다면 file_name의 해당 위치를 ?으로 변경하기
# - 그리고 이어서 출력할 수 있도록 for문 돌리고, end = '' 붙이기
############################

