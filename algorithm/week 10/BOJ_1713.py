# https://richard25.tistory.com/39\

# 왜 틀렸다고 나오지..?

n = int(input()) # 사진의 갯수
w = int(input()) # 전체 학생의 총 추천 횟수
num = list(input().split()) # 추천 받은 학생을 나타내는 번호
# print(num)


# Key : 후보자의 숫자
# Value : [추천 받은수, 들어온 순서]

photo = dict()
for i in range(w) :
    if num[i] in photo : # 만약 딕셔너리에 후보자의 숫자가 이미 있다면
        photo[num[i]][0] += 1 # 그 후보자의 딕셔너리 values 값에서 추천 받은 수[0]에 1을 더해라
        # print(photo[num[i]][0]
    else : # 그게 아니라면 (후보자의 숫자가 딕셔너리에 없다면)
        if len(photo) < n : # 만약 n(사진의 갯수)가 딕셔너리의 값보다 작다면 -> 사진이 아직 다 안걸린 것이기 때문에
            photo[num[i]] = [1, i] # 그 후보자의 value 값에 추천 받은 수 1을 추가하고, 들어온 순서를 넣는다
        else : # 만약 그게 아니라면 (사진이 모두 채워져 있는 상태)
            del_list = sorted(photo.items(), key= lambda x : (x[1][0] , x[1][1])) 
            # values 첫번째 값, 두번째 값 순으로 정렬 (추천 받은 횟수가 같아면 오래된 사람을 삭제해아 하기 때문에)
            del_key = del_list[0][0]
            # 가장 오래된 후보자를 삭제하게 위해 새로운 변수에 담고 
            del(photo[del_key]) # 삭제
            photo[num[i]] = [1, i] # 새로운 후보자의 수를 갱신!


ans_list = list(sorted(photo.keys())) # 후보자의 숫자를 리스트에 담고
print(" ".join(ans_list)) # 출력
# answer = str(ans_list[0]) # 첫번째 후보자의 수를 문자열로 바꾸고
# for i in ans_list[1: ] : # 
#     answer += " " + str(i)
# print(answer)