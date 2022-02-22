# Mission(부모학력_자녀시험점수 관계)



## 1. 코드_1



- **데이터 살펴보기**

  ````
  import numpy as np
  import pandas as pd
  import seaborn as sns
  import matplotlib.pyplot as plt
  ````

  ````python
  df = pd.read_csv("./StudentsPerformance.csv")
  df
  ````

  ````python
  df.info()
  
  <class 'pandas.core.frame.DataFrame'>
  RangeIndex: 1000 entries, 0 to 999
  Data columns (total 8 columns):
   #   Column                       Non-Null Count  Dtype 
  ---  ------                       --------------  ----- 
   0   gender                       1000 non-null   object
   1   race/ethnicity               1000 non-null   object
   2   parental level of education  1000 non-null   object
   3   lunch                        1000 non-null   object
   4   test preparation course      1000 non-null   object
   5   math score                   1000 non-null   int64 
   6   reading score                1000 non-null   int64 
   7   writing score                1000 non-null   int64 
  dtypes: int64(3), object(5)
  memory usage: 62.6+ KB
  ````

  ````python
  df.describe()
  ````

  

- **데이터 시각화**

```python
# 수학 점수 현황
p = sns.countplot(x="math score", data = df, palette="muted")
_ = plt.setp(p.get_xticklabels(),rotation=90)
```

```python
# passmark를 40으로 하고 40 미만이면 F, 40 이상이면 P
passmark = 40

df['Math_PassStatus'] = np.where(df['math score'] < passmark,
                                 'F','P')
df.Math_PassStatus.value_counts()
```

````python
# 수학점수를 기준으로 남녀의 비율 시각화
p = sns.countplot(x = 'gender', data = df, hue = 'Math_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(),rotation=90)
````

````python
# 수학점수를 기준으로 그룹별 비율 시각화
p = sns.countplot(x = 'race/ethnicity', data = df, hue = 'Math_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(),rotation=90)
````

```python
# 수학점수를 기준으로 부모 학력별 비율 시각화
p = sns.countplot(x = 'parental level of education', data = df, hue = 'Math_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(),rotation=90)
```

```python
# 수학점수를 기준으로 점심식사 여부 비율 시각화

p = sns.countplot(x = 'lunch', data = df, hue = 'Math_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(),rotation=90)
```

````python
# 수학점수를 기준으로 시험 대비과목 이수여부 비율 시각화

p = sns.countplot(x = 'test preparation course', data = df, hue = 'Math_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(),rotation=90)
````

````python
# math와 reading 과목의 관계 시각화
p = sns.countplot(x = 'reading score', data = df, hue = 'Math_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(),rotation=90)
````

````python
# math와 writing 과목의 관계 시각화
p = sns.countplot(x = 'writing score', data = df, hue = 'Math_PassStatus', palette='bright')
_ = plt.setp(p.get_xticklabels(),rotation=90)
````

````python
# 각 학생별 성적 평균 구하기

score_df = df[['math score','reading score','writing score']].mean(axis=1)

# 평균값 데이터 프레임에 삽입하기
df['score_avg'] = score_df
df
````



- **데이터 전처리**

````python
from sklearn import preprocessing

def encode_features(df):
    features = ['gender','race/ethnicity','parental level of education', 'lunch', 'test preparation course']
    for feature in features:
        le = preprocessing.LabelEncoder()
        le = le.fit(df[feature])
        df[feature] = le.transform(df[feature])
    return df

df = encode_features(df)
df
````



- **데이터 분리 및 학습 **

````python
# 학습데이터와 테스트데이터 분리
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

y_target = df['score_avg']
#print(y_target)
X_data = df.drop(['math score','reading score','writing score', 'score_avg','Math_PassStatus'], axis=1, inplace=False)


X_train, X_test, y_train, y_test = train_test_split(X_data, y_target,test_size=0.3, random_state=156)

# LinearRegression 학습 예측 평가 수행
lr = LinearRegression()
lr.fit(X_train, y_train)
y_preds = lr.predict(X_test)
mse = mean_squared_error(y_test, y_preds)
rmse = np.sqrt(mse)

print('MSE : {0:.3f}, RMSE : {1:.3f}'.format(mse, rmse))
print('Variance score : {0:.3f}'.format(r2_score(y_test, y_preds)))

### 아직 정확히 이해하지 못함..
````

````python
print('절편 값: ', lr.intercept_)
print('회귀 계수값: ', np.round(lr.coef_,1))
````

````python
coeff = pd.Series(data = np.round(lr.coef_,1), index=X_data.columns)
print(coeff)

coeff.sort_values(ascending=False)
````



- **회귀**

````python
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.model_selection import cross_val_score

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
        print('alpha {0} 일 때 5 폴드 세트의 평균 RMSE : {1:}'.format(param, avg_rmse))
        
        model.fit(X_data_n, y_target_n)
        if return_coeff:
            coeff = pd.Series(data=model.coef_, index= X_data_n.columns)
            colname = 'alpha:'+str(param)
            coeff_df[colname] = coeff
            
    return coeff_df
````

````python
# 라쏘 회귀
lasso_alphas = [0, 0.1,0.7,1, 10]
coeff_lasso_df = get_linear_reg_eval('Lasso', params=lasso_alphas, X_data_n=X_data, y_target_n=y_target)

sort_column = 'alpha:' + str(lasso_alphas[0])
coeff_lasso_df.sort_values(by=sort_column, ascending=False)
````

````python
# 릿지 회귀
ridge_alphas = [0, 0.1,0.7,1, 10]
coeff_ridge_df = get_linear_reg_eval('Ridge', params=lasso_alphas, X_data_n=X_data, y_target_n=y_target)

sort_column = 'alpha:' + str(ridge_alphas[0])
coeff_ridge_df.sort_values(by=sort_column, ascending=False)
````

````python
# 엘라스틱넷
elastic_alphas = [0, 0.1,0.7,1, 10]
coeff_elastic_df = get_linear_reg_eval('ElasticNet', params=elastic_alphas, X_data_n=X_data, y_target_n=y_target)

sort_column = 'alpha:' + str(elastic_alphas[0])
coeff_elastic_df.sort_values(by=sort_column, ascending=False)
````





## 2. 코드_2



- **데이터 살펴보기**

  ````python
  import numpy as np
  import pandas as pd
  import seaborn as sns
  import matplotlib.pyplot as plt
  ````

  ````python
  df = pd.read_csv("./StudentsPerformance.csv")
  df
  ````

  ````python
  df.info()
  df.describe()
  df.corr()
  ````



- **데이터 시각화**

  ````python
  from wordcloud import WordCloud
  
  plt.subplots(figsize=(8,8))
  wordcloud=WordCloud(background_color='white',
                     width=512,
                     height=384).generate(' '.join(df))
  
  plt.imshow(wordcloud)
  plt.axis('off')
  plt.savefig('graph.png')
  plt.show()
  ````

  ````python
  sns.heatmap(df.corr(),
             annot=True) # 실제 값을 표시한다
  ````

  ````python
  sns.pairplot(df[['math score','reading score','writing score']], height=4)
  ````

  ````python
  def average_score(dt):
      return (dt['math score']+dt['reading score']+dt['writing score'])/3
  
  df['average score'] = df.apply(average_score, axis=1)
  df
  ````

  ````python
  sns.catplot(x='lunch', y='math score', hue='gender', kind='boxen',data=df, height=10, palette=sns.color_palette(['r','b']))
  
  sns.catplot(x='lunch', y='reading score', hue='gender', kind='boxen',data=df, height=10, palette=sns.color_palette(['r','b']))
  
  sns.catplot(x='lunch', y='writing score', hue='gender', kind='boxen',data=df, height=10, palette=sns.color_palette(['r','b']))
  ````

  ````python
  sns.catplot(x='lunch',y='average score', hue='gender',kind='boxen', data=df,
             height=10, palette = sns.color_palette(['red','blue']))
  
  plt.title('average')
  ````

  ````python
  sns.catplot(x='test preparation course',y='average score', hue='gender',kind='boxen', data=df,
             height=10, palette = sns.color_palette(['red','blue']))
  
  plt.title('average')
  ````

  ````python
  sns.catplot(x='parental level of education', y= 'average score', kind='boxen',data=df, height= 14)
  plt.title('average')
  plt.legend(loc='lower right')
  ````

  

​	

