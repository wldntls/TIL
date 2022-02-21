

# 3-6. 지도학습_Ensemble-protected



## 1. 앙상블 유형

- 보팅(Voting)
  - 하드보팅
  - 소프트보팅
- 배깅(Bagging)
  - 랜덤 포레스트(Random Forest)
- 부스팅(boosting)
  - 에이다 부스팅(AdaBoost)
  - 그래이던트 부스팅(Gradient Booting Machine(GBM))
  - XGBoost
  - LightBGM
- 스태킹(Stacking)



## 2. 앙상블 특징

- 단일 모델의 약점을 다수의 모델을 결합하여 보완함
- 뛰어난 성능들만 구성하는 것만이 좋은 것은 아니다.
- 랜덤포레스트, 뛰어난 부스팅 알고리즘들은 모두 결정 트리 알고리즘을 기반으로 함
- 결정트리의 과적합 문제를 다수의 분류기를 결합해서 보완, 직관적인 분류기준은 강화



## 3. 보팅(Voting)과 배깅(Bagging)의 차이

- 보팅(Voting)

  - 서로 다른 알고리즘
  - 하나의 데이터 셋

  

  <img src="Desktop/스크린샷 2022-02-21 22.04.44.png" alt="스크린샷 2022-02-21 22.04.44" style="zoom: 33%;" />

  - 서로 다른 알고리즘

  - 하나의 데이터 셋

  - 유형

    - 하드보팅

      - 예측한 결괏값들 중 다수의 분류기가 결정한 예측값을 최종 보팅 결괏값으로 선정, "다수결의 원칙"

        <img src="Desktop/스크린샷 2022-02-21 22.09.15.png" alt="스크린샷 2022-02-21 22.09.15" style="zoom: 33%;" />

    - 소프트보팅

      - 분류기들의 레이블 값 결정 확률을 모두 더하고 이를 평균해서 이들 중 확률이 가장 높은 레이블 값을 최종 보팅 결괏값으로 선정

      - 하드보팅보다 소프트보팅이 예측 성능이 좋음

        <img src="Desktop/스크린샷 2022-02-21 22.07.49.png" alt="스크린샷 2022-02-21 22.07.49" style="zoom:33%;" />

      

- 배깅(Bagging)

  - 하나의 알고리즘
  - 샘플링 데이터셋(표본수는 다름)

  <img src="Desktop/스크린샷 2022-02-21 22.06.26.png" alt="스크린샷 2022-02-21 22.06.26" style="zoom:33%;" />

  



## 4. 보팅 실습

- ```python
  import pandas as pd
  
  from sklearn.ensemble import VotingClassifier
  from sklearn.linear_model import LogisticRegression
  from sklearn.neighbors import KNeighborsClassifier
  from sklearn.datasets import load_breast_cancer
  from sklearn.model_selection import train_test_split
  from sklearn.metrics import accuracy_score
  import warnings
  
  cancer = load_breast_cancer()
  
  data_df = pd.DataFrame(cancer.data, columns =cancer.feature_names)
  data_df.head(3)
  ```

- ````python
  # 개별 모델 로지스틱 회귀, KNN
  lr_clf = LogisticRegression()
  knn_clf = KNeighborsClassifier(n_neighbors = 8)
  
  # 소프트 보팅 기반의 앙상블 모델로 구현한 분류기
  vo_clf = VotingClassifier(estimators =[('LR',lr_clf),('KNN',knn_clf)], voting='soft')
  
  X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target,
                                                     test_size=0.2, random_state=156)
  
  # VotingClassifier
  vo_clf.fit(X_train, y_train) # 학습
  pred = vo_clf.predict(X_test) # 예측
  print('Voting 분류기 정확도 : {0:.4f}'.format(accuracy_score(y_test, pred))) # 정확도 평가
  
  # 개별모델의 학습/예측/평가
  classifiers = [lr_clf, knn_clf] 
  for classifier in classifiers:
      classifier.fit(X_train, y_train) # 학습
      pred = classifier.predict(X_test) # 예측
      class_name = classifier.__class__.__name__ # 클래스 명 추출
      print('{0} 정확도 : {1:.4f}'.format(class_name, accuracy_score(y_test,pred)))
  ````

- ````
  Voting 분류기 정확도 : 0.9474
  LogisticRegression 정확도 : 0.9386
  KNeighborsClassifier 정확도 : 0.9386
  ````



## 5. 배깅 - 랜덤 포레스트

- 부트스트래핑 분할 : 샘플링하는 방식
  - 데이터가 섞일 수 있음

- <img src="Desktop/스크린샷 2022-02-21 23.44.15.png" alt="스크린샷 2022-02-21 23.44.15" style="zoom:33%;" />

- RandomFrestClassifier 하이퍼 파라미터
  - max_depth 
  - max_features : 결정 트리 갯수 결정
  - n_estimators 
  - max_samples_leaf

- 실습

  - ````python
    import pandas as pd
    import matplotlib.pyplot as plt
    
    # features.txt 파일에는 피처 이름 index와 피처명이 공백으로 분리되어 있음. 이를 dataframe으로 로드.
    feature_name_df = pd.read_csv('./human_activity/features.txt', sep='\s+',
                                 header= None, names=['column_index','column_name'])
    
    # 피처명 index를 제거하고, 피처명만 리스트 객체로 생성한 뒤 샘플로 10개만 추출
    feature_name = feature_name_df.iloc[:, 1].values.tolist()
    print('전체 피처명에서 10개만 추출:', feature_name[:10])
    ````

  - ````python
    # 중복된 피처명을 수정하기 위한 함수  
    def get_new_feature_name_df(old_feature_name_df):
        feature_dup_df = pd.DataFrame(data=old_feature_name_df.groupby('column_name').cumcount(),
                                     columns=['dup_cnt'])
        feature_dup_df = feature_dup_df.reset_index()
        new_feature_name_df = pd.merge(old_feature_name_df.reset_index(),feature_dup_df, how='outer')
        new_feature_name_df['column_name'] = new_feature_name_df[['column_name','dup_cnt']].apply(lambda 																		x: x[0]+'_'+str(x[1]) if x[1]>0 else x[0], axis=1)
        
        # 크면 그 값을 넣어주고, 아니면 원래 값을 출력
        new_feature_name_df = new_feature_name_df.drop(['index'],axis=1)
        return new_feature_name_df
    ````

  - ````python
    def get_human_dataset():
        feature_name_df = pd.read_csv('./human_activity/features.txt', sep='\s+',
                                 header= None, names=['column_index','column_name'])
        
        # 신규 피처명 DataFrame 생성.
        new_feature_name_df = get_new_feature_name_df(feature_name_df)
        # DataFrame에 피처명을 컬럼으로 부여하기 위해 리스트 객체로 다시 변환
        feature_name = new_feature_name_df.iloc[:, 1].values.tolist()
        
        # 학습 피처 데이터 셋과 테스트 피처 데이터 DataFrame으로 로딩, 컬럼명은 feature_name 적용
        X_train = pd.read_csv('./human_activity/train/X_train.txt', sep='\s+',names = feature_name)
        X_test = pd.read_csv('./human_activity/test/X_test.txt', sep='\s+', names = feature_name)
    
        # 학습 레이블과 테스트 레이블 데이터를 DataFrame으로 로딩, 컬럼명은 action 부여
        y_train = pd.read_csv('./human_activity/train/y_train.txt', sep='\s+',header=None, names = 																																													['action'])
        y_test = pd.read_csv('./human_activity/test/y_test.txt', sep='\s+',header=None, names = 																																														['action'])
        
        return X_train, X_test, y_train, y_test
    ````

  - ````python
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import accuracy_score
    import pandas as pd
    import warnings 
    warnings.filterwarnings('ignore') # 경고 메시지 무시하기
    
    X_train, X_test, y_train, y_test = get_human_dataset()
    
    # 랜덤 포레스트 학습 및 별도의 테스트 셋을 예측 성능 평가
    rf_clf = RandomForestClassifier(random_state=0)
    rf_clf.fit(X_train, y_train)
    pred = rf_clf.predict(X_test)
    accuracy = accuracy_score(y_test, pred)
    
    print('랜덤 포레스트 정확도 : {0:.4f}'.format(accuracy))
    랜덤 포레스트 정확도 : 0.9253
    ````

  - ````python
    # 최적의 하이퍼 파라미터와 예측 정확도를 찾기 위해 하이퍼 파리미터를 계속 바꿔가면서 돌렸음
    from sklearn.model_selection import GridSearchCV
    
    params = {
        'n_estimators':[159], # 300으로 두었을때, 예측 정확도 오히려 떨어짐-> 많이 한다고 좋은 결과가 나오는 것은 아님
        'max_depth':[6,8,10,12],
        'min_samples_leaf':[8,9,10,12,18],
        'min_samples_split':[1,2,3,4,5,6,7,8,16,20]
    }
    
    rf_clf = RandomForestClassifier(random_state = 0, n_jobs=-1) # n_jobs = -1 : cpu를 모두 사용하겠다,
    grid_cv = GridSearchCV(rf_clf, param_grid=params, cv=2, n_jobs=-1)
    grid_cv.fit(X_train, y_train)
    
    print('최적의 하이퍼 파라미터:/n',grid_cv.best_params_)
    print('최고 예측 정확도 : {0:.4f}'.format(grid_cv.best_score_))
    ````

  - ````python
    # 상위 20위의 데이터 시각화
    import matplotlib.pyplot as plt
    import seaborn as sns
    
    ftr_importances_values = rf_clf1.feature_importances_
    ftr_importances = pd.Series(ftr_importances_values, index=X_train.columns)
    ftr_top20 = ftr_importances.sort_values(ascending=False)[:20]
    
    plt.figure(figsize=(8,6))
    plt.title('Feature importances Top 20')
    sns.barplot(x=ftr_top20, y = ftr_top20.index)
    plt.show()
    ````

    - `cumcount()`

      - ````python
        import pandas as pd
        
        df = pd.DataFrame([['a'],['a'],['a'],['b'],['b'],['a']],
                         columns=['A'])
                         
        df.groupby('A').cumcount() # 몇번째 중복되는 것인지 알려줌 ex) 첫번째 a는 1, 두번째 a는 2 세번째 a는 3 이렇게
        ````

      - ````python
        0    0 # 첫번째 중복
        1    1 # 두번째 중복
        2    2 # 세번째 중복
        3    0
        4    1
        5    3 # 네번째 중복
        dtype: int64
        ````

    - `merge()`

      - ````python
        # join test
        
        import pandas as pd
        
        data_A = {'key':[1,2,3], 'name':['Jane','John','Peter']}
        dataframe_A = pd.DataFrame(data_A, columns = ['key','name'])
        
        data_B = {'key':[2,3,4], 'age':[18,15,20]}
        dataframe_B = pd.DataFrame(data_B, columns = ['key','age'])
        
        print(dataframe_A)
           key   name
        0    1   Jane
        1    2   John
        2    3  Peter
        
        print(dataframe_B)
           key  age
        0    2   18
        1    3   15
        2    4   20
        ````

      - ````python
        df_INNER_JOIN = pd.merge(dataframe_A, dataframe_B, left_on = 'key',right_on = 'key', how= 'inner')
        print(df_INNER_JOIN) # 데이터 프레임끼리 뭉치는 것, dataframe_A,B 둘다 key가 기준, inner가 default, 겹치는 것만 출력
        
           key   name  age
        0    2   John   18
        1    3  Peter   15
        ````

      - ````python
        df_OUTER_JOIN = pd.merge(dataframe_A, dataframe_B, left_on = 'key',right_on = 'key', how= 'outer')
        print(df_OUTER_JOIN) # outer join 다 뭉치는 것 , 빈값은 nan으로 표현됨, 겹치는 것 포함, 하나의 데이터 프레임에만 있는 것도 출력
        
           key   name   age
        0    1   Jane   NaN
        1    2   John  18.0
        2    3  Peter  15.0
        3    4    NaN  20.0
        ````

      - ````python
        df_LEET_JOIN = pd.merge(dataframe_A, dataframe_B, left_on = 'key',right_on = 'key', how= 'left')
        print(df_LEET_JOIN) # key값을 왼쪽을 기준으로 해서 왼쪽(dataframe_A)은 다 나오고 왼쪽에 없는 것은 다 날리고, 값이 없는 것은 nan
        
           key   name   age
        0    1   Jane   NaN
        1    2   John  18.0
        2    3  Peter  15.0
        ````

      - ````python
        df_RIGHT_JOIN = pd.merge(dataframe_A, dataframe_B, left_on = 'key',right_on = 'key', how= 'right')
        print(df_RIGHT_JOIN) # key값을 오른쪽을 기준으로 해서 오른쪽(dataframe_B)은 다나오고 오른쪽에 없는 것은 다 날리고, 값이 없는 것은 nan
        
           key   name  age
        0    2   John   18
        1    3  Peter   15
        2    4    NaN   20
        ````



## 6. 부스팅(Boosting)

- 에이다 부스팅(Ada Boosting)
  - 약한 분류기들이 상호보완 하도록 순차적으로 학습하고, 이들을 조합하여 최종적으로 강한 분류기의 성능을 향상시키는 것
- 그래이던트 부스팅(Gradient Boosting)
- 



