N = int(input())

file_list = [input() for i in range(N)]

for file in file_list:
    for i in file:
        if file_list[i] != file_list[i+1]:
            print(file_list)

