# 입력받은 모든 수를 절댓값으로 변경 ads()
# 리스트에 담기 (num)
# 산술평균 : sum(num)/n
# 중앙값 : sort(num) 
#       med = len(num) // 2
#       len(num) % 2 == 1:
#        print(num[med])
# 최빈값 : max_num = value_count(num) 
#        max(max_num)
# 범위 : sort(num)
#      num[-1] - num[0] 

import sys
from collections import Counter

n = int(sys.stdin.readline())

num_lst = []

for i in range(n):
    num = int(input())
    num_lst.append(num)

# 산술평균
print(round(sum(num_lst) / n)) # 반올림하는 방법

# 중앙값
num_lst.sort()
print(num_lst[len(num_lst) // 2])

# 최빈값
max_num = Counter(num_lst).most_common()
if len(max_num) > 1 and max_num[0][1] == max_num[1][1]: # 최빈값이 2개 이상일 때
    print(max_num[1][0])
else:
    print(max_num[0][0])

# 범위
print(max(num_lst) - min(num_lst))






