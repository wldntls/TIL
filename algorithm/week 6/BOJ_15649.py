n, m = map(int, input().split())

visited = [False] * (n + 1) # 탐색 여부를 확인하기 위한 리스트
# +1을 해주는 이유 -> 헷갈리지 않게 하기 위해 1부터 시작하는 것으로 맞춰주기 위해 
arr = [] # 결과를 담아서 출력해주기 위한 리스트 선언

def solve(depth, n, m):
    if depth == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n + 1):
        if not visited[i]:
            # 탐색을 안했다면 if not ___ => False 일 경우, if ___ => True 일 경우
            # 따라서 visted[i] 가 False이라면 조건문을 수행한다.
            #print(visited)
            visited[i] = True # 현재 숫자를 True로 바꿔줍니다.
            arr.append(i) # 현재 숫자를 arr에 추가하기
            #print(arr, '탐색 시작')
            #print(visited)
        
            solve(depth + 1, n, m) # depth가 m과 같아지면 여기서 빠져나와서 밑에 명령문 수행

            visited[i] = False
            arr.pop()
            #print(arr, '탐사 내용 제거')

solve(0, n, m)

# https://blog.encrypted.gg/945

""" def dfs():
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    for i in range(1, N+1):
        if i in s: # 가지치기, 이미 선택한 숫자 배제
            continue
        s.append(i)
        dfs() #함수호출
        s.pop() # 출력 후 return하고 마지막 원소 비우기

N, M = map(int, input().split())
s = []
dfs() """

###############################
# 내가 이해한 것
# 깊이가 m과 같아지면 출력
# 재귀적으로 돌면서 함수가 출력을 했는지 확인을 해야한다.
# 1에서 재귀적으로 반복, 2에서 재귀적으로 반복
# 대충 이해하긴 했지만, 전날 한번 더 보고 설명하기