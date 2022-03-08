words = list(input().split())
print(words)

for m in words[1]:
    for n in words[0]:
        if m == n:


            print(words[0])
    print(m)

# 2차원 리스트 
# 만약 m과 n이 처음으로 같다면 words[1] 출력
# 만약 m과 n이 다르면 처음으로 같은 문자의 열에 문자를 출력 나머지는 .을 출력 
# 문자열
