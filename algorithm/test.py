print('hello')

# input 기본
a = input()
b = int(input())
c = float(input())

print(a, b, c)
print(type(a), type(b), type(c))

# map 이용하기
a, b = map(int, input().split())
c, d = input().split()
e, f = map(int, input())

print(a, b)
print(c, d)
print(e, f)

# print
print(a, b, c, d, e)
print(a, b, c, d, e, sep="&")
print(a, b, c, d, e, end="!")