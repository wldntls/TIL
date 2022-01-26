# 데이터 시각화 기초

## 2-4. 데이터 분석_인구 공공데이터

### 1. 인구 공공데이터 가져오기

- [인구공공데이터 가져오기](https://www.mois.go.kr/)
- 파일명 : age.csv



### 2. 우리 동네 인구 구조 시각화 하기

- 신도림 인구 데이터 출력

  - ```python
    import csv 
    f = open('age.csv')
    data = csv.reader(f)
    
    for row in data:
        if '신도림' in row[0]: # 0번째 인덱스 안에 '신도림' 이 포함되어 있다면
            print(row)
    ```

  - ```python
    import csv 
    
    f = open('age.csv')
    data = csv.reader(f)
    
    for row in data:
        if '신도림' in row[0]:
            for i in row[3:]: # 3번째 인덱스부터 마지막 인덱스 데이터까지 i에 담기
                print(i)
    ```

  - ```python
    import csv 
    
    f = open('age.csv')
    data = csv.reader(f)
    result = []
    
    for row in data:
        if '신도림' in row[0]:
            for i in row[3:]:
                result.append(i) # result 리스트에 하나씩 담기 
    
    print(result)
    ```

  - ```python
    import csv 
    
    f = open('age.csv')
    data = csv.reader(f)
    result = []
    
    for row in data:
        if '신도림' in row[0]:
            for i in row[3:]:
                result.append(int(i.replace(',',''))) 
              # 정수로 바꿔주는 함수 - int(), 쉼표가 포함된 문자열이기 때문에 replace 함수로 쉼표를 공백으로 바꿔줘야 인식이 됨.
    
    print(result)
    ```

- 읍면동 입력 받아 그래프 그리기

  - ````python
    import csv 
    
    f = open('age.csv')
    data = csv.reader(f)
    result = [] # 데이터를 담을 리스트 변수
    
    dong = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해 주세요: ') # 사용자에게 읍면동을 입력받기 위한 코드
    
    for row in data:
        if dong in row[0]: # 입력받은 데이터가 0번째 인덱스에 있다면
            for i in row[3:]: # 3번째 인덱스부터 i에 담기
                result.append(int(i.replace(',',''))) # result 리스트에 담기
                
    import matplotlib.pyplot as plt 
    
    plt.style.use('ggplot') # matplotlib에서 제공하는 그래프 스타일
    plt.rc('font', family = 'AppleGothic') # 폰트 AppleGothic
    plt.title(dong + '지역의 인구구조') # 제목
    plt.plot(result)
    plt.show()
    ````



- 막대 그래프 그리기

  - ````python
    import matplotlib.pyplot as plt
    
    plt.bar(range(6),[1,2,3,5,6,7]) # 막대그래프 코드, 간격?이 6이고, 데이터값 (잘모르겠음)
    plt.show()
    ````

  - ````python
    import csv 
    
    f = open('age.csv')
    data = csv.reader(f)
    result = []
    
    for row in data:
        if '신도림' in row[0]:
            for i in row[3:]:
                result.append(int(i.replace(',','')))
    
    import matplotlib.pyplot as plt
    plt.bar(range(101),result) # 막대그래프 코드, 간격 101? 
    plt.show()
    plt.barh(range(101),result) # 가로 막대그래프 코드, 간격 101?
    plt.show()
    ````



- 항아리 모양 그래프 그리기

  - ````python
    import csv 
    
    f = open('age.csv')
    data = csv.reader(f)
    m = []
    f = []
    
    for row in data:
        if '신도림' in row[0]:
            for i in range(0,101): # 0부터 100까지 
                m.append(int(row[i+3])) # 시작이 0이니까 +3을 통해서 3번째 인덱스부터 m 리스트에 담기
                f.append(int(row[-(i+1)])) # 시작이 0이니까 -와 +1를 사용하여 뒤에서 부터 f 리스트에 담기
    
    f.reverse() # f 리스트 뒤집기
    print(m)
    print(f)
    ````

  - ````python
    import csv
    f = open('gender.csv')
    data = csv.reader(f)
    m = []
    f = []
    
    for row in data:
        if '신도림' in row[0]:
            for i in row[3:104]: # 3 인덱스부터 104 인덱스까지가 실데이터
                m.append(int(i.replace(',','')))
            for i in row[106:207]: # 106 인덱스부터 207 인덱스까지가 실데이터 (오류관련 밑에 추가설명*1)
              	f.append(int(i.replace(',','')))
                
    import matplotlib.pyplot as plt
    
    plt.barh(range(101),m)
    plt.barh(range(101),f)
    plt.show()
    ````

  - 1 : row[106:] 만 썻을때는 'ValueError: shape mismatch: objects cannot be broadcast to a single shape' 이러한 오류가 떴음.

    -> 지정된 x 축의 데이터 개수 (range(101))와 파일에 있는 데이터의 갯수가 일치하지 않아 발생한 에러, row[106:207] 이런식으로 값을 지정해줘야 오류가 안남

  - ````python
    import csv
    f = open('gender.csv')
    data = csv.reader(f)
    m = []
    f = []
    
    for row in data:
        if '신도림' in row[0]:
            for i in row[3:104]: 
                m.append(int(i.replace(',','')))
            for i in row[106:207]: 
              	f.append(-int(i.replace(',',''))) # 위에 코드에서 -만 추가함 -> 반대로 되면서 항아리 그래프 완성!
                
    import matplotlib.pyplot as plt
    
    plt.barh(range(101),m)
    plt.barh(range(101),f)
    plt.show()
    ````

  - ````python
    import matplotlib.pyplot as plt
    
    plt.rc('font', family ='AppleGothic')
    plt.title('신도림 지역의 남녀 성별 인구 분포') # 제목
    
    plt.rcParams['axes.unicode_minus'] =False # 마이너스 기호 깨짐 방지
    plt.barh(range(101),m,label = '남성') # 가로 막대, 간격 101?, 범례설정
    plt.barh(range(101),f,label = '여성') # 가로 막대, 간격 101?, 범례설정
    plt.legend() # 범례
    plt.show()
    ````

  - ````python
    import csv
    f = open('gender.csv')
    data = csv.reader(f)
    m = []
    f = []
    
    name = input('찾고 싶은 지역의 이름을 알려주세요 : ')
    
    for row in data:
        if name in row[0]:
            for i in row[3:104]:
                m.append(-int(i.replace(',','')))
            for i in row[106:207]:
                f.append(int(i.replace(',','')))
            break # break 안하면 shape mismatch 에러남!
    
    import matplotlib.pyplot as plt
    
    plt.style.use('ggplot')
    plt.figure(figsize=(10,5),dpi=300)
    plt.rc('font',family='AppleGothic')
    plt.rcParams['axes.unicode_minus'] =False
    plt.title(name + '지역의 남녀 성별 인구 분포')
    plt.barh(range(101),m,label= '남성')
    plt.barh(range(101),f,label= '여성')
    plt.legend()
    plt.show()
    ````

- 인구 구조를 파이차트로 표현하기

  - ````python
    import matplotlib.pyplot as plt
    
    plt.pie([10,20]) #파이차트로 나타내는 코드
    plt.show()
    ````

  - ````python
    import matplotlib.pyplot as plt
    
    size = [2441,2312,1031,1233]
    plt.axis('equal') # 이게 뭐지?
    plt.pie(size) 
    plt.show()
    ````

  - ````python
    import matplotlib.pyplot as plt
    
    plt.rc('font', family = "AppleGothic")
    size = [2441,2312,1031,1233]
    label = ['A형','B형','AB형','O형'] # 레이블을 추가하기 위해 리스트에 담음
    plt.axis('equal')
    plt.pie(size, labels =label) # 위에 담은 레이블을 labels에 할당
    plt.show()
    ````

  - ````python
    import matplotlib.pyplot as plt
    
    plt.rc('font',family = 'AppleGothic')
    size = [2441,2312,1031,1233]
    label = ['A형','B형','AB형','O형']
    plt.axis('equal')
    plt.pie(size,labels = label, autopct='%.1f%%') # autopct 으로 그래프 안에 %를 출력해줌 (비율 출력)
    plt.legend() # 범례
    plt.show()
    ````

  - ````python
    import matplotlib.pyplot as plt
    
    plt.rc('font', family='AppleGothic')
    size = [2441,2312,1031,1233]
    label = ['A형','B형','AB형','O형']
    color = ['darkmagenta','deeppink','hotpink','pink'] # 색추가
    plt.axis('equal')
    plt.pie(size,labels=label,autopct = '%.1f%%',colors=color, explode = (0,0,0.1,0)) 
    # explode 돌출 효과주기 위해 나머지 0, 효과주고 싶은 범위만 0.1로 설정
    plt.legend()
    plt.show()
    ````



- 원하는 지역의 성별 인구를 파이 차트로 그리기

  - ````python
    import csv 
    
    f = open('gender.csv')
    data = csv.reader(f)
    size = []
    name = input('찾고 싶은 지역의 이름을 알려주세요 : ') # 읍면동을 입력받기 위해 input 받기
    for row in data: # data를 순서대로 row에 넣기
        if name  in row[0]: # name이 만약 0번째 행과 같다면
            m = 0 
            f = 0
            for i in range(101): #0부터 100까지 i로 for문 돌리기
                m += int(row[i+3].replace(',',''))
                # 남성 실데이터가 3인덱스 부터 시작하기 때문에 +3을 하고, 쉼표를 공백으로 바꾸고 실수로 변환하여 m에 담기
                f += int(row[i+106].replace(',',''))
                # 여성 실데이터가 106인덱스 부터 시작하기 때문에 +106을 하고, 쉼표를 공백으로 바꾸고 실수로 변환하여 f에 담기
            break # break 안하면 shape mismatch 에러남!
            
    size.append(m)
    size.append(f)
    # m,f를 각각 size 리스트에 담기
    
    import matplotlib.pyplot as plt
    plt.rc('font', family='AppleGothic')
    color = ['crimson','darkcyan']
    plt.axis('equal')
    plt.pie(size, labels =['남','여'],autopct='%.1f%%',colors = color, startangle=90) 
    # 리스트에 담은 m,f의 labels을 정해주고, autopct으로 파이 차트 안에 비율 표시해주고, color 넣어주고, startangle로 각도지정 
    plt.title(name+'지역의 남녀 성별 비율')
    # 입력받은 name과 결합하여 제목 지정
    plt.show()
    
    ````



- 원하는 지역의 성별 인구를 꺽은선 그래프로 표현하기

  - ````python
    import csv 
    f= open('gender.csv')
    data = csv.reader(f)
    m = [] # 남성인구를 담을 리스트 변수
    f = [] # 여성인구를 담을 리스트 변수
    
    name = input('궁금한 동네를 입력해주세요 : ')
    
    for row in data:
        if name in row[0]:
            for i in range(3,104): # 실데이터가 3인덱스부터 시작 
                m.append(int(row[i].replace(',',''))) # 남성인구 3인덱스부터 104인덱스까지
                f.append(int(row[i+103].replace(',',''))) # 여성 인구 106인덱스부터 207인덱스까지
            break # 빠져나가기 위한 코드
    
    import matplotlib.pyplot as plt
    plt.plot(m, label ='Male')
    plt.plot(f, label = "Female")
    plt.legend()
    plt.show()
    ````



- 원하는 지역의 연령대별로 인구 성별이 어떻게 차이가 나는지 막대그래프로 확인하기

  - ````python
    import csv
    
    f= open('gender.csv')
    
    data = csv.reader(f)
    result = []
    
    name = input('궁금한 동네를 입력해주세요: ')
    
    for row in data:
        if name in row[0]:
            for i in range(3,104):
                result.append(int(row[i].replace(',', ''))-int(row[i+103].replace(',', '')))
                # 남성의 인구와 여성의 인구수가 연령대별로 얼마나 차이가 나는지 확인하기 위한 코드
            break
     
            
    import matplotlib.pyplot as plt
    
    plt.bar(range(101),result) # 범위가 101?
    plt.show()
    ````



- 산점도로 표현하기

  - ```python
    import matplotlib.pyplot as plt
    
    plt.style.use('ggplot') # 격자무늬 추가
    plt.scatter([1,2,3,4],[10,30,20,40]) # 산점도로 표현하기 위한 코드
    plt.show()
    ```

  - ````python
    import matplotlib.pyplot as plt
    
    plt.scatter([1,2,3,4],[10,30,20,40], s=[100,200,250,300],c = ['red','blue','green','gold']) 
    # s는 크기, c는 색상
    plt.show()
    ````

  - ````python
    import matplotlib.pyplot as plt
    
    plt.scatter([1,2,3,4],[10,30,20,40], s=[100,200,250,300],c = range(4)) # 컬러바의 3색상까지
    plt.colorbar() # 그래프 옆에 컬러바가 나타남
    plt.show()

  - ````python
    import matplotlib.pyplot as plt
    
    plt.scatter([1,2,3,4],[10,30,20,40], s=[100,200,250,300],c = range(4), cmap ='jet')
    # cmap은 컬러바를 지정하는 것 color 스타일이 미리 정해져 있는 것을 가져다 쓰는 것
    plt.colorbar()
    plt.show()
    ````

  - ````python
    import matplotlib.pyplot as plt
    import random 
    x = [] # x 축의 랜덤 숫자를 담을 리스트 변수
    y = [] # y 축의 랜덤 숫자를 담을 리스트 변수
    
    size = [] # size의 랜덤 숫자를 담을 리스트 변수
    
    for i in range(100):
        x.append(random.randint(50,100)) # 50부터 100까지의 난수를 정수로 추출하여 x리스트에 담기
        y.append(random.randint(50,100)) # 50부터 100까지의 난수를 정수로 추출하여 y리스트에 담기
        size.append(random.randint(10,100)) # 10부터 100까지의 난수를 정수로 추출하여 size리스트에 담기
        
    plt.scatter(x, y, s= size) # 버블 차트로 출력하고 s도 난수로 받아서 표현
    plt.show()
    ````

  - ````python
    import matplotlib.pyplot as plt
    import random 
    x = []
    y = []
    
    size = []
    
    for i in range(100):
        x.append(random.randint(50,100))
        y.append(random.randint(50,100))
        size.append(random.randint(10,100))
        
    plt.scatter(x, y, s= size, c = size, cmap= 'jet', alpha=0.7) 
    # c는 색상의 숫자, cmap 색상 설정, alpha는 투명도 설정
    plt.colorbar() # color 바 설정
    plt.show()
    ````

  
  
