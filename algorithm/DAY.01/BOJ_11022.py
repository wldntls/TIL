t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print('Case #{0}:'.format(i+1), a, '+', b, '=', a+b)

    #print(f'Case #{i+1}: {a} + {b} = {a+b}')