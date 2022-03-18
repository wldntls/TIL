wood_pieces = list(map(int, input().split()))

for i in range(5):
    for j in range(4):
        if wood_pieces[j] > wood_pieces[j+1]:
            wood_pieces[j], wood_pieces[j+1] = wood_pieces[j+1], wood_pieces[j]
            print(*wood_pieces) # 출력을 위해 리스트 풀어주기

        if wood_pieces == [1,2,3,4,5]:
            break

############################
# 코드 리뷰
# - 다섯개의 나무조각을 공백을 기준으로 리스트에 정수로 담는다.
# - 이중 for문을 활용하여 한번 빈복될 때마다 모든 숫자를 비교할 수 있도록 한다.
# - 그리고 작은 숫자를 앞으로 올 수 있게 한다.
# - 만약 wood_pieces가 [1,2,3,4,5] 순서로 정렬이 된다면 for문을 빠져나온다.
# - print를 할때 *를 사용하면 리스트의 괄호 없이 출력된다.
############################