import sys

input = lambda: sys.stdin.readline().rstrip()

n, r, c = map(int, input().split())

visit = 0
while n != 0: # 0이 아니면 계속 while문 돌아감
    # n -= 1
    size = 2 ** (n - 1) # 중앙이 되는 사이즈

    # 1사분면
    if r < size and c < size: 
        visit += size * size * 0 # 0이면 빠져나가서 0을 출력하게 됨

    # 2사분면 
    elif r < size and c >= size: # 가로가 중앙 사이즈보다 작고, 세로가 크거나 같아면
        visit += size * size * 1
        c -= size

    # 3사분면
    elif r >= size and c < size:
        r -= size

    # 4사분면
    else:
        visit += size * size * 3
        r -= size
        c -= size

print(visit)
