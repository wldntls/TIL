# 2-1 Pandas-protected



## 1. 시리즈

- 데이터 주소(index)와 데이터 값(value)로 이루어져 있다.

- 딕셔너리 -> 시리즈 변환 

  - ````python
    # pandas.Series(딕셔너리)
    
    import pandas as pd
    
    dict_data = {'a':1,'b':2,'c':3}
    sr = pd.Series(dict_data)
    print(type(sr))
    print(sr)
    
    결과값
    <class 'pandas.core.series.Series'>
    a    1
    b    2
    c    3
    dtype: int64
    ````

- 시리즈의 인덱스 구조는 인덱스 이름과 정수형 위치 인덱스가 있다.

- 리스트 -> 시리즈 변환

  - ````python
    import pandas as pd
    
    list_data = ['2019-01-02',3.14,'ABC',100,True]
    sr = pd.Series(list_data)
    print(sr)
    
    결과값
    0    2019-01-02
    1          3.14
    2           ABC
    3           100
    4          True
    dtype: object
    ````

  - ````python
    idx = sr.index
    val = sr.values
    print(idx, '\n',val)
    
    결과값
    RangeIndex(start=0, stop=5, step=1) 
    ['2019-01-02' 3.14 'ABC' 100 True]
    ````

- 튜플 -> 시리즈 변환

  - ````python
    import pandas as pd
    
    tup_data = ('민수','20217-04-08','여',True)
    sr = pd.Series(tup_data,inex - ['이름','생년월일','성별','학생여부']) # 인덱스 설정 안하면 정수형 인덱스로 나옴
    
    print(sr[0]) # value 값만 출력
    print(sr['이름'])
    민수
    민수
    
    print(sr[1,2]) # key, value 값이 같이 나옴
    print(sr[['생년월일','성별']])
    생년월일    2017-04-08
    성별               여
    dtype: object
    생년월일    2017-04-08
    성별               여
    dtype: object
    
    print(sr[1:])
    print(sr['생년월일':'학생여부']) # 텍스트 인덱스는 꼭 끝을 써줘야함
    
    생년월일    2017-04-08
    성별               여
    학생여부          True
    dtype: object
    생년월일    2017-04-08
    성별               여
    학생여부          True
    dtype: object
    ````



## 2. 데이터프레임

- 시리즈들의 모임

- 딕셔너리 -> 데이터 프레임 변환

  - ````python
    # pandas.DataFrame(딕셔너리 객체)
    
    import pandas as pd
    
    dict_data = {'A':[1,2,3],'B':[4,5,6],'c':[7,8,9],'d':[10,11,12],'e':[13,14,15]}
    df = pd.DataFrame(dict_data)
    print(df)
    
       A  B  c   d   e
    0  1  4  7  10  13
    1  2  5  8  11  14
    2  3  6  9  12  15
    ````

- 행 인덱스와 열 이름 변경

  - ````python
    import pandas as pd
    
    df = pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중']],index = ['준서','예은'],columns = ['나이','성별','학교'])
    print(df.index)
    print(df.columns)
    
    결과값
    Index(['준서', '예은'], dtype='object')
    Index(['나이', '성별', '학교'], dtype='object')
    
    df.index = ['학생1','학생2'] # 행 인덱스 변경 : DataFrame 객체.index = 새로운 행 인덱스 배열
    df.columns = ['연령','남녀','소속'] # 열 이름 변경 : DataFrame 객체.colums = 새로운 열 이름 배열
    
    print(df.index)
    print(df.columns)
    
    결과값
    Index(['학생1', '학생2'], dtype='object')
    Index(['연령', '남녀', '소속'], dtype='object')
    ````

  - ````python
    # 행 인덱스 변경 : DataFrame 객체. rename(index={기존 인덱스:새 인덱스,...})
    df.rename(columns = {'나이':'연령','성별':'남녀','학교':'소속'},inplace = True) 
    # 열 이름 변경 : DataFrame 객체. rename(columns={기존 인덱스:새 이름,...})
    df.rename(index={'준서':'학생1','예은':'학생2'},inplace = True)
    
    print(df)
    
    # inplace : True -> 이 코드가 있어야 df의 행과 열이 변경
    # inplace : False or 생략 -> df.rename의 행과 열이 변경, 이럴 경우 df=~ 이렇게 다시 받아줘야 df가 변경됨
    ````

- 행/열 삭제

  - ````python
    # 행 삭제 
    
    import pandas as pd
    exam_data = {'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
    
    df = pd.DataFrame(exam_data, index=['서준','우현','인아'])
    print(df)
    
        수학  영어   음악   체육
    서준  90  98   85  100
    우현  80  89   95   90
    인아  70  95  100   90
    
    df2 = df.copy() # 원본 data에서 copy
    df2.drop('우현', axis = 0, inplace = True) # 행 삭제 : DataFrame 객체.drop(행 인덱스 또는 배열, axis=0)
    print(df2)
    
        수학  영어   음악   체육
    서준  90  98   85  100
    인아  70  95  100   90
    ````

  - ````python
    # 열 삭제
    
    df4 = df.copy()
    df4.drop('수학', axis = 1, inplace = True) # 열 삭제 : DataFrame 객체.drop(열 이름 또는 배열, axis=1)
    print(df4)
    
        영어   음악   체육
    서준  98   85  100
    우현  89   95   90
    인아  95  100   90
    ````

- 행 선택

  - ````python
    import pandas as pd
    exam_data = {'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
    
    df = pd.DataFrame(exam_data, index=['서준','우현','인아'])
    print(df)
    
        수학  영어   음악   체육
    서준  90  98   85  100
    우현  80  89   95   90
    인아  70  95  100   90
    
    label1 = df.loc['서준'] # 인덱스 이름 슬라이싱의 경우 끝 포함
    position1 = df.iloc[0] # 정수형 위치 인덱스 슬라이싱의 경우 끝 제외가능
    print(label1)
    print(position1)
    
    # label1, position1 결과
    수학     90
    영어     98
    음악     85
    체육    100
    Name: 서준, dtype: int64
    ````

  - ````python
    label2 = df.loc[['서준','우현']]
    position2 = df.iloc[[0,1]]
    print(label2)
    print(position2)
    
    label3 = df.loc['서준':'우현']
    position3 = df.iloc[0:1]
    print(label3)
    print(position3)
    
    # label2, position2, label3 결과
        수학  영어  음악   체육
    서준  90  98  85  100
    우현  80  89  95   90
    
    # position3 결과
        수학  영어  음악   체육
    서준  90  98  85  100
    ````

- 열 선택

  - ````python
    import pandas as pd
    exam_data = {'이름':['서준','우현','인아'],'수학': [90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
    df = pd.DataFrame(exam_data)
    
    math1 = df['수학'] # 대괄호 1개 -> 시리즈 출력, 대괄호 2개 -> 데이터프레임으로 출력
    print(math1)
    0    90
    1    80
    2    70
    Name: 수학, dtype: int64
    
    english = df.영어 # 속성값으로 지정 가능, 시리즈로 출력
    print(english)
    0    98
    1    89
    2    95
    
    music_gym = df[['음악','체육']]
    print(music_gym)
        음악   체육
    0   85  100
    1   95   90
    2  100   90
    ````

  - ````
    ````

  - 



