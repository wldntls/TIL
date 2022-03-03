'''
list = []

for i in range(1, 9):
    num = input()
    list.append(int(num))

max_num = max(list)

print(max_num)
print(i)
'''
list = [int(input()) for i in range(0, 9)]

print(max(list))

print(list.index(max(list))+1)