import sys

input = lambda: sys.stdin.readline().rstrip()

n, r, c = map(int, input().split())

cnt = -1

lst = []
total_order = []
for i in range(2**n):
    for j in range(2**n):
        
        cnt += 1
        lst.append(cnt)
        if len(lst) == 4:
            total_order.append(lst)

        
print(total_order)