first_array = [list(map(int, input().split())) for i in range(2)]
second_array = [list(map(int, input().split())) for i in range(2)]

# 1 
third_array = [[0]*3 for i in range(2)]

for i in range(2):
    for j in range(3):
        third_array[i][j] = first_array[i][j] * second_array[i][j]
print(third_array)

# 2
# third_array = []

for i in range(2):
    temp = []
    for j in range(3):
        temp.append(first_array[i][j] * second_array[i][j])
    third_array.append(temp)

# 2번 List Comprhansion 사용하여 더 간단하게 
third_array = [[first_array[i][j] * second_array[i][j] for j in range(3)] for i in range(2)]

# 1, 2- 출력
for i in range(2):
    for j in range(3):
        print(third_array, end = " ")
    print()

#########################################
# 생각 과정
# - new_array를 list에 어떻게 담지?
# 
# 
#
# 올바른 풀이 과정 방향
# - 초기화하고 다시 넣기
##########################################


#####################################
# 강사님 코드

list_a = [list(map(int, input().split())) for i in range(2)]
list_b = [list(map(int, input().split())) for i in range(2)]

# 1번
# list_c = [[0] * 3 for i in range(2)]
# for i in range(2):
#     for j in range(3):
#         list_c[i][j] = list_a[i][j] * list_b[i][j]

# 2번
# list_c = []
# for i in range(2):
#     temp = []
#     for j in range(3):
#         temp.append(list_a[i][j] * list_b[i][j])
#     list_c.append(temp)

# 2번을 더 간단하게 (list comprehension 이용)
list_c = [[list_a[i][j] * list_b[i][j] for j in range(3)] for i in range(2)]

# 출력
for i in range(2):
    for j in range(3):
        print(list_c[i][j], end=" ")
    print()