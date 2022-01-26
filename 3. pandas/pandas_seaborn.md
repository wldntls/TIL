# pandas_Seaborn(고급 그래프 도구)



## 1. 데이터 셋 가져오기

- ````python
  import seaborn as sns #seaborn 라이브러리 불러오기 
  
  titanic = sns.load_dataset('titanic') # seaborn 라이브러리 안에 titanic 데이터 불러오기 
  
  print(titanic.head()) # titanic 데이터 처음 5개의 데이터 불러오기
  print('\n')
  print(titanic.info()) # titanic 데이터 마지막 5개의 데이터 불러오기
  ````



## 2. 회귀선이 있는 산점도

- ```python
  import matplotlib.pyplot as plt # matplotlib 라이브러리 불러오기
  import seaborn as sns # seaborn 라이브러리 불러오기
  
  titanic = sns.load_dataset('titanic')
  
  sns.set_style('darkgrid') # darkgrid 스타일 테마 불러오기 
  
  fig = plt.figure(figsize=(15,5)) 
  # 사이즈 재정리 figsize = (width, height), 그래프 객체 생성(figure에 2개의 서브 플롯 생성)
  ax1=fig.add_subplot(1,2,1) # 1행 2열 첫번째 칸은 ax1
  ax2=fig.add_subplot(1,2,2) # 1행 2열 두번째 칸은 ax2
  
  # 그래프 replot 불러와서 옵션 설정하기
  sns.regplot(x = 'age', # x축 변수
             y='fare', # y축 변수
             data = titanic, 
             ax=ax1) # 첫번째 칸 그래프
  
  sns.regplot(x='age',
             y='fare',
             data = titanic,
             ax=ax2, # 두번째 칸 그래프
             fit_reg=False) #회귀선 미표시 (기본값으로 원래 회귀선 설정되어 있음)
  
  plt.show()
  ```

  

## 3. 히스토그램/커널 밀도 그래프

- ```python
  import matplotlib.pyplot as plt
  import seaborn as sns
  
  titanic = sns.load_dataset('titanic')
  
  sns.set_style('darkgrid')
  
  fig = plt.figure(figsize=(15,5))
  ax1 = fig.add_subplot(1,3,1) # 1행 3열 첫번째 칸은 ax1
  ax2 = fig.add_subplot(1,3,2) # 1행 3열 두번째 칸은 ax2
  ax3 = fig.add_subplot(1,3,3) # 1행 3열 세번째 칸은 ax3
  
  sns.distplot(titanic['fare'],ax=ax1) # displot 함수는 히스토그램과 커널 밀도 그래프 같이 출력되는 것이 기본값
  
  sns.distplot(titanic['fare'], hist=False, ax=ax2) # 히스토그램 출력 안함
  
  sns.distplot(titanic['fare'], kde=False, ax=ax3) # 커널 밀도 그래프 출력 안함
  
  ax1.set_title('titanic fare - hist/ked')
  ax2.set_title('titanic fare - ked')
  ax3.set_title('titanic fare - hist')
  
  plt.show()
  ```



## 4. 히트맵

- ````python
  import matplotlib.pyplot as plt
  import seaborn as sns
  
  titanic = sns.load_dataset('titanic')
  
  table = titanic.pivot_table(index=['sex'], columns = ['class'], aggfunc='size') 
  # 피벗테이블로 범주형 변수 생성, 행은 'sex', 열은 'class', aggfunc='size'는 데이터 값의 크기를 기준으로 크기를 설정
  
  sns.heatmap(table,
             annot=True, fmt='d', # annot=True 숫자표시, 정수형 포맷
             cmap = 'YlGnBu', # 컬러 맵 설정
             linewidth=.5, # 구분 선 굵기
             cbar=False) # 컬러바 표시 X
  
  plt.show()
  ````



## 5. 범주형 데이터의 산점도

- ````python
  import matplotlib.pyplot as plt
  import seaborn as sns
  
  titanic = sns.load_dataset('titanic')
  
  sns.set_style('whitegrid')
  
  fig = plt.figure(figsize=(15,5))
  ax1 = fig.add_subplot(1,2,1)
  ax2 = fig.add_subplot(1,2,2)
  
  # 이산형 변수의 분표 - 데이터 분산을 고려하지 않음
  sns.stripplot(x="class", # x축 변수
               y="age", # y축 변수
               data=titanic, 
               ax=ax1)
  
  # 이산형 변수의 분표 - 데이터 분산을 고려하고 중복 없음
  sns.swarmplot(x="class", # x축 변수
              y="age", # y축 변수
              data = titanic,
              ax=ax2)
  
  ax1.set_title('Strip Plot')
  ax2.set_title('Strip Plot')
  
  plt.show()
  ````



## 6. 막대그래프

-  ```python
   import matplotlib.pyplot as plt
   import seaborn as sns
   
   titanic = sns.load_dataset('titanic')
   
   sns.set_style('whitegrid')
   
   fig = plt.figure(figsize = (15,5))
   ax1 = fig.add_subplot(1,3,1)
   ax2 = fig.add_subplot(1,3,2)
   ax3 = fig.add_subplot(1,3,3)
   
   sns.barplot(x='sex',y='survived',data=titanic, ax=ax1) # 막대그래프 코드, x,y 축 설정
   
   sns.barplot(x='sex',y='survived',hue='class',data=titanic, ax=ax2) #  hue 범례 제목 설정
   
   sns.barplot(x='sex',y='survived',hue = 'class', dodge=False, data=titanic,ax=ax3) 
   #barplot 기본 설정 누적그래프 아님 그래서 dodge=False 설정하면 누적그래프로 설정됨
   
   ax1.set_title('titanic survived - sex')
   ax2.set_title('titanic survived - sex/class')
   ax3.set_title('titanic survived - sex/class(stacked)')
   
   
   
   plt.show()
   ```



## 7. 빈도 그래프

- ````python
  import matplotlib.pyplot as plt
  import seaborn as sns
  
  titanic = sns.load_dataset('titanic')
  
  sns.set_style('whitegrid')
  
  fig = plt.figure(figsize = (15,5))
  ax1 = fig.add_subplot(1,3,1)
  ax2 = fig.add_subplot(1,3,2)
  ax3 = fig.add_subplot(1,3,3)
  
  # 빈도 그래프 코드 
  sns.countplot(x='class',palette='Set1',data=titanic,ax=ax1) # x축 설정, 색상 설정
  sns.countplot(x='class',hue= 'who', palette='Set2',data=titanic,ax=ax2) # hue 범례 제목 추가
  sns.countplot(x='class',hue= 'who', palette='Set3',dodge=False, data=titanic,ax=ax3)
  # 빈도 그래프는 기본으로 누적그래프가 아님, dodge=False를 통해 누적 그래프로 설정 가능
  
  ax1.set_title('titanic class')
  ax2.set_title('titanic class - who')
  ax3.set_title('titanic class - who(stacked)')
  
  
  plt.show()
  ````



## 8. 박스 플롯. 바이올린 그래프 

- ````python
  import matplotlib.pyplot as plt
  import seaborn as sns
  
  titanic = sns.load_dataset('titanic')
  
  sns.set_style('whitegrid')
  
  fig = plt.figure(figsize = (15,10))
  ax1 = fig.add_subplot(2,2,1) # 2행 2열 첫번째
  ax2 = fig.add_subplot(2,2,2) # 2행 2열 두번째
  ax3 = fig.add_subplot(2,2,3) # 2행 2열 세번째
  ax4 = fig.add_subplot(2,2,4) # 2행 2열 네번째
  
  sns.boxplot(x='alive', y='age', data=titanic, ax=ax1) # 박스플롯 코드
  
  sns.boxplot(x='alive',y='age', hue='sex', data=titanic,ax=ax2) # hue 변수 추가 - 범례 설정
  
  sns.violinplot(x='alive',y='age', data=titanic,ax=ax3) # 박스플롯 곡선 모양
  
  sns.violinplot(x='alive',y='age',hue='sex',data=titanic, ax=ax4) # hue 변수 추가 - 범례 설정
  
  plt.show()
  ````