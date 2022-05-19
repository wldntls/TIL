
# n = int(input())
# a, b = map(int, input().split())
# m = int(input())

# for i in range(n + ):
#     for j in range(m)

# graph = [list(map(int, input().split())) for _ in range(m) for _ in range(n+1)]


# print(graph)

# visited = [False] * (n + 1)
# result = []

# def dfs(a_num, depth):
#     depth += 1
#     visited[a_num] = True
    
#     if a_num == b:
#         result.append(a_num)

#     for i in graph[a_num]:
#         if not visited[i]:
#             dfs(i, depth)

# dfs(a, 0)


# https://wonyoung2257.tistory.com/56
# https://lbdiaryl.tistory.com/m/212

# 왜 틀렸습니다...?

# 입력값 받는 부분
n = int(input()) # 전체 사람의 수를 입력받기 
a, b = map(int, input().split()) # 촌수를 계산해야하는 두사람
m = int(input()) # 부모 자식간의 관계의 개수
graph = [[] for _ in range(n+1)] # 연결된 노드들을 받을 인덱스 생성
visited = [False] * (n+1) # 방문을 표시할 리스트 
result = [] # 결과를 담을 리스트

# 어떤 노드들이 연결되어 있는지 graph라는 2차원 배열에 저장
for _ in range(m):
    x, y = map(int, input().split())  
    graph[x].append(y)
    graph[y].append(x)

# print(graph)
# 결과 : [[], [2, 3](3), [1, 7, 8, 9](2), [1], [5, 6], [4], [4], [2](1), [2], [2]]
# 인덱스 위치에 연결되어 있는 숫자의 리스트가 들어가 있음 

def dfs(a_num, depth): # a와 깊이를 계산할 depth를 인자로 받기
    depth += 1 # 깊이 +1 해주기
    visited[a_num] = True # 방문처리
    
    if a_num == b: # b는 전역변수라서 함수안으로 불러오는 것이 가능?
        result.append(depth)

    for i in graph[a_num]:
        if not visited[i]:
            dfs(i, depth)

dfs(a, 0)

if len(result) == 0:
  print(-1)
else:
  print(result[0]-1) # 왜 마이너스 1 해주지...?

