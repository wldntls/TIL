T = int(input())

for i in range(T):
    S, R = input().split()
    S = int(S)
    for j in R:
        P = j * S
        print(P, end="")
    print()


############################
# 생각 못했던 점
# - S, R은 for문 안에서 입력을 받아야 T만큼 받을 수 있음
# - S는 정수로 다시 바꿔줘야함
# 
# 코드 리뷰 설명
# - 테스트 케이스 개수 입력 받기
# - for문 안에서 S, R 입력 받고, S 정수로 바꿔주기
# - R을 for문을 이용해서 S를 곱해서 P에 담기
# -  이중 for문의 안쪽 for문에서 먼저 print(P)를 해주고, end를 이용해 한줄로 출력하게 함
# -  그리고 아래 print()를 사용해서 두번째 문자열도 출력
# 
# 피드백 
# - 변수명 대문자 쓰지 않기
############################