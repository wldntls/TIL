first_array = [list(map(int, input().split())) for i in range(2)]
second_array = [list(map(int, input().split())) for i in range(2)]

print(first_array)
print(second_array)


for i in range(2):
    for j in range(4):
        array_1 = first_array[i][j] * second_array[i][j]
        print(array_1, end = " ")
    print()

#########################################
# 생각했던 과정
# - 2행 4열을 리스트에 리스트로 담기
# - 이중 for문을 이용해서 두개의 행렬의 인덱스를 곱해야함
# - 마지막 출력하는 과정에서 막힘
#
# 올바른 풀이 과정 방향
# - 두 번째 for문 안에서는 4번만 돌기 때문에 5번째부터 아래 행으로 출력하기 위해서는 첫 번째 for문에 속하게 print()를 내려주면 됨
##########################################