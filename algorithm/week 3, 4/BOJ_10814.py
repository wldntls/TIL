n = int(input()) # n으로 회원의 수를 정수로 입력받기

members = [] # for문 안에서 활용하기 위해 리스트 할당

for i in range(n): # 회원의 수 만큼 for문을 돌리기
    age, name = map(str, input().split()) # 나이와 이름을 정수로 입력받기
    age = int(age) # 나이를 정수로 변환
    members.append((age, name)) # 리스트에 담기

members.sort(key=lambda x : x[0]) # 나이순으로 정렬, 리스트 sorted로 정렬하면 1번째 인자가 알파벳 순으로 정렬됨?!?
# print(members)

for member in members:
    print(member[0], member[1])




