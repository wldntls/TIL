import sys
n = int(input())

stack = []

for _ in range(n):
    command = sys.stdin.readline().split() # 시간 복잡도 줄이기 위해서 

    if command[0] == 'push':
        stack.append(command[1])

    if command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        elif len(stack) > 0:
            print(stack.pop())

    if command[0] == 'size':
        print(len(stack))

    if command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        elif len(stack) > 0:
            print(0)
            
    if command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        elif len(stack) > 0:
            print(stack[-1])


# 문자열 받을때 - sys.stdin.readline()
# 정수 한개 입력 받을 때 - int(sys.stdin.readline())
# 여러개 정수 입력 받을 때 - map(int(sys.stdin.readline().split()))
# 문자열 n줄 입력받아 리스트에 저장할 때 - [sys.stdin.readline().split() for i in range(n)]
