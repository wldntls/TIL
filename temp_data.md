# 데이터 시각화 기초



## **2-3. 데이터 분석_기온 공공데이터**

### 1. 데이터 다운로드

- [기상자료개방포털](https://data.kma.go.kr/)
- csv 파일로 저장
- mac 
  - 텍스트 편집기로 열기 -> 복제본 만들기 -> UTF-8으로 저장 -> 이름 변경 눌러서확장자 csv 파일로 변경
- windows
  - 메모장 -> 다른이름으로 저장 -> ANSI 파일로 저장 -> 이름 변경 눌러서 확장자 csv 파일로 변경

---



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
- 기본 그래프 그리기
  - 

- 박스플롯

- 

- 인구공공데이터 

  - 다운

  - 데이터 읽어오기

  - 신도림 인구 데이터 불러오기

  - 신도림 인구 실데이터만 불러오기

  - 읍면동을 입력받아 인구 데이터 그래프로 나타내기

    

---



> 2-4. 데이터 분석_인구 공공데이터



- **추가로 공부해야할 것**

  - 그래프 스타일 찾아보기

    