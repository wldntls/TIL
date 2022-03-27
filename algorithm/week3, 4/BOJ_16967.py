# 미해결
h, w, x, y = map(int, input().split())

merge_matrix=[list(map(int, input().split())) for _ in range(h+x)]

# 배열 B
print(merge_matrix)

a_matrix = []

# 배열 A의 행렬을 이중 리스트 형태로 추출해내야함?
a_matrix = [[0 for _ in range(w)] for _ in range(h)]
print(a_matrix)

for i in range(h):
    for j in range(w):
        # 배열 A와 배열 B가 겹치는 구간 찾기
        if i < h and j < w:
            a_matrix[i][j] += 1
        if i+x < h and j+y < w:
            a_matrix[i+x][j+y] += 1
print(a_matrix)

# 겹치는 구간을 원래 배열 A로 돌려주기


            



# 원래 배열인 A를 추출해내야함


