n = int(input())

members = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    members.append((age, name))
    #member_sorted = sorted(members)

members.sort(key=lambda x : x[0])

for member in members:
    print(member[0], member[1])

#if age_sorted[]

    #print(sorted(members[i][0]))

# 나이가 같으면 입력된 순으로 출력하기



