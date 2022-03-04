n = int(input())

for i in range(n):
    typo_n, word = map(str, input().split())
    print(word[:int(typo_n)-1]+word[int(typo_n):])