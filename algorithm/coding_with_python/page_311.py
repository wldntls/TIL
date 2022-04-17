n = int(input())
horrors = list(map(int, input().split()))
horrors.sort()

adventure = 0 
result = 0

for i in horrors:
    adventure += 1
    if adventure >= i:
        result += 1
        adventure = 0
print(result)