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
# - paper에 가로, 세로의 크기가 각각 100인 정사각형 모양의 넓이를 리스트에 0을 담아 할당하기
# - for문을 돌려서 도화지의 갯수를 받기
# - for문 안에서 x, y를 입력 받기
# - 이중 for문을 활용하여 입력 받은 x와 y를 +10해서 돌려줌(색종이의 크기가 10이기 때문에)
# - 그리고 해당되는 인덱스에 1을 삽입하기
# - 그리고 1이 입력된 paper를 for문을 돌려 각 행의 갯수를 더하고, 행의 합을 더하여 출력
############################

