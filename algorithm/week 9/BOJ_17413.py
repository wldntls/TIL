# https://velog.io/@bye9/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-17413-%EB%8B%A8%EC%96%B4-%EB%92%A4%EC%A7%91%EA%B8%B02
import sys 

intput = lambda: sys.stdin.readline().rstrip()

s = list(input())
tag = False
word = ""
result = ""

# 예시 : <ab cd>ef gh<ij kl>

for i in s:
  #뒤집어서 출력
  if tag==False: 
    # print(i)
    if i=='<': # 1. <로 시작하면 tag가 true로 바뀌면서 word에 추가
      # print(i)
      tag=True
      word += i
      
    #중간점검
    elif i==' ': # 만약 중간에 공백이 있다면 
      word += i # 공백을 word에 넣고 
      result += word # 공백을 result에 넣고
      word='' # word 초기화
    else: # 그냥 문자열이면 
      word=i+word # 뒤집어서 문자열 넣기

  #정상적으로 출력
  elif tag==True: # 2. ab는 >가 나타나기 전이기 때문에 tag가 true로 고정되어 있기 때문에 정상으로 word에 들어감
    word += i
    
    if i=='>': # 3. 만약 i가 > 이면 여기로 들어와서 tag를 false로 바뀌고 
      tag=False
      result += word # 4. 정상적으로 출력됐던, word를 result에 넣음
      word='' # 5. 그리고 word 초기화 

print(result+word) # 끝에 문자열이 오면 갱신이 안되니까 맨뒤에 있는 뒤집어져있는 문자열과 같이 출력