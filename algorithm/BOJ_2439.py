t = int(input())

#for i in range(t):
#    a = '*' * (i+1)
#    print(a.rjust(t))

for i in range(1, t+1):
    print(" "*(t-i) + "*"*i)