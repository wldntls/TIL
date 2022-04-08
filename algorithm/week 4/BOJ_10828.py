import sys # 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈이다.
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
            print(stack.pop()) # 가장 위에 있는 수를 빼고, 그 수를 출력

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
            print(stack[-1]) # 그냥 가장 위에 있는 수를 출력해주는 것(빼는 것 아님)


# 문자열 받을때 - sys.stdin.readline()
# 정수 한개 입력 받을 때 - int(sys.stdin.readline())
# 여러개 정수 입력 받을 때 - map(int(sys.stdin.readline().split()))
# 문자열 n줄 입력받아 리스트에 저장할 때 - [sys.stdin.readline().split() for i in range(n)]
