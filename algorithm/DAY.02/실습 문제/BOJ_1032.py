N = int(input())

file_list = [input() for i in range(N)]

for i in file_list:
    if file_list[i] != file_list[i+1]:
        print(file_list)

