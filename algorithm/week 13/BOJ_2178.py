# 1: 이동 가능
# 0: 이동 불가능

import sys 

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        

