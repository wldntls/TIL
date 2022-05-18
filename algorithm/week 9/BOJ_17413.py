# https://velog.io/@bye9/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-17413-%EB%8B%A8%EC%96%B4-%EB%92%A4%EC%A7%91%EA%B8%B02
import sys 

intput = lambda: sys.stdin.readline().rstrip()

s = list(input())
tag = False
word = ""
result = ""


for i in s:
  #뒤집어서 출력
  if tag==False:
    if i=='<':
      tag=True
      word=word+i
    #중간점검
    elif i==' ':
      word=word+i
      result=result+word
      word=''
    else:
      word=i+word

  #정상적으로 출력
  elif tag==True:
    word=word+i
    if i=='>':
      tag=False
      result=result+word
      word=''

print(result+word)



# <> 밖에 있는 것 뒤집기

