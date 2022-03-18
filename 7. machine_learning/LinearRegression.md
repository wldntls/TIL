# 3-7. 지도학습_회귀



## 1. 회귀(LinearRegression)

- 회귀분석 

  - 의미

    - 데이터 값이 평균과 같은 일정한 값으로 돌아가려는 경향을 이용한 통계학 기법
    - 종속 변수(목표)와 하나 이상의 독립 변수(예측 변수라고도 함) 간의 미래 사건을 예측하는 방법
    - 연속적인 출력값을 예측
    - 예측 변수(또는 설명 변수)와 연속적인 반응 변수(또는 결과)가 주어졌을 때 출력 값을 예측하기 위해 두 변수 사이의 관계를 찾는 방법

  - 종속변수, 독립변수, 회귀계수

    - Y=W1X1 + W2X2 + W3X3 + ...+WnXn
    - Y : 종속변수
    - X1 + X2 + X3 .. + Xn : 독립변수
    - W1 + W2 + W3 + ... + Wn : 회귀계수

  - 종류

    | 독립변수 개수       | 회귀 계수의 결합     |
    | ------------------- | -------------------- |
    | 1개 : 단일 회귀     | 선형 : 선형 회귀     |
    | 여러 개 : 다중 회귀 | 비선형 : 비선형 회귀 |



## 2. 선형회귀(LinearRegression)

- 의미

  - 특성 x와 타깃 y가 주어지면 데이터 포인트와 직선 사이 거리가 최소가 되는 직선 -> 평균 제곱 거리 -> 데이터에서 학습한 직선의 기울기와 절편을 사용하여 새로운 데이터의 출력 값을 예측
  -  종속 변수 *y*와 한 개 이상의 독립 변수 (또는 설명 변수) *X*와의 선형 상관 관계를 모델링하는 회귀분석 기법

- Error 

  - 실제 데이터의 y값과 예측 직선모델의 y값의 차이

- Square Error 

  - 실제 데이터의 y값과 예측 직선 모델의 y값의 차이를 제곱해서 넓이로 보는 것

- Mean Square Error

  - Square Error를 다 더해서 n으로 나누어 평균낸 값
  - 이를 이용하여 best한 선형회귀모델 직선을 그는 것

- 목표 함수(object function) 또는 비용 함수(cost function)

  - 실제 값과 가설 값(예측 값)의 차이를 제곱해서 평균낸 개념을 이용해서 이를 최저로 만드는 함수

- 경사하강법

  - 정답이 주어진 데이터가 있을 때, 우리는 최적의 선형회귀모델(직선)을 만들고, 그 모델의 Mean Square Error 즉, cost function을 최소로 만드는 최적의 직선을 찾아야 한다.
  - 그  cost를 최소로 하는 직선을 구하는 과정을 train(학습)이라고 하고, train에 사용되는 알고리즘이 Gradient Descent 알고리즘이라 한다.

  

- 회귀의 평가지표
  - MAE
    - Mean Absolutea Errora이며 실제 값과 예측 값의 차이를 절댓값으로 변환해 평균한 값
  - MSE
    - Mean Squared Error이며 실제 값과 예측 값의 차이를 제곱해 평균한 값
  - MSLE
    - MSE에 로그를 적용한 것
    - 결정값이 클수록 오류값도 커지기 때문에 일부 큰 오류값들로 인해 전체 오류값이 커지는 것을 막아줌
  - RMSE
    - MSE 값은 오류의 제곱을 구하므로 실제 오류 평균보다 더 커지는 특성이 있으므로 MSE에 루트를 씌운 것이 RMSE(Root Mean Squared Error)
  - RMSLE
    - RMSE에 로그를 적용한 것
    - 결정값이 클수록 오류값도 커지기 때문에 일부 큰 오류값들로 인해 전체 오류값이 커지는 것을 말함
  - R(2)
    - 분산 기반으로 예측 성능을 평가
    - 실제 값의 분산 대비 예측 값의 분산 비율을 지표로 하며, 1에 가까울 수록 예측 정확도가 높음



## 3. 릿지(Ridge) or L2 

- 선형 회귀에 큰 회귀 계수 값의 예측 영향도를 감소시키기 위해 회귀 계수값을 더 작게 만드는 L2 규제 추가한 회귀 모델
- 중요하지 않은 피처의 영향을 감소



- 보스턴 주택가격

  ````python
  from sklearn.linear_model import Ridge
  from sklearn.model_selection import cross_val_score
  
  boston = load_boston()
  
  bostonDF = pd.DataFrame(boston.data, columns = boston.feature_names)
  
  bostonDF['PRICE'] = boston.target # price가 우리가 예측해야하는 값
  
  y_target = bostonDF['PRICE']
  X_data = bostonDF.drop(['PRICE'], axis = 1, inplace = False)
  
  ridge = Ridge(alpha=10)
  neg_mse_scores = cross_val_score(ridge, X_data, y_target, scoring="neg_mean_squared_error", cv=5)
  rmse_scores = np.sqrt(-1*neg_mse_scores)
  avg_rmse = np.mean(rmse_scores)
  
  print('5 fold의 개별 Negative MSE scores: ', np.round(neg_mse_scores, 3))
  print('5 fold의 개별 RMSE scores: ', np.round(rmse_scores, 3))
  print('5 fold의 개별 RMSE : {0:.3f} ', format(avg_rmse))
  
  5 fold의 개별 Negative MSE scores:  [-11.422 -24.294 -28.144 -74.599 -28.517]
  5 fold의 개별 RMSE scores:  [3.38  4.929 5.305 8.637 5.34 ]
  5 fold의 개별 RMSE : {0:.3f}  5.518166280868971
  ````

  ````python
  # alpha값을 0, 0.1, 1, 10, 100으로 변경하면서 RMSE 측정
  alphas = [0,0.1,1,10,100]
  
  for alpha in alphas:
      ridge = Ridge(alpha = alpha)
      
      neg_mse_scores = cross_val_score(ridge, X_data, y_target, scoring="neg_mean_squared_error", cv=5)
      avg_rmse = np.mean(np.sqrt(-1*neg_mse_scores))
      print('alpha {0} 일 때 5 folds의 평균 RMSE : {1:.3f}'.format(alpha,avg_rmse))
      
  alpha 0 일 때 5 folds의 평균 RMSE : 5.829
  alpha 0.1 일 때 5 folds의 평균 RMSE : 5.788
  alpha 1 일 때 5 folds의 평균 RMSE : 5.653
  alpha 10 일 때 5 folds의 평균 RMSE : 5.518
  alpha 100 일 때 5 folds의 평균 RMSE : 5.330
  ````

  ````python
  # 각 alpha에 따른 회귀 계수 값을 시각화하기 위해 5개의 열로 된 맷플롯립 축 생성
  fig, axs = plt.subplots(figsize=(18,6), nrows =1, ncols=5)
  
  coeff_df = pd.DataFrame()
  
  for pos, alpha in enumerate(alphas):
      ridge = Ridge(alpha=alpha)
      ridge.fit(X_data, y_target)
      
      coeff = pd.Series(data=ridge.coef_, index=X_data.columns)
      colname = 'alpha:' +str(alpha)
      coeff_df[colname] = coeff
      coeff = coeff.sort_values(ascending=False)
      axs[pos].set_title(colname)
      axs[pos].set_xlim(-3,6)
      sns.barplot(x=coeff.values, y=coeff.index, ax=axs[pos])
      
  plt.show()
  ````

  ```python
  # alpha 값에 따른 컬럼별 회귀계수 출력
  
  ridge_alphas = [0,0.1,1,10,100]
  sort_column = 'alpha:' +str(ridge_alphas[0])
  coeff_df.sort_values(by=sort_column, ascending=False)
  ```



## 4. 라쏘(Lasso) or L1

- 선형 회귀에 예측 영향력이 작은 피처의 회귀 계수를 0으로 만드는 L1 규제 추가한 회귀 모델
- 중요하지 않은 피처를 제거



- 보스턴 주택가격

  ````python
  from sklearn.linear_model import Lasso,ElasticNet
  
  def get_linear_reg_eval(model_name, params = None, X_data_n=None, y_target_n=None,
                         verbose=True, return_coeff=True):
      
      coeff_df = pd.DataFrame()
      if verbose : print('#######', model_name ,'#######')
      for param in params:
          if model_name == 'Ridge' : model = Ridge(alpha=param)
          elif model_name == 'Lasso': model = Lasso(alpha=param)
          elif model_name == 'ElasticNet': model = ElasticNet(alpha=param, l1_ratio=0.7)
          neg_mse_scores = cross_val_score(model, X_data_n, y_target_n, scoring="neg_mean_squared_error", cv=5)
          
          avg_rmse = np.mean(np.sqrt(-1*neg_mse_scores))
          print('alpha {0} 일 때 5 폴드 세트의 평균 RMSE : {1:.3f}'.format(param, avg_rmse))
          
          model.fit(X_data_n, y_target_n)
          if return_coeff:
              coeff = pd.Series(data=model.coef_, index= X_data_n.columns)
              colname = 'alpha:'+str(param)
              coeff_df[colname] = coeff
              
      return coeff_df
  ````

  ````python
  lasso_alphas = [0.07, 0.1, 0.5, 1, 3]
  coeff_lasso_df = get_linear_reg_eval('Lasso', params=lasso_alphas, X_data_n=X_data, y_target_n=y_target)
  
  ####### Lasso #######
  alpha 0.07 일 때 5 폴드 세트의 평균 RMSE : 5.612
  alpha 0.1 일 때 5 폴드 세트의 평균 RMSE : 5.615
  alpha 0.5 일 때 5 폴드 세트의 평균 RMSE : 5.669
  alpha 1 일 때 5 폴드 세트의 평균 RMSE : 5.776
  alpha 3 일 때 5 폴드 세트의 평균 RMSE : 6.189
  ````

  ````python
  sort_column = 'alpha:' +str(lasso_alphas[0])
  coeff_lasso_df.sort_values(by=sort_column, ascending=False)
  ````

  



## 5. 엘라스틱넷(ElasticNet)

- 선형 회귀에 L2, L1 규제를 추가한 회귀 모델
- 주로 피처가 많은 데이터 세트에 적용



- 보스턴 주택가격

  ````python
  # 위의 함수 사용
  
  elastic_alphas = [0.07, 0.1, 0.5, 1, 3]
  coeff_elastic_df = get_linear_reg_eval('ElasticNet', params=elastic_alphas, X_data_n=X_data, y_target_n=y_target)
  
  ####### ElasticNet #######
  alpha 0.07 일 때 5 폴드 세트의 평균 RMSE : 5.542
  alpha 0.1 일 때 5 폴드 세트의 평균 RMSE : 5.526
  alpha 0.5 일 때 5 폴드 세트의 평균 RMSE : 5.467
  alpha 1 일 때 5 폴드 세트의 평균 RMSE : 5.597
  alpha 3 일 때 5 폴드 세트의 평균 RMSE : 6.068
  ````

  ````python
  sort_column = 'alpha:' +str(elastic_alphas[0])
  coeff_elastic_df.sort_values(by=sort_column, ascending=False)
  ````

  



## 6. 보스턴 주택가격 회귀 구현



- 데이터 로드 및 살펴보기

  ````python
  import numpy as np
  import matplotlib.pyplot as plt
  import pandas as pd
  import seaborn as sns
  from scipy import stats
  from sklearn.datasets import load_boston
  
  boston = load_boston()
  
  bostonDF = pd.DataFrame(boston.data, columns = boston.feature_names)
  
  bostonDF['PRICE'] = boston.target # price가 우리가 예측해야하는 값
  
  print('Boston 데이타셋 크기 :', bostonDF.shape)
  bostonDF.head()
  
  bostonDF.info()
  bostonDF.describe()
  ````



- 상관관계 : 시각화

  ````python
  fig,axs = plt.subplots(figsize=(16,8), ncols=4, nrows=2)
  lm_features = ['RM','ZN','INDUS','NOX','AGE','PTRATIO','LSTAT','RAD']
  for i, feature in enumerate(lm_features):
      row = int(i/4) # row와 col로 위치를 잡음
      col = i%4
      sns.regplot(x=feature, y='PRICE', data = bostonDF, ax=axs[row][col])
  ````

  

- 모델 학습

  ````python
  from sklearn.model_selection import train_test_split
  from sklearn.linear_model import LinearRegression
  from sklearn.metrics import mean_squared_error, r2_score
  
  y_target = bostonDF['PRICE']
  X_data = bostonDF.drop(['PRICE'], axis = 1, inplace = False)
  
  X_train, X_test, y_train, y_test = train_test_split(X_data, y_target, test_size=0.3, random_state = 156)
  
  lr=LinearRegression()
  lr.fit(X_train, y_train)
  y_preds = lr.predict(X_test)
  
  mse = mean_squared_error(y_test, y_preds)
  rmse = np.sqrt(mse)
  
  # 이게 뭘 의미할까..?
  print('MSE : {0:.3f}, RMSE : {1:.3f}'.format(mse, rmse))
  print('Variance score: {0:.3f}'.format(r2_score(y_test, y_preds)))
  
  MSE : 17.297, RMSE : 4.159
  Variance score: 0.757
  ````

  ````python
  print('절편 값:',lr.intercept_) # 절편값이 저장
  print('회귀 계수값:', np.round(lr.coef_,1))
  
  절편 값: 40.995595172165
  회귀 계수값: [ -0.1   0.1   0.    3.  -19.8   3.4   0.   -1.7   0.4  -0.   -0.9   0.  -0.6]
  ````

  ````python
  coeff = pd.Series(data=np.round(lr.coef_, 1), index=X_data.columns)
  coeff.sort_values(ascending=False)
  
  RM          3.4
  CHAS        3.0
  RAD         0.4
  ZN          0.1
  INDUS       0.0
  AGE         0.0
  TAX        -0.0
  B           0.0
  CRIM       -0.1
  LSTAT      -0.6
  PTRATIO    -0.9
  DIS        -1.7
  NOX       -19.8
  dtype: float64
  ````

  ````python
  from sklearn.model_selection import cross_val_score
  
  y_target = bostonDF['PRICE']
  X_data = bostonDF.drop(['PRICE'],axis=1, inplace=False)
  lr = LinearRegression()
  
  neg_mse_scores = cross_val_score(lr, X_data, y_target, scoring="neg_mean_squared_error", cv=5)
  rmse_scores = np.sqrt(-1*neg_mse_scores)
  avg_rmse = np.mean(rmse_scores)
  
  print('5 fold의 개별 Negative MSE scores: ', np.round(neg_mse_scores, 2))
  print('5 fold의 개별 RMSE scores: ', np.round(rmse_scores, 2))
  print('5 fold의 개별 RMSE : {0:.3f} ', format(avg_rmse))
  ````

  



## 7. 시계열(Time series)

````python
import numpy as np
import pandas as pd
from fbprophet import Prophet

df = pd.read_csv('./avocado.csv')
df

df.info()
df.describe()
df.groupby('type').mean()
````

````python
df = df.loc[(df.type == 'conventional') & (df.region == 'TotalUS')]
df['Date'] = pd.to_datetime(df['Date']) # 날짜가 원래는 str이기 때문에 datetime으로 바꿔준 것
data = df[['Date', 'AveragePrice']].reset_index(drop=True)
data = data.rename(columns = {'Date':'ds', 'AveragePrice':'y'})
data.head()
````

````python
data.plot(x='ds', y='y', figsize=(16,8))
````

````python
model = Prophet()
model.fit(data)
future = model.make_future_dataframe(periods=365)
forecast = model.predict(future)
forecast.tail()
````

````python
fig1 = model.plot(forecast)
````

````python
fig2 = model.plot_components(forecast)
````

