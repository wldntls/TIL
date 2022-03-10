square = [[0] * 100 for i in range(100)]

for _ in range(4):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            square[i][j] = 1

print(sum(sum(line) for line in square))

############################
# 코드 리뷰
# - square에 가로, 세로의 크기가 각각 100인 정사각형 모양의 넓이를 리스트에 0을 담아 할당하기
# - for문을 네 개의 직사각형 위치 왼쪽, 오른쪽 아래 꼭짓점 좌표를 정수로 입력 받기
# - 이중 for문을 통해 입력 받은 x1, x2와 y1, y2 만큼 반복함
# - 그리고 해당되는 인덱스에 1을 삽입하기
# - 그리고 1이 입력된 square를 for문을 돌려 각 행의 갯수를 더하고, 행의 합을 더하여 출력
############################



