def solution(board, moves):
    basket = [] # 인형을 담을 바구니
    answer = 0 # 갯수를 셀 변수
    
    for move in moves:
        for column in board:
            # 만약에 column의 move-1가 0이 아니라면 인형이라는 소리
            if column[move-1] != 0: 
                basket.append(column[move-1])
                column[move-1] = 0
                
                # 바구니에 2개 넘어가면 중복 확인하기 위해 
                if len(basket) > 1:
                    if basket[-1] == basket[-2]:
                        basket.pop(-1)
                        basket.pop(-1)
                        answer += 2
                break # 추가로 같은 라인의 인형이 담기는걸 방지하기 위해 
    return answer