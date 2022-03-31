# DP 문제
n = int(input()) # 일하는 기간 정수 입력받기

day_list = []
pay_list = []
dp = []

for i in range(n): # n만큼 for문 돌리기
    day, pay = map(int, input().split()) # 기간과 금액 공백을 기준으로 입력받기
    day_list.append(day) # day_list에 기간 넣기
    pay_list.append(pay) # pay_list에 금액 넣기
    dp.append(pay) # dp 리스트에 금액 넣기
    print(dp)
dp.append(0) # dp[i] = dp[i+1] 밑에 이부분에서 list of range 오류를 방지하기 위해 0을 추가, 뒤에서부터 값을 돌리기 위함도 있음
#print(t_list)
#print(p_list)
print(dp) # 출력 결과 [10, 20, 10, 20, 15, 40, 200, 0]

for i in range(n-1, -1, -1): # 뒤에서 부터 for문 돌리기
    #print(i)
    if day_list[i] + i > n: # n+1일에는 일을 할 수 없음, 만약 n(일하는 기간)보다 상담하는 기간이 크다면 
        #print(t_list[i],'o')
        #print(dp[i])
        dp[i] = dp[i+1] # 그 날짜의 금액을 0으로 변환
        #print(dp)

    else: # 일하는 기간에 상담하는 기간이 들어오게 된다면 
        #print(dp[i])
        print(dp[i+1]) # 만약 n보다 큰 경우 다음이라면 0이 담겨 있을 것임, 아니라면 그 날짜의 금액이 담겨 있을 것임
        #print(p_list[i])
        print(day_list[i],'ㅓㅈ에') # day_list의 인덱스를 반환
        print(dp[i+day_list[i]],'wad') # 인덱스 값과 dp의 i 인덱스 값을 더하고 그 인덱스에 담겨져 있는 값 출력 
        print(pay_list[i]+dp[i+day_list[i]],'ws')
        # dp[i+1] : 일을 맡지 않을 경우 보상
        # pay_list[i]+dp[i+day_list[i]] : 현재 일을 맡았을 때 들어오는 보상 + 현재 일을 끝낸 다음날에 쌓여있는 보상
        dp[i] = max(dp[i+1], pay_list[i]+dp[i+day_list[i]]) 

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