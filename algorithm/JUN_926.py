first_array = [list(map(int, input().split())) for i in range(2)]
second_array = [list(map(int, input().split())) for i in range(2)]

print(first_array)
print(second_array)


for i in range(2):
    for j in range(4):
        array_1 = first_array[i][j] * second_array[i][j]
        print(array_1, end = " ")
    print()
