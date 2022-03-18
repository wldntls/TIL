# 아직 이해가 안된다...

def is_correct(sudoku): # 스도쿠라는 파라메터 입력받기
    for line in sudoku: # 스도쿠를 for문으로 돌려서 line에 삽입합니다.
        if len(set(line)) < 9: # 1~9에서 하나라도 중복되면 길이가 9보다 작음 (set은 중복허용 안함, 순서가 없음)
            return False 
    return True


for t in range(1, int(input()) + 1):
    # print(t,'w')
    if t > 1: 
        input() # 두개의 스도쿠를 입력 받게 되나?? 테스트 케이스 사이에 개행??

    sudoku1 = [list(map(int, input().split())) for _ in range(9)] # 한 줄이 담기게 됩니다.이중 리스트
    #print(sudoku1)

    sudoku3 = [] 
    for i in range(0, 9, 3): # 행
        for j in range(0, 9, 3): # 열
            line = [sudoku1[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            #print(line)
        
            sudoku3.append(line)
            #print(sudoku3)

    if is_correct(sudoku1) and is_correct(zip(*sudoku1)) and is_correct(sudoku3):
        print(f"Case {t}: CORRECT")
    else:
        print(f"Case {t}: INCORRECT")






