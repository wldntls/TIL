

# 데이터 시각화 기초



## **2-3. 데이터 분석_기온 공공데이터**

### 1. 데이터 다운로드

- [기상자료개방포털](https://data.kma.go.kr/)

- csv 파일로 저장

- mac 

  - 텍스트 편집기로 열기 -> 복제본 만들기 -> UTF-8으로 저장 -> 이름 변경 눌러서확장자 csv 파일로 변경

- windows

  - 메모장 -> 다른이름으로 저장 -> ANSI 파일로 저장 -> 이름 변경 눌러서 확장자 csv 파일로 변경

    

### 2. 서울 기온 데이터 분석하기

- *데이터 분석을 하려는 파일과 같은 폴더에서 분석 진행해야함*

- 서울 기온 데이터 분석

  - ````python
    import csv 
    f = open('seoul.csv','r',encoding='cp949') 
    # 'r'=> 읽기 
    #encoding='cp949' => 파일을 읽기 위해 인코딩 변환(데이터 다운로드 mac 버전 실행 -> 삭제해도 오류 없음) 
    #'seoul.csv' 파일이 같은 폴더 안에 있어야함.
    
    data = csv.reader(f,delimiter=',') #delimiter -> 구분문자
    print(data)    
    f.close()

  

- 데이터 출력하기

  - ````python
    import csv 
    f = open('seoul.csv')
    data = csv.reader(f)
    for row in data:
        print(row)
    
    f.close()
    #한 줄이 리스트 형태로 출력됨
    ````



- 헤더 저장하기

  - ```python
    import csv 
    f = open('seoul.csv')
    data = csv.reader(f)
    header = next(data) # next -> data의 첫 행 읽고 다음 행으로 넘어감, 읽은 행을 header에 담은 것
    print(header)
    #헤더만 출력됨
    ```

  - ```python
    import csv 
    f = open('seoul.csv')
    data = csv.reader(f)
    header = next(data)
    for row in data:
        print(row)
    #첫 행 빼고 실데이터만 리스트 형태로 출력됨
    ```



- 서울의 가장 더웠던 날은 언제였을까? -> 서울의 최고기온이 가장 높았던 날은 언제였을까?

  - ````python
    import csv
    f = open('seoul.csv')
    data = csv.reader(f)
    header = next(data)
    
    for row in data:
        if row[-1] == '': # 만약 최고 기온이 공백이라면
            row[-1] = -999 # 최고 기온을 -999으로 할당
    				row[-1] = float(row[-1]) # 최고 기온을 실수로 변환
        print(row) # 그리고 그것을 출력해라
    ````

  - ````python
    #p.21 mission
    # 정답
    
    import csv 
    f = open('seoul.csv')
    data = csv.reader(f)
    header = next(data)
    max_temp = -999 # 최고 기온 값을 저장할 변수, 데이터에 영향을 받지 않을 수 있는 값(아주 작은 값)으로 설정
    max_date = '' # 최고 기온이 가장 높았던 날을 저장할 변수
    
    for row in data:
        if row[-1] != '': # 만약 최고 기온이 공백이 아니라면
            row[-1] = float(row[-1]) # 최고 기온을 실수로 변환, 마지막 행이기 때문에 인덱스 [-1]로 설정 [4]도 가능
            if  max_temp < row[-1]: # 만약 row[-1]값(최고 기온)이 max_temp 보다 크다면  
                max_date = row[0] # max_data에 row[0](날짜)값을 저장
                max_temp = row[-1] # 그리고 max_temp에 row[-1]값(최고 기온)을 저장
                #이를 for 문이 도는 동안 반복해서 최고 기온과 최고 기온의 날짜를 출력
    f.close()
    
    print(max_date, max_temp)
    print('기상 관측 이래 서울의 최고 기온이 가장 높았던 날은', max_date,'로',max_temp,'도 였습니다.')
    ````

---



### 3.  데이터 시각화 기초

- [matpoltlib 라이브러리](http://matplotlib.org)

- pyplot은 matpoltlib에서 지원하는 모듈 중 하나 

- 기본 그래프 그리기

  - ```python
    import matplotlib.pyplot as plt # 라이브러리 불러오기
    
    plt.plot([10,20,30,40]) # y축 값, x축은 자동으로 0부터 0.5씩 셋팅됨
    plt.show() #그래프 보여주기 
    ```

  - ````python
    import matplotlib.pyplot as plt
    
    plt.plot([1,2,3,4],[12,43,25,15]) # 각각 x축, y축
    plt.show()
    ````

  

- 그래프 제목 넣기

  - ````python
    import matplotlib.pyplot as plt
    
    plt.title('plotting') # 제목 넣기
    plt.plot([10,20,30,40])
    plt.show()
    ````



- 그래프 범례 넣기

  - ````python
    import matplotlib.pyplot as plt
    
    plt.title('legend') # 그래프 제목
    plt.plot([10,20,30,40],label='asc') # label을 통해 해당 그래프에 범례 설정
    plt.plot([40,30,20,10],label='dasc') # label을 통해 해당 그래프에 범례 설정
    plt.legend() # 범례를 표시해주는 코드, 괄호 안에 loc = 숫자를 넣으면 위치 지정할 수 있음 ex) plt.legend(loc=2)
    plt.show()
    ````

  

- 그래프 색상 바꾸기

  - ````python
    import matplotlib.pyplot as plt
    
    plt.title('color') # 그래프 제목
    plt.plot([10,20,30,40], color = 'skyblue', label = 'skyblue') #color를 넣어 색 지정
    plt.plot([40,30,20,10], color = 'pink', label = 'pink')
    plt.legend()
    plt.show()
    ````

  

- 그래프 선 모양 바꾸기

  - ````python
    import matplotlib.pyplot as plt
    
    plt.title('linestyle')
    plt.plot([10,20,30,40],color = 'r', linestyle='--', label='dasned') # 'r': 'red', linestyle 정하기
    plt.plot([40,30,20,10],color = 'g',ls = ':', label = 'dotted') # 'g' : 'green', ls = linestyle
    plt.legend() # 범례
    plt.show()
    # plt.plot([], 색상, 선모양, 범례)
    ````



- 마커 모양 바꾸기

-  ```python
   import matplotlib.pyplot as plt
   
   plt.title('marker')
   plt.plot([10,20,30,40],'r.',label='circle') # 'r.' -> 빨간색 원형 마커 그래프
   plt.plot([40,30,20,10],'g^',label='triangle up') # 'g^' -> 초록색 삼각형 마커 그래프
   plt.legend()
   plt.show()
   # plt.plot([],색상, 마커모양, 선모양, 범례)
   ```

### 4.  내 생일의 기온 변화 그래프 그리기

- 최고 기온 데이터만 읽어오기

  - ````python
    import csv
    f = open('seoul.csv')
    data = csv.reader(f)
    next(data)
    
    for row in data:
        print(row[-1]) # 최고 기온의 데이터만 출력
    ````



- 데이터 리스트에 저장하기

- ````python
  import csv 
  f =  open('seoul.csv')
  data = csv.reader(f)
  next(data)
  result = [] # 리스트를 저장할 수 있는 리스트 변수
  
  for row in data:
      if row[-1] != '': # 만약 최고 기온이 공백이 아니라면(공백 값이 아닌 데이터들만 리스트에 담은 것)
          result.append(float(row[-1])) # 최고 기온을 실수로 변환하여 result 리스트 변수에 하나씩 추가해라
  
  print(result)
  ````



- 데이터 시각화

  - ````python
    import csv 
    
    f =  open('seoul.csv')
    data = csv.reader(f)
    next(data)
    result = []
    
    for row in data:
        if row[-1] != '':
            result.append(float(row[-1]))
    
    import matplotlib.pyplot as plt # matplotlib 라이브러리 부름
    
    plt.figure(figsize = (10,2)) # figsize (가로길이, 세로길이) 설정
    plt.plot(result,'r') # 그래프 빨간색으로 설정 
    plt.show() # 출력
    ````



- 날짜 데이터 추출

  - ````python
    data = '1907-10-01'
    print(data.split('-')) # 날짜 데이터를 '-'를 기준으로 잘라서 리스트로 출력
    
    print(data.split('-')[0])
    print(data.split('-')[1])
    print(data.split('-')[2]) # 날짜 데이터를 '-'를 기준으로 줄바꿈으로 출력
    ````

  

- 데이터 시각화

  - ````python
    #특정 월 기온 데이터 추출
    import csv 
    
    f = open('seoul.csv')
    data = csv.reader(f)
    next(data)
    
    for row in data:
        if row[-1] !='': # 최고 기온이 공백이 아라면
            if row[0].split('-')[1] == '08': # 그리고 첫번째 인덱스 '-' 기준으로 1번째 인덱스(월)가 '08'이라면
                result.append(float(row[-1])) # 실수로 최고 기온 데이터를 result에 담아라
    
    plt.plot(result,'hotpink')
    plt.show() # 그래프 출력
    ````

  - ````python
    # 특정 날짜 기온 데이터 추출
    import csv 
    
    f = open('seoul.csv')
    data = csv.reader(f)
    next(data)
    result = []
    
    for row in data:
        if row[-1] != '':
            if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '14': 
              # 첫번째 인덱스 '-' 기준으로 1번 인덱스(월)는 '02', 2번 인덱스(일)는 '14'이라면 
              result.append(float(row[-1])) # 실수로 최고 기온 데이터를 result에 담아라
                
    plt.plot(result, 'hotpink')
    plt.show() # 그래프 출력
    ````

  - ````python
    # 내 생일의 최고 및 최저 기온 그래프로 그리기
    import csv 
    
    f= open('seoul.csv')
    data = csv.reader(f)
    next(data)
    high = [] # 최고 기온을 담을 리스트 변수
    low =[] # 최저 기온을 담을 리스트 변수 
    
    for row in data:
        if row[-1] != '':
            if row[0].split('-')[1] == '10' and row[0].split('-')[2] == '04':
              # 첫번째 인덱스 '-' 기준으로 1번 인덱스(월)는 '02', 2번 인덱스(일)는 '14'이라면 
                high.append(float(row[-1])) # 실수로 최고 기온 데이터를 high에 담아라
                low.append(float(row[-2])) # 실수로 최저 기온 데이터를 low에 담아라
                
    plt.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지(잘모르겠음)
    plt.rc('font',family='AppleGothic') # mac은 AppleGothic 사용해야함. 그래야지 한글 출력 가능
    plt.title('내 생일의 기온 변화 그래프') 
    plt.plot(high, 'hotpink', label = 'high')
    plt.plot(low,'blue',label = 'low')
    plt.legend()
    plt.show()
    ````

    

- 히스토그램

  - ````python
    import matplotlib.pyplot as plt
    
    plt.hist([1,1,2,3,4,5,6,6,7,8,10]) # 히스토그램 그래프 코드
    plt.show()
    ````

  - ````python
    import random
    
    dice = []
    for i in range(5): # 5번 for문 돌리고
        dice.append(random.randint(1,6)) # 1부터 6까지 정수로 랜덤하게 출력해서 dice 리스트에 담기
    
    plt.hist(dice, bins=6) # x축 값을 6칸으로 나누어 출력
    plt.show()
    ````



- 기온 데이터를 히스토그램으로 표현하기

  - ````python
    import csv
    import matplotlib.pyplot as plt
    
    f = open('seoul.csv')
    data = csv.reader(f) # 기온 데이터 불러오기
    next(data)
    result = [] # 기온 데이터를 담을 리스트 변수
    
    for row in data:
        if row[-1] != '':
            result.append(float(row[-1])) # 최고 기온 데이터 result 리스트에 담기
            
    plt.hist(result,bins=100,color = 'r') # 히스토그램으로 간격은 100, 컬러 빨강 
    plt.show() # 출력
    ````

  - ````python
    # 특정 날짜 기온 데이터 추출
    import csv
    import matplotlib.pyplot as plt
    
    f = open('seoul.csv')
    data = csv.reader(f)
    next(data)
    aug = []
    
    for row in data:
        month = row[0].split('-')[1] # 인덱스 0번째 데이터를 '-'를 기준으로 나눴을 때, 인덱스 1번째를 month에 담기
        if row[-1] != '': # 만약 최고 기온이 공백이 아니라면
            if month == '08': # 만약 month가 '08'이라면
                aug.append(float(row[-1])) # 실수로 변환하여 최고 기온을 aug 리스트에 담기
                
    plt.hist(aug,bins = 100,color = 'r') 
    plt.show()

  - ````python
    # 특정 달 2개의 기온 데이터 추출
    import csv
    import matplotlib.pyplot as plt
    
    f = open('seoul.csv')
    data = csv.reader(f)
    next(data)
    aug = []
    jan = []
    
    for row in data:
        month = row[0].split('-')[1]  # 인덱스 0번째 데이터를 '-'를 기준으로 나눴을 때, 인덱스 1번째를 month에 담기
        if row[-1] != '': # 만약 최고 기온이 공백이 아니라면
            if month == '08': # 만약 month가 '08'이라면
                aug.append(float(row[-1])) # 실수로 변환하여 최고 기온을 aug 리스트에 담기
            if month == '01': # 만약 month가 '01'이라면
                jan.append(float(row[-1])) # 실수로 변환하여 최고 기온을 jan 리스트에 담기
                
    plt.hist(aug,bins=100, color = 'r', label = "Aug")
    plt.hist(jan,bins=100, color = 'b', label = "Jan")
    plt.legend()
    
    plt.show()
    ````

    

- 박스플롯

- 기온 데이터를 상자그림으로 표현하기

  - ````python
    import matplotlib.pyplot as plt # matplotlib 라이브러리 
    import random # random 라이브러리 부르기
    result = []
    
    for row in range(13): 
        result.append(random.randint(1,1000)) # 1부터 1000까지 범위에서 난수를 정수로 13개 출력하여 result에 담기
        
    print(sorted(result)) # result 리스트를 오름차순으로 프린트
    
    plt.boxplot(result) # 박스플롯 코드 
    plt.show()
    ````

  - ```python
    import csv
    import matplotlib.pyplot as plt
    
    f = open('seoul.csv')
    data = csv.reader(f)
    next(data)
    result =[]
    
    for row in data:
        if row[-1] != '':
            result.append(float(row[-1])) # 최고 기온을 실수로 변환하여 result 리스트에 담기 
            
    plt.boxplot(result) # 박스 플롯으로 출력
    plt.show()
    ```

  - ```python
    # 특정 달 2개를 박스플롯으로 만들기
    import csv
    import matplotlib.pyplot as plt
    
    f = open('seoul.csv')
    data = csv.reader(f)
    next(data)
    aug = []
    jan = []
    
    for row in data:
        month = row[0].split('-')[1] # 인덱스 0번째 데이터를 '-'를 기준으로 나눴을 때, 인덱스 1번째를 month에 담기
        if row[-1] != '': # 만약 최고 기온이 공백이 아니라면
            if month == '08': # 만약 month가 '08'이라면
                aug.append(float(row[-1])) # 실수로 변환하여 최고 기온을 aug 리스트에 담기
            if month == '01': # 만약 month가 '01'이라면
                jan.append(float(row[-1])) # 실수로 변환하여 최고 기온을 jan 리스트에 담기
                
    plt.boxplot(aug) #박스플롯으로 aug 출력
    plt.boxplot(jan) #박스플롯으로 jan 출력
    plt.show()          
    plt.boxplot([aug,jan]) #한 그래프에 옆으로 나란히 출력
    plt.show() 
    
    ```

  - ````python
    # 월별 데이터 상자 그림으로 그리기
    import csv
    import matplotlib.pyplot as plt
    
    f = open('seoul.csv')
    data = csv.reader(f)
    next(data)
    month = [[],[],[],[],[],[],[],[],[],[],[],[]] # 12달의 기온 데이터를 담을 수 있는 리스트 변수
    
    for row in data:
        if row[-1] != '':
            month[int(row[0].split('-')[1])-1].append(float(row[-1]))
            # 0번째 인덱스 데이터를 '-'를 기준으로 나눠 1번째 인덱스를 정수로 변환하고 이를 -1하여 month 인덱스에 맵핑될 수 있도록 하여 1월, 2월, 3월 .. 각각의 기온 데이터를 담을 수 있게 한다. 
            
    plt.boxplot(month) # month 리스트 데이터를 박스 플롯으로 출력
    plt.show()
    ````

    