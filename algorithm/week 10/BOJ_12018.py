# 결론적으로 마일리지가 많은 과목을 들어야함 -> 일단 주어진 마일리지의 값을 모두 더해야함
# 학생들이 배팅할 마일리지의 최댓값은 100
# 가장 많은 과목수를 골라야 한다. 즉 내가 가진 포인트를 최대한 활용해서 많은 강의를 듣는것이 목적인 문제이다. 



n,m=map(int,input().split()) # 과목수 n, 주어진 마일리지 m
result=[]

for k in range(n):
  p,l=map(int,input().split()) # 과목을 신청한 사람 p, 과목의 수강 인원이 l
  mileage=list(map(int,input().split())) # 각 사람이 마일리지를 얼마나 넣었는지
  mileage.sort(reverse=True) # 내림차순으로 정렬

  if p<l: # 만약 과목을 신청한 사람이 수강 인원보다 적다면 
    result.append(1) # 마일리지를 1만 추가(예시에서는 2 4 밖에 없음)
  else:
    result.append(mileage[l-1]) # 수강신청 인원 마지막 사람의 마일리지를 저장
result.sort() # 결과를 오름차순으로 정렬
print(result)

cnt=0
for i in result: 
  m-=i # 최대 마일리지 수를 확인하기 위해서(마일리지 다쓰면 과목 못들음)
  cnt+=1 # 최대 과목수를 넣기 위해서
  if m<0: # 만약에 마일리지를 넘어선다면
    print(cnt-1) # 과목수를 하나빼서 출력
    break

if m>0: 
  print(cnt)