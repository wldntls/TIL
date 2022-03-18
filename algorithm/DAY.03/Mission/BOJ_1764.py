n, m = map(int, input().split()) # n, m를 공백을 기준으로 정수로 입력받기

dict = {input(): 1 for _ in range(n)} # 듣도 못한 사람의 수 n만큼을 딕셔너리의 key값으로 입력받고, value값은 1로 설정
people_list = [] # for문에서 사용할 리스트 변수 선언

for i in range(m): # 보도 못한 사람의 수 m만큼 for문 돌리기
    people = input() # 문자 입력받기
    if people in dict.keys(): # 만약 입력받은 people이 dict 딕셔너리 key값에 있다면
        people_list.append(people) # for문 밖에서 선언한 people_list 리스트에 하나씩 삽입
print(len(people_list)) # 리스트의 길이를 출력하는 함수인 len를 활용하여 듣보잡의 수를 출력
print('\n'.join(sorted(people_list))) # join함수를 활용하여 단어마다 개행을 넣어주고, sorted함수를 활용하여 이름을 사전순으로 출력

############################
# 코드 리뷰
# - 리스트에 명단을 모두 넣어서 문제를 풀려고 했었음
# - 하지만 시간복잡도 문제와 list 범위 밖을 넘어가는 오류 문제가 발생했었음
# - 그래서 딕셔너리를 활용하여 문제를 풀 수 있는 방안을 생각했음
# - 결과적으로 리스트를 활용한 것보다 훨씬 더 쉽게 결과값을 출력할 수 있었음
############################