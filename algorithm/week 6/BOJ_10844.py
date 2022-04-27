# 계단의 수는 0~9까지 일 수밖에 없음. 왜냐하면, 10이 되면 1, 0 이렇게 되기 때문에
# n = 1 일때, 길이가 1인 계단 수가 총 몇개 있는지 

#         0  1  2  3  4  5  6  7  8  9
# 자리수(1) 0  1  1  1  1  1  1  1  1  1
# 자리수(2) 1  1  2  2  2  2  2  2  2  1
# 자리수(3) 1  3  3  4  4  4  4  4  3  2

# 규칙
# 해당 위치의 대각선 위 위치의 숫자들이 합

n = int(input())

stairs = [[0]*10 for _ in range(n + 1)] # 이차원 리스트 생성

# 초기값 설정
stairs[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1] # 자리수가 1일 때, 올 수 있는 숫자들의 갯수? 

for i in range(2, n + 1):

    # 계단 수가 0으로 끝나는 경우 -> 앞에 있는 자리수가 1일 때만 고려해야함
    stairs[i][0] = stairs[i - 1][1]
    #print(stairs[i][0], 'a')
    #print(stairs[i - 1][1],'b')

    # 계단 수가 9로 끝나는 경우 -> 앞에 있는 자리수가 8일 떄만 고려해야함
    stairs[i][9] = stairs[i - 1][8]
    #print(stairs[i][9], 'c')
    #print(stairs[i - 1][8], 'd')

    # 계단 수가 1~8로 끝나는 경우 -> 앞뒤로 올 수 있는 자리수의 갯수를? 더해줘야하기 때문에 
    for j in range(1, 9):
        stairs[i][j] = stairs[i - 1][j - 1] + stairs[i - 1][j + 1]
        # print(stairs[i - 1][j - 1], 'e')
        # print(stairs[i - 1][j + 1], 'f')
        # print(stairs[i][j], 'g')

print(sum(stairs[n]) % 1000000000)

# 아직 해결되지 않은 점 
# tairs[i - 1][8] 등에서 왜 모두 i-1이지?
# 출력은 왜 저렇게 뽑지? 문제에서 저렇게 뽑으라함
# https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-10844-%EC%89%AC%EC%9A%B4-%EA%B3%84%EB%8B%A8-%EC%88%98