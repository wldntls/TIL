# 오늘의집 코테 문제 1번
path = input()

ewsn = ['E', 'W', 'S', 'N']

answer = []

# x 

# y
for i in path:
    move = path.count(i)
    print(move*100)

# direction
for i in ewsn:
    for j in ewsn:
        if i == 'E':

        if ewsn[i][j] == ewsn['E']['N'] or ewsn['S']['E'] or ewsn['W']['S'] or ewsn['N']['W'] :
            direction = 'left'
        if ewsn[i][j] == ewsn['E']['S'] or ewsn['S']['W'] or ewsn['W']['N'] or ewsn['N']['E'] :
            direction = 'right'


n, m = map(int, input().split())

visited = [False] * (n + 1)
arr = [] 

def back_tracking(depth, n, m):
    if depth == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, len(visited) + 1):
        if not visited[i]:
            visited[i] = True 
            arr.append(i) 
            back_tracking(depth + 1, n, m) 
            visited[i] = False
            arr.pop()

back_tracking(0, n, m)
