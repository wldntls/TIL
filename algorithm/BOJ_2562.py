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

# max_num = max(list)

print(max(list))

print(list.index(max(list))+1)

#########################################
# 생각했던 과정
# - 9번째까지 리스트에 담고, 그 중에서 max 찾기
#
# 올바른 풀이 과정 방향
# - range에서 0은 없어도 됨
# - index 메서드 사용 위치 반환하기
##########################################