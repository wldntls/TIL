h, w, x, y = map(int, input().split())

merge_matrix=[list(map(int, input().split())) for _ in range(h+x)]

# 배열 A의 행렬을 이중 리스트 형태로 추출해내야함?
a_matrix = [[0 for _ in range(w)] for _ in range(h)]
check = [[0 for _ in range(w)] for _ in range(h)]

print(a_matrix)

for i in range(h):
    for j in range(w):
        # 배열 A와 배열 B가 겹치는 구간 찾기
        if i < h and j < w:
            check[i][j] += 1
        if i+x < h and j+y < w:
            check[i+x][j+y] += 1

# 겹치는 구간을 원래 배열 A로 돌려주기
for i in range(h):
    for j in range(w):
        if check[i][j] == 1:
            a_matrix[i][j] = merge_matrix[i][j]
        elif check[i][j] == 2:
            a_matrix[i][j] = merge_matrix[i][j] - a_matrix[i-x][j-y]

for i in range(h):
    for j in range(w):
        print(a_matrix[i][j], end=' ')
    print()

            



# 원래 배열인 A를 추출해내야함


