n, k = map(int, input().split())

count = 0

while True:
  if n % k == 0:
    count += 1
    n = n // k
    #print(n)

  elif n - 1:
    count += 1
    n -= 1

  if n == 1:
    break

print(count)
