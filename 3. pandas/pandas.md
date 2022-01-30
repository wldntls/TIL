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

  - ````python
    df.iloc[ : :2] # 행 슬라이싱 간격 2
    	수학	영어	음악	체육
    서준	90	98	85	100
    인아	70	95	100	90
    
    df.iloc[0:3:2] # 0부터 3 인덱스까지 출력하는데 슬라이싱 간격은 2
    	수학	영어	음악	체육
    서준	90	98	85	100
    인아	70	95	100	90
    
    df.iloc[ : :-1] # 인덱스를 뒤집어서 2부터 0인덱스 순으로 출력
    	수학	영어	음악	체육
    인아	70	95	100	90
    우현	80	89	95	90
    서준	90	98	85	100
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




- 원소 선택

  - ````python
    import pandas as pd
    exam_data = {'이름':['서준','우현','인아'],'수학': [90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
    df = pd.DataFrame(exam_data)
    
    df.set_index('이름', inplace = True) # 원래는 정수형 인덱스, 해당 코드를 사용하면 이름이 인덱스가 됨.
    print(df)
        수학  영어   음악   체육
    이름                  
    서준  90  98   85  100
    우현  80  89   95   90
    인아  70  95  100   90
    
    # 데이터프레임 df의 특성 원소 1개 선택
    a = df.loc['서준','음악']
    print(a)
    85
    
    b = iloc[0,2]
    print(b)
    85
    
    # 데이터프래임 df의 특정 원소 2개 이상 선택('서준'의 '음악','체육' 점수)
    c = df.loc['서준',['음악','체육']]
    print(c)
    d = df.iloc[0,[2,3]]
    print(d)
    e = df.loc['서준','음악':'체육']
    print(e)
    f = df.iloc[0,2:]
    print(f)
    
    # c,d,e,f의 출력 결과
    음악     85
    체육    100
    Name: 서준, dtype: int64
        
    # df 2개 이상의 행과 열에 속하는 원소들 선택 ('서준','우현'의 '음악','체육' 점수)
    g = df.loc[['서준','우현'],['음악','체육']]
    print(g)
    h = df.iloc[[0,1],[2,3]]
    print(h)
    i = df.loc ['서준':'우현','음악':'체육']
    print(i)
    j = df.iloc[0:2,2:]
    print(j)
    
    # g,h,i,j의 출력
        음악   체육
    이름         
    서준  85  100
    우현  95   90
    ````



- 열 추가

  - ````python
    import pandas as pd
    exam_data = {'이름':['서준','우현','인아'],'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
    
    df = pd.DataFrame(exam_data)
    
    df['국어'] = 80 # '국어' 열 추가, 데이터 값은 80으로 지정
    print(df)
       이름  수학  영어   음악   체육  국어
    0  서준  90  98   85  100  80
    1  우현  80  89   95   90  80
    2  인아  70  95  100   90  80
    ````



- 행 추가

  - ````python
    import pandas as pd
    exam_data = {'이름':['서준','우현','인아'],'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
    
    df.loc[3] = 0 # 새로운 행 이름 '3'에 데이터 값 0을 추가
    print(df)
       이름  수학  영어   음악   체육
    0  서준  90  98   85  100
    1  우현  80  89   95   90
    2  인아  70  95  100   90
    3   0   0   0    0    0
    
    df.loc[4] = ['동규',90,80,70,60] # 새로운 행 이름 '4'에 데이터 값 여러 개를 추가
    print(df)
       이름  수학  영어   음악   체육
    0  서준  90  98   85  100
    1  우현  80  89   95   90
    2  인아  70  95  100   90
    3   0   0   0    0    0
    4  동규  90  80   70   60
    
    df.loc['행5'] = df.loc[3] # 새로운 행 이름 '행5'에 행 '3'을 복사하여 출력
    print(df)
        이름  수학  영어   음악   체육
    0   서준  90  98   85  100
    1   우현  80  89   95   90
    2   인아  70  95  100   90
    3    0   0   0    0    0
    4   동규  90  80   70   60
    행5   0   0   0    0    0
    ````

    

- 원소 값 변경

  - ````python
    import pandas as pd
    exam_data = {'이름':['서준','우현','인아'],'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
    df = pd.DataFrame(exam_data)
    
    df.set_index('이름',inplace=True) # 인덱스를 이름으로 설정
    print(df)
        수학  영어   음악   체육
    이름                  
    서준  90  98   85  100
    우현  80  89   95   90
    인아  70  95  100   90
    
    df.iloc[0][3] = 80 # 정수형 인덱스 행 0인덱스, 열 3인덱스 80으로 변경
    print(df)
        수학  영어   음악  체육
    이름                 
    서준  90  98  100  80
    우현  80  89   95  90
    인아  70  95  100  90
    
    df.loc['서준',['음악','체육']] = 50 # 이름 인덱스 행 서준, 열 음악, 체육 50으로 변경
    print(df)
        수학  영어   음악  체육
    이름                 
    서준  90  98   50  50
    우현  80  89   95  90
    인아  70  95  100  90
    
    df.loc['서준',['음악','체육']] = 100, 50 # 이름 인덱스 행 서준, 열 음악 100, 체육 50으로 변경
    print(df)
        수학  영어   음악  체육
    이름                 
    서준  90  98  100  50
    우현  80  89   95  90
    인아  70  95  100  90
    ````

  

- 행, 열의 위치 바꾸기

  - ````python
    # df.transpose() = df.T 행열이 바뀜
    
    import pandas as pd
    exam_data = {'이름':['서준','우현','인아'],'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
    
    df = pd.DataFrame(exam_data)
    
    df = df.transpose()
    print(df)
          0   1    2
    이름   서준  우현   인아
    수학   90  80   70
    영어   98  89   95
    음악   85  95  100
    체육  100  90   90
    
    df = df.T
    print(df) # 다시 원래대로 바뀜
       이름  수학  영어   음악   체육
    0  서준  90  98   85  100
    1  우현  80  89   95   90
    2  인아  70  95  100   90
    ````



- 특정 열을 행 인덱스로 설정

  - ````python
    import pandas as pd
    exam_data = {'이름':['서준','우현','인아'],'수학':[90,80,70],'영어':[98,89,95],'음악':[85,95,100],'체육':[100,90,90]}
    
    df = pd.DataFrame(exam_data)
    
    ndf = df.set_index(['이름']) # 이름을 인덱스로
    print(ndf)
        수학  영어   음악   체육
    이름                  
    서준  90  98   85  100
    우현  80  89   95   90
    인아  70  95  100   90
    
    ndf2 = ndf.set_index('음악') # 기존의 인덱스(이름) 없어지고 음악이 새로운 인덱스로 
    print(ndf2)
         수학  영어   체육
    음악              
    85   90  98  100
    95   80  89   90
    100  70  95   90
    
    ndf3 = ndf.set_index(['수학','음악']) # 기존의 인덱스(이름) 없어지고 수학, 음악이 새로운 인덱스로
    print(ndf3)
            영어   체육
    수학 음악          
    90 85   98  100
    80 95   89   90
    70 100  95   90
    ````



- 행 인덱스 재배열

  - ````python
    import pandas as pd
    dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
    
    df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
    print(df)
        c0  c1  c2  c3  c4
    r0   1   4   7  10  13
    r1   2   5   8  11  14
    r2   3   6   9  12  15
    
    new_index = ['r0','r1','r2','r3','r4'] # 새로운 인덱스 리스트 new-index 변수에 담기
    ndf = df.reindex(new_index) # 새로운 인덱스 설정 -> 공백은 NaN으로 출력
    print(ndf)
         c0   c1   c2    c3    c4
    r0  1.0  4.0  7.0  10.0  13.0
    r1  2.0  5.0  8.0  11.0  14.0
    r2  3.0  6.0  9.0  12.0  15.0
    r3  NaN  NaN  NaN   NaN   NaN
    r4  NaN  NaN  NaN   NaN   NaN
    
    new_inde = ['r0','r1','r2','r3','r4']
    ndf2 = df.reindex(new_index, fill_value = 0.0) # fill_value 설정으로 NaN 값 설정가능 0.0 실수, 0 정수
    print(ndf2)
         c0   c1   c2    c3    c4
    r0  1.0  4.0  7.0  10.0  13.0
    r1  2.0  5.0  8.0  11.0  14.0
    r2  3.0  6.0  9.0  12.0  15.0
    r3  0.0  0.0  0.0   0.0   0.0
    r4  0.0  0.0  0.0   0.0   0.0
    ````



- 행 인덱스 초기화

  - ````python
    import pandas as pd
    dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
         
    df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
    
    ndf = df.reset_index() # 인덱스로 설정되어 있던 행을 하나의 열 인덱스로 처리
    print(ndf)
      index  c0  c1  c2  c3  c4
    0    r0   1   4   7  10  13
    1    r1   2   5   8  11  14
    2    r2   3   6   9  12  15
    ````



- 데이터프레임 정렬

  - ````python
    # 행 인덱스를 기준으로 데이터프레임 정렬
    import pandas as pd
    dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
    
    df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
    
    ndf = df.sort_index(ascending=False) # 인덱스를 기준으로 내림차순 정렬, True는 오름차순으로 정렬
    print(ndf)
        c0  c1  c2  c3  c4
    r2   3   6   9  12  15
    r1   2   5   8  11  14
    r0   1   4   7  10  13
    
    # 열 기준으로 데이터프레임 정렬
    ndf = df.sort_values(by='c1',ascending=False) # c1을 기준으로 내림차순 정렬
    print(ndf)
        c0  c1  c2  c3  c4
    r2   3   6   9  12  15
    r1   2   5   8  11  14
    r0   1   4   7  10  13
    ````



- 시리즈 연산 

  - ````python
    # 시리즈 vs 숫자
    
    import pandas as pd
    student1 = pd.Series({'국어':100,'영어':80,'수학':90})
    print(student1)
    국어    100
    영어     80
    수학     90
    dtype: int64 # type 정수
    
    percentage = student1/200 # 시리즈를 숫자 200으로 나누기
    print(percentage)
    print(type(percentage))
    국어    0.50
    영어    0.40
    수학    0.45
    dtype: float64 # type 실수
    ````

  - ````python
    # 시리즈 vs 시리즈
    import pandas as pd
    student1 = pd.Series({'국어':100,'영어':80,'수학':90})
    student2 = pd.Series({'수학':80,'국어':90,'영어':80})
    
    # 두 학생의 과목별 점수로 사칙연산 수행(시리즈+시리즈)
    addition = student1 + student2
    subtraction = student1 - student2
    multiplication = student1*student2
    division = student1/student2
    print(type(division))
    <class 'pandas.core.series.Series'>
    
    result = pd.DataFrame([addition, subtraction, multiplication, division],index = ['덧셈','뺄셈','곱셈','나눗셈'])
    
    print(result)
                  국어        수학      영어
    덧셈    190.000000   170.000   160.0
    뺄셈     10.000000    10.000     0.0
    곱셈   9000.000000  7200.000  6400.0
    나눗셈     1.111111     1.125     1.0
    ````

  - ````python
    import pandas as pd
    import numpy as np
    
    student1 = pd.Series({'국어':np.nan,'영어':80,'수학':90})
    student2 = pd.Series({'수학':80,'국어':90})
    
    # 두 학생의 과목별 점수로 사칙연산 수행(시리즈+시리즈)
    addition = student1 + student2
    subtraction = student1 - student2
    multiplication = student1*student2
    division = student1/student2
    print(type(division))
    <class 'pandas.core.series.Series'>
    
    result = pd.DataFrame([addition, subtraction, multiplication, division],index = ['덧셈','뺄셈','곱셈','나눗셈'])
    
    print(result) # '국어':np.nan, 영어 x 이기 때문에 연산 값도 NaN 으로 출력됨
         국어        수학  영어
    덧셈  NaN   170.000 NaN
    뺄셈  NaN    10.000 NaN
    곱셈  NaN  7200.000 NaN
    나눗셈 NaN     1.125 NaN
    ````

  - ````python
    # 연산 메소드
    import pandas as pd
    import numpy as np
    
    student1 = pd.Series({'국어':np.nan,'영어':80,'수학':90})
    student2 = pd.Series({'수학':80,'국어':90})
    
    # 두 학생의 과목별 점수로 사칙연산 수행(연산 메소드 사용)
    sr_add = student1.add(student2, fill_value=0) 
    sr_sub = student1.sub(student2, fill_value=0)
    sr_mul = student1.mul(student2, fill_value=0)
    sr_div = student1.div(student2, fill_value=0) # student2 내가 더한, 뺄, 곱, 나눌 값 ,fill_value NaN 값 출력안됨
    
    result = pd.DataFrame([sr_add,sr_sub,sr_mul,sr_div],index = ['덧셈','뺄셈','곱셈','나눗셈'])
    
    print(result)
           국어        수학    영어
    덧셈   90.0   170.000  80.0
    뺄셈  -90.0    10.000  80.0
    곱셈    0.0  7200.000   0.0
    나눗셈   0.0     1.125   inf # inf 무한대
    ````



- 데이터프레임 연산

  - ````python
    # 데이터프레임 vs 숫자
    import pandas as pd
    import seaborn as sns # seaborn 라이브러리 가져오기
    
    titanic = sns.load_dataset('titanic') # seaborn에서 titanic 데이터 가져오기
    df = titanic.loc[:, ['age','fare']] # titanic 전체 행(:), 열은 'age','fare' 가져오겠다
    print(df.head()) # 첫 5행만 표시
        age     fare
    0  22.0   7.2500
    1  38.0  71.2833
    2  26.0   7.9250
    3  35.0  53.1000
    4  35.0   8.0500
    
    addition = df +10 # 데이터프레임에 숫자 10 더하기
    print(addition.head())
        age     fare
    0  32.0  17.2500
    1  48.0  81.2833
    2  36.0  17.9250
    3  45.0  63.1000
    4  45.0  18.0500
    ````

  - ````python
    # 데이터프레임 vs 데이터프레임
    import pandas as pd
    import seaborn as sns
    
    titanic = sns.load_dataset('titanic')
    df = titanic.loc[:, ['age','fare']]
    print(df.tail()) # 마지막 5행 표시
          age   fare
    886  27.0  13.00
    887  19.0  30.00
    888   NaN  23.45
    889  26.0  30.00
    890  32.0   7.75
    
    addition = df +10 # 데이터프레임에 숫자 10 더하기
    print(addition.tail()) # 마지막 5행 표시
          age   fare
    886  37.0  23.00
    887  29.0  40.00
    888   NaN  33.45
    889  36.0  40.00
    890  42.0  17.75
    
    subtraction = addition - df # 데이터프레임끼리 연산하기(addition - df)
    print(subtraction.tail()) # 마지막 5행 표시
          age  fare
    886  10.0  10.0
    887  10.0  10.0
    888   NaN  10.0
    889  10.0  10.0
    890  10.0  10.0
    ````

    

## 3. 데이터 입출력

- 외부 파일 읽어오기

  - ````python
    # CSV파일 -> 데이터프레임 : pandas.read_csv("파일경로(이름)")
    import pandas as pd
    file_path = r'/Users/shinjiwoo/student/project 1/read_csv_sample.csv' # 현재 경로
    
    df1 = pd.read_csv(file_path)
    print(df1) # 기본 컬럼명 -> 첫행, 기본 행 인덱스 -> 정수형 인덱스
       c0  c1  c2  c3
    0   0   1   4   7
    1   1   2   5   8
    2   2   3   6   9
    
    df2 = pd.read_csv(file_path,header=None) # 원래 header가 c0,c1,c2,c3이었는데 none으로 입력하면 첫행까지 데이터로 보면서 자동으로 정수형 인덱스가 지정됨
    print(df2)
        0   1   2   3
    0  c0  c1  c2  c3
    1   0   1   4   7
    2   1   2   5   8
    3   2   3   6   9
    
    df3 = pd.read_csv(file_path,index_col=None) # 인덱스 값을 숫자로 정하게 됨. 해당 데이터는 원래 숫자형 인덱스로 지정되어 있어서 데이터 변화 없음
    print(df3)
       c0  c1  c2  c3
    0   0   1   4   7
    1   1   2   5   8
    2   2   3   6   9
    
    df4 = pd.read_csv(file_path,index_col='c0') #c0가 인덱스로 지정됨
    print(df4)
    ````

  - ````python
    # Excel -> 데이터프레임 : pandas.read_excel("파일경로(이름)")
    import pandas as pd
    
    df1 = pd.read_excel('../data/남북한발전전력량.xlsx') # header=0 (default 옵션)
    df2 = pd.read_excel('../data/남북한발전전력량.xlsx', header = None) # header = None 옵션
    
    print(df1)
    print(df2)
    ````

  - ````python
    import pandas as pd
    
    df1 = pd.read_excel('./stocks.xlsx', sheet_name = ['stock2016','stock2017','stock2018'], engine="openpyxl") # 시트이름 지정해서 시트 데이터 열기
    
    print(df1)
    ````

  - ````python
    # json 파일 
    import pandas as pd
    
    df = pd.read_json('./read_json_sample.json') # read_json() 함수로 데이터프레임 변환
    
    print(df)
               name  year        developer opensource
    pandas           2008    Wes Mckinneye       True
    NumPy            2006  Travis Oliphant       True
    matplotlib       2003   John D. Hunter       True
    
    print(df.index)
    Index(['pandas', 'NumPy', 'matplotlib'], dtype='object')
    ````

  - ````python
    # html 파일
    import pandas as pd
    
    url ='./sample.html'
    tables = pd.read_html(url)
    
    print(len(tables)) # tables의 개수 확인
    2
    
    for i in range(len(tables)): # for문 돌려서 2개 표 출력
        print("tables[%s]"% i)
        print(tables[i])
        print('\n')
        
    df = tables[1 # 파이썬 패키지 정보가 들어있는 두 번째 데이터프레임을 선택하여 df 변수에 저장
    
    df.set_index(['name'],inplace=True) # 'name' 열을 인덱스로 지정
    print(df)
    ````



## 4. 데이터 살펴보기

- 데이터 내용

  - ````python
    import pandas as pd
    
    df = pd.read_csv('./auto-mpg.csv',header=None) #read_csv() 함수로 df todtjd
    
    # 열 이름 지정
    df.columns = ['mpg','cylinders','displacement','horespower','weight','acceleration','model year','origin','name']
    
    print(df.head()) # 처음 5개 행
    
    print(df.tail()) # 마지막 5개 행
    
    print(df.shape) # df의 모양과 크기 확인: (행의 개수, 열의 개수)를 투플로 반환
    (398, 9)
    
    print(df.info()) # 데이터프레임의 기본 정보
    ````

    

- 데이터 요약 정보 확인하기

  - ````python
    import pandas as pd
    
    df = pd.read_csv('./auto-mpg.csv',header=None) #read_csv() 함수로 df todtjd
    
    df.columns = ['mpg','cylinders','displacement','horespower','weight','acceleration','model year','origin','name']
    
    print(df.shape) # df의 모양과 크기 확인: (행의 개수, 열의 개수)를 투플로 반환
    (398, 9)
    
    print(df.info()) # 데이터프레임의 기본 정보
    ````

  - | 판다스 자료형           | 파이썬 자료형                  | 비고                            |
    | ----------------------- | ------------------------------ | ------------------------------- |
    | int64                   | Int                            | 정수형 데이터                   |
    | float64                 | float                          | 실수형 데이터(소수점이 있는 수) |
    | object                  | string                         | 문자열 데이터                   |
    | datetime64, timedelta64 | 없음(datetime 라이브러리 활용) | 시간 데이터                     |

  - ```python
    print(df.dtypes) # 데이터프레임 df의 자료형 확인
    mpg             float64
    cylinders         int64
    displacement    float64
    horespower       object
    weight            int64
    acceleration    float64
    model year        int64
    origin            int64
    name             object
    dtype: object
    
    print(df.mpg.dtypes) # 시리즈(mog 열)의 자료형 확인
    float64
    
    # 기술 통계 정보 요약
    print(df.describe()) # 산술데이터만 가능
    
    print(df.describe(include ='all')) # all 입력하면 추가로 밑에 3가지 추가됨(unique, top, freq), object 까지 포함해서 출력

  

- 데이터 개수 확인

  - ````python
    import pandas as pd
    
    df = pd.read_csv('./auto-mpg.csv',header=None)
    df.columns = ['mpg','cylinders','displacement','horespower','weight','acceleration','model year','origin','name']
    
    print(df.count())
    mpg             398
    cylinders       398
    displacement    398
    horespower      398
    weight          398
    acceleration    398
    model year      398
    origin          398
    name            398
    dtype: int64
    
    print(type(df.count())) 
    <class 'pandas.core.series.Series'>
    
    unique_values = df['origin'].value_counts() # 데이터프레임 df의 특정 열이 가지고 있는 고유값 확인
    print(unique_values)
    1    249
    3     79
    2     70
    Name: origin, dtype: int64
    
    print(type(unique_values))
    <class 'pandas.core.series.Series'>
    ````

  

- 통계 함수 적용

  - ````python
    # 평균값
    print(df.mean())
    mpg               23.514573
    cylinders          5.454774
    displacement     193.425879
    weight          2970.424623
    acceleration      15.568090
    model year        76.010050
    origin             1.572864
    dtype: float64
      
    print(df['mpg'].mean())
    print(df.mpg.mean())
    23.514572864321615
    
    print(df[['mpg','weight']].mean())
    mpg         23.514573
    weight    2970.424623
    dtype: float64
    
    # 중간값
    print(df.median())
    mpg               23.0
    cylinders          4.0
    displacement     148.5
    weight          2803.5
    acceleration      15.5
    model year        76.0
    origin             1.0
    dtype: float64
      
    print(df['mpg'].median())
    mpg               23.0
    cylinders          4.0
    displacement     148.5
    weight          2803.5
    acceleration      15.5
    model year        76.0
    origin             1.0
    dtype: float64
      
    print(df.mpg.median())
    23.0
    
    # 최대값
    print(df.max())
    mpg                         46.6
    cylinders                      8
    displacement               455.0
    horespower                     ? # object 형태, 가장 큰값 출력
    weight                      5140
    acceleration                24.8
    model year                    82
    origin                         3
    name            vw rabbit custom # object 형태, 가장 큰값 출력
    dtype: object
      
    print(df['mpg'].max())
    46.6
    
    # 최소값
    print(df.min())
    mpg                                 9.0
    cylinders                             3
    displacement                       68.0
    horespower                          100 # object 형태, 가장 작은값 출력
    weight                             1613
    acceleration                        8.0
    model year                           70
    origin                                1
    name            amc ambassador brougham # object 형태, 가장 작은값 출력
    dtype: object
    
    print(df['mpg'].min())
    9.0
    
    # 표준편차 (문자열 계산 안함)
    print(df.std())
    mpg               7.815984
    cylinders         1.701004
    displacement    104.269838
    weight          846.841774
    acceleration      2.757689
    model year        3.697627
    origin            0.802055
    dtype: float64
      
    print(df['mpg'].std())
    7.815984312565782
    
    # 상관계수 (두 열 사이의 얼마나 상관도가 있는지 , - : 음의 상관관계, + : 양의 상관관계)
    print(df.corr() # 데이터프레임으로 출력
    - 판다스 자료 참고 
    
    print(df[['mpg','weight']].corr()) # 2개의 열을 따로 출력하는 것도 가능
                 mpg    weight
    mpg     1.000000 -0.831741
    weight -0.831741  1.000000
    
    # 0.5 이상 상관관계 어느정도 있음 
    # 0.5 이하 상관관계 거의 없음
    ````



- 판다스 내장 그래프 도구 활용

  

  - | Kind 옵션 | 설명                 |
    | --------- | -------------------- |
    | line      | 선 그래프            |
    | bar       | 수직 막대 그래프     |
    | barh      | 수평 막대 그래프     |
    | his       | 히스토그램           |
    | box       | 박스플롯             |
    | kde       | 커널 밀도 그래프     |
    | area      | 면적 그래프          |
    | pie       | 파이 그래프          |
    | scatter   | 산점도 그래프        |
    | hex bin   | 고밀도 산점도 그래프 |

  - ````python
    import pandas as pd
    df = pd.read_excel('./남북한발전전력량.xlsx')
    
    df_ns = df.iloc[[0,5],3:]
    df_ns.index = ['South','North'] # x축
    df_ns.columns = df_ns.columns.map(int)
    print(df_ns.head())
    
    df_ns.plot() # 선 그래프 그리기
    
    tdf_ns = df_ns.T # 전치 행렬
    print(tdf_ns.head())
    tdf_ns.plot() # 선 그래프 그리기
    
    tdf_ns.plot(kind='bar') # 막대 그래프 그리기
    
    tdf_ns.plot(kind='hist') # 히스토그램 그리기
    
    # 산점도
    import pandas as pd
    df = pd.read_csv('./auto-mpg.csv',header=None)
    df.columns = ['mpg','cylinders','displacement','horespower','weight','acceleration','model year','origin','name']
    
    df.plot(x='weight',y='mpg',kind='scatter') # 2개의 열을 선택하여 산점도 그리기
    
    df[['mpg','cylinders']].plot(kind='box') # 열을 선택하여 박스 플롯 그리기
    ````

  













