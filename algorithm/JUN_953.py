foul = list(input().split())

record = {}

for i in foul:
    # {'Jay': 2, "John": 3, "John": 3... } 계속 다시 세는 코드, 시간복잡도 O(n^2)
    record[i] = foul.count(i)
    min_fouls = min(record.values())

for name, counts in record.items():
    if min_fouls == counts:
        print(name)

print(min_fouls)



####################################
# 1. 딕셔너리 만들기
# 2. 최소 파울 갯수 찾기
# 3. 가장 파울 적게한 선수 출력
# 4. 최소 파울 갯수 출력
#
#
####################################