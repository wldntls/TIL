word = [input() for i in range(5)]
print(word)
word_max = max(len(i) for i in word)

for i in range(word_max):
    for j in word:
        if i < len(j):
            print(j[i], end='')

############################
# 코드 리뷰
# - 단어를 5개를 for문을 돌려서 입력받고 리스트에 넣고 word 변수에 할당
# - word를 for문에서 돌려서 길이가 가장 긴 단어의 숫자를 word_max에 할당
# - 이중 for문으로 word의 0번째, 1번째를 순서대로 출력하게 한다. 
# - 길이가 짧은 열을 방지하기 위해 if문에 문자열을 비교하여 i보다 작으면 출력하는 걸로 한다. 
############################

