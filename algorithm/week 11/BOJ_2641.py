# 1: 오른쪽 
# 2: 위쪽
# 3: 왼쪽
# 4: 아래쪽

# 1. 반대로 뒤집은 모양의 수열이 같다면 같은 모양을 가지게 됨
# 2. 특정 부분부터 기본 모양의 수열과 같게 이어진다면 같은 모양을 가지게 됨

import sys

# 입력받기
input = lambda: sys.stdin.readline().rstrip()

num_count = int(input()) # 표본 모양수열의 길이(숫자의 개수)
standard = list(map(int, input().split())) # 표본 모양수열
reverse_standard = [] # 반대 방향으로 뒤집은 기본 모양수열 

for i in standard:
    if i == 1:
        r = 3
    elif i == 2:
        r = 4
    elif i == 3:
        r = 1
    elif i == 4:
        r = 2
    reverse_standard.append(r)

reverse_standard.reverse()

shape_count = int(input()) # 모양수열의 개수
shapes_lst = [list(map(int, input().split())) for _ in range(shape_count)] # 모양들의 수열
answer = []

for shape in shapes_lst:
    for i in range(num_count):
        if shape[i:] + shape[:i] == standard:
            answer.append(shape)
        elif shape[i:] + shape[:i] == reverse_standard:
            answer.append(shape)

print(len(answer))
for i in answer:
    print(*i)
    

# pop이나 append를 쓰는 것이 디큐가 더 시간 복잡도 적음

# for i in range(num_count):
#     for j in range(1, 4):
#         if standard_shape == j:
#             nx = x + dx[j-1]
#             ny = y + dy[j-1]


