# 그리디 : 현재 상황에서 당장 좋은 것만 고르는 방법
# 해당 문제에서 가장 좋은 방법은?
# -> 오름차순으로 정렬하는 것이 필요
# 피보나치 수열와 같은 방식

n = int(input())
p = sorted(list(map(int, input().split())))

# 결과
# p = [1, 2, 3, 3, 4]

min_time = 0
sum = 0

for i in p:
    sum += i # sum에는 그사람이 돈을 인출하는데 걸리는 시간
    min_time += sum # min_time은 모든 사람이 돈을 인출하는데 필요한 최소시간
    
print(min_time)





