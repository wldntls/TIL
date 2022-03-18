T = int(input())

for i in range(T):
    k = int(input())
    k_list = [input() for i in range(k)]
    password = 0
    for j in range(k):
        for z in range(j+1, k):
            password1 = k_list[j] + k_list[z]
            password2 = k_list[z] + k_list[j]
            if password1 == password1[::-1]:
                password = password1
            if password2 == password2[::-1]:
                password = password2
    print(password)

############################
# 코드 리뷰
# - 테스트 케이스 입력받고 갯수만큼 for문 돌리기
# - for문 안에서 k개의 단어 갯수 입력 받기
# - 입력받은 단어 리스트에 담기
# - 마지막 출력을 위해 password에 0을 할당
# - 리스트 안에 모든 문자를 더하여 비교하기 위해 이중 for문 작성, 두번째 for문의 시작은 j와 겹치지 않게 하기 위해 +1을 해줌
# - password1, password2에 각각 앞뒤로 문자열을 더하여 할당
# - 만약 password1, password2가 문자열을 뒤집었을 때와 같다면 각각을 password에 할당
# - 마지막으로 password를 for문 밖에서 출력

# 피드백
# - 대문자 바꾸기
############################



