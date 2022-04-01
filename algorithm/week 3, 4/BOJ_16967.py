h, w, x, y = map(int, input().split())

# 배열 B를 이중 리스트 만들기
merge_matrix=[list(map(int, input().split())) for _ in range(h+x)]

# 배열 A의 행렬을 이중 리스트 형태로 추출해내야함?
a_matrix = [[0 for _ in range(w)] for _ in range(h)] # A 배열의 이중 리스트 0을 채워 만들어주기
check = [[0 for _ in range(w)] for _ in range(h)] # 확인을 위해 똑같이 만들기

for i in range(h):
    for j in range(w):
        # 배열 A와 배열 B가 겹치는 구간 찾기
        if i < h and j < w: 
            check[i][j] += 1 # 겹치지 않으면 1
        if i+x < h and j+y < w: # 겹치는 구간을 찾아낼 수 있음 그래서 겹치는 구간의 부분은 2를 가지게 되는 것임
            check[i+x][j+y] += 1

# 겹치는 구간을 원래 배열 A로 돌려주기
for i in range(h):
    for j in range(w):
        if check[i][j] == 1:
            a_matrix[i][j] = merge_matrix[i][j]
        elif check[i][j] == 2:
            a_matrix[i][j] = merge_matrix[i][j] - a_matrix[i-x][j-y] # 배열 B에서 배열 A의 값을 빼기

# 출력값과 같이 출력하기 위한 함수
for i in range(h):
    for j in range(w):
        print(a_matrix[i][j], end=' ')
    print()


# 피드백
# 합칠수도 있을 것 같음
