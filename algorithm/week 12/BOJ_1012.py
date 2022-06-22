import sys

input = lambda: sys.stdin.readline().rstrip()

t = input()
m, n, k = map(int, input().split())

location = [input().split() for i in range(k)]

