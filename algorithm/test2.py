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



