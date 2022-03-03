#n = int(input())

#print(sum(map(int, input())))

n = int(input())

numbers = list(map(int, input()))
print(sum(numbers))

#########################################
# 생각했던 과정
# - for문 돌려서 리스트에 담아서 더하려고 했었음
# 
# 올바른 풀이 과정 방향
# - 리스트에 담지 않아도 sum에 함수는 정수의 합을 구해줌
#########################################
