# https://richard25.tistory.com/39\

import sys

from regex import W

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
w = int(input())
num = list(input().split())
print(num)

photo = dict()
for i in range(w) :
    if num[i] in photo :
        photo[num[i]][0] += 1
    else : 
        if len(photo) < n :
            photo[num[i]] = [1, i]
        else :
            del_list = sorted(photo.items(), key= lambda x : (x[1][0] , x[1][1]))
            del_key = del_list[0][0]
            del(photo[del_key])
            photo[num[i]] = [1, i]

ans_list = list(sorted(photo.keys()))
answer = str(ans_list[0])
for i in ans_list[1: ] :
    answer += " " + str(i)
print(answer)