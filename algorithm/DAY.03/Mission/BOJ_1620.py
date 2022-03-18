n, m = map(int, input().split()) # 포켓몬의 개수인 n과 문제의 개수 m을 공백을 기준으로 정수로 입력받기

pokemon_dict = {input() : str(i) for i in range(1, n+1)}
# 포켓몬의 개수만큼 for문을 돌려서 key값으로 입력받고, i를 string으로 변환하여 value값에 넣어주기(피드백 -> 스트링으로 미리 바꿔주는 것 좋았음)
# 변수명 지정 이유 -> 포켓몬 이름을 입력받는 것이기 때문에 pokemon_dict라고 정하였습니다. 

reverse_dict = dict(map(reversed, pokemon_dict.items()))
# 딕셔너리를 뒤집기

for j in range(m): # 문제의 개수 m만큼 for문을 돌리기
    pokemon = input() # 문제를 입력받기
    if pokemon in pokemon_dict.keys(): # 만약에 입력받은 pokemon이 dict_num의 key값에 있다면 
        print(pokemon_dict[pokemon]) # pokemon_dict의 pokemon의 value값을 출력
    else:
        print(reverse_dict[pokemon]) # 그게 아니라면 뒤집어진 딕셔너리인 reverse_dict의 pokemon의 value값을 출력

# reverse가 시간복잡도가 O(n)이라서 reverse가 for문 안에서 있으면 이중 for문과 같아지기 때문에 시간초과가 났습니다. 
# 그래서 시간초과를 해결하기 위해서 reverse를 for문 밖으로 내보냈습니다. 
# 그랬더니 시간초과문제가 해결되었습니다. 