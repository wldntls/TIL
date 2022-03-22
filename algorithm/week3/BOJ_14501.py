# DP 문제
n = int(input())

t_list = []
p_list = []
dp = []

for i in range(n):
    t, p = map(int, input().split())

    t_list.append(t)
    p_list.append(p)
    dp.append(p)
dp.append(0)
#print(t_list)
#print(p_list)
#print(dp)

for i in range(n-1, -1, -1):
    #print(i)
    if t_list[i] + i > n:
        #print(t_list[i],'o')
        #print(dp[i])
        dp[i] = dp[i+1] # 뒤에 리스트 값들을 0으로 변환
        #print(dp)

    else:
        #print(dp[i])
        #print(dp[i+1])
        #print(p_list[i])
        #print(t_list[i])
        #print(dp[i+t_list[i]],'wad')
        #print(p_list[i]+dp[i+t_list[i]],'ws')
        dp[i] = max(dp[i+1], p_list[i]+dp[i+t_list[i]])

print(dp[0])




'''

print(schedule)

pay = schedule[0][1] # 금액
day_1 = schedule[0][0] # 상담 기간

for i in range(len(schedule)):
    if day_1 == i: # 상담 기간과 인덱스가 겹치면 상담이 끝난 다음날이기 때문에
        pay += schedule[i][1]
        print(pay)



        print(schedule[i][0])
        if schedule[i][0] == day_1+i:
            print(i)
            pay += schedule[i][1]
            print(pay)
'''