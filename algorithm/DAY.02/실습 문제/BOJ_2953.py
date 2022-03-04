total_list = []

for i in range(5):
    A, B, C, D = map(int, input().split())
    total = A + B + C + D
    total_list.append(total)

win = max(total_list)
print(total_list.index(win) + 1, win)


############################
# 코드 리뷰
# - 참가자가 5명이기 때문에 5번 for문 돌리고 그 안에서 input 정수로 받아야함
# - A, B, C, D 모두 더하기
# - total_list를 for문 밖에서 하나 선언해서 각 참가자의 total을 리스트에 담기
# - max를 활용하여 가장 높은 점수 win에 담기
# - index를 활용하여 win의 인덱스 파악하고 +1 해주기, 그리고 w
############################