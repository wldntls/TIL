# 오늘의집 코테 문제 2번
n = input()

voice_data = [i.lower() for i in n]
#print(voice_data)

cut = []

for i in range(len(n)):
  if voice_data[i] in voice_data:
    pattern = voice_data.count(voice_data[i])
    cut.append(pattern)
#print(cut)

for j in range(len(n)):
  if max(cut) == cut[j]:
    voice_data[j] = ''
    #print(voice_data)

for z in range(len(n)):
  if voice_data[z] != '':
    print(n[z], end='')

# 만약에 voice_data에 voice_data[0]가 있다면 같은 문자인 것들을 출력해서 갯수를 센다
# 
#  