n = int(input())

element_locations = []

for i in range(n):
    x, y = map(int, input().split())
    element_locations.append((x, y))

element_locations.sort(key=lambda x: (x[0], x[1]))

for element_location in element_locations:
    print(element_location[0], element_location[1])



"""
n = int(input())

cdn = [ list(map(int,input().split())) for i in range(n)]

cdn.sort()

for i in cdn:
    print(i[0],i[1])

"""