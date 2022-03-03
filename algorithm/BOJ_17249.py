punch = input()

punch_list = punch.split('(^0^)')
left = punch_list[0].count("@=")
right = punch_list[1].count("=@")

print(left, right)