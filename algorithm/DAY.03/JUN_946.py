n = int(input())
dict_1 = {}

for i in range(n):
    capital = input().split()
    dict_1[capital[0]] = capital[1]
    # country, city = input().split()
    # dict_1 [country] = city

word = input()

print(dict_1.get(word, "Unknown Country"))

