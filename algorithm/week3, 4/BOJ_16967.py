# 미해결
h, w, x, y = map(int, input().split())

merge_matrix=[list(map(int, input().split())) for _ in range(h+x)]

print(merge_matrix)

a_matrix = []

for i in range(h):
    for j in range(w):
        a_matrix.append(merge_matrix[i][j])
print(a_matrix)



# 원래 배열인 A를 추출해내야함


