foul = list(input().split())

record = {}

for i in foul:
    # {'Jay': 2, "John": 3, "John": 3... } 계속 다시 세는 코드, 시간복잡도 O(n^2)
    record[i] = foul.count(i) # 결국, 이 코드는 시간복잡도가 높은 코드
    min_fouls = min(record.values())

for name, counts in record.items():
    if min_fouls == counts:
        print(name)

print(min_fouls)

####################강사님코드##################
# 1. 딕셔너리 만들기
palyers = input().split()
fouls = {}

for palyer in palyers:
    # 1) 이미 선수 있너요?
    if palyer in fouls:
        fouls[palyer] += 1
    # 2) 선수가 없어요?
    else:
        fouls[palyer] = 1

# 2. 최소 파울 갯수 찾기
min_foul = min(fouls.values())

# 3. 가장 파울 적게한 선수 출력
for palyer, foul in fouls.items():
    if foul == min_foul:
        print(palyer)

# 4. 최소 파울 갯수 출력
print(min_foul)
