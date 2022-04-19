# 계단의 수는 0~9까지 일 수밖에 없음. 왜냐하면, 10이 되면 1, 0 이렇게 되기 때문에
# n = 1 일때, 길이가 1인 계단 수가 총 몇개 있는지 

n = int(input())

stairs = [[0]*10 for _ in range(n + 1)]

# 초기값 설정
stairs[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n + 1):
    # 계단 수가 0으로 끝나는 경우
    stairs[i][0] = stairs[i - 1][1]
    print(stairs[i][0])
    # 계단 수가 9로 끝나는 경우
    stairs[i][9] = stairs[i - 1][8]

    # 계단 수가 1~8로 끝나는 경우 
    for j in range(1, 9):
        stairs[i][j] = stairs[i - 1][j - 1] + stairs[i - 1][j + 1]
        print(stairs[i][j])

print(sum(stairs[n]) % 100000000)