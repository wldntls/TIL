# 영화 리뷰 분류 : 이진 분류 예제

### 리뷰 50000개

### 훈련 데이터 25000개와 테스트 데이터 25000개

### 50%는 부정 , 50%는 긍정 리뷰



이진 분류 - binary

다중분류 - 

- categorical_crossentropy
  - 원핫 인코딩으로 된 것 써야함
- sparse_categorical_crossentropy 
  - 원핫 인코딩으로 안되어있어도 안에서 알아서 처리해줌



###  데이터 살펴보기

````python
from tensorflow import keras
import pandas as pd

keras.__version__
````

````python
# imdb 데이터셋 다운 받기 
# 단어 10000개만 다운
# 테스트 데이터와 트레인 데이터 나누기
from tensorflow.keras.datasets import imdb

(train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words = 10000)
````

````python
train_data

array([list([1, 14, 22, 16, 43, 530, 973, 1622, 1385, 65, 458, 4468, 66, 3941, 4, 173, 36, 256, 5, 25, 100, 43, 838, 112, 50, 670, 2, 9, 35, 480, 284, 5, 150, 4, 172, 112, 167, 2, 336, 385, 39, 4, 172, 4536, 1111, 17, 546, 38, 13, 447, 4, 192, 50, 16, 6, 147, 2025, 19, 14, 22, 4, 1920, 4613, 469, 4, 22, 71, 87, 12, 16, 43, 530, 38, 76, 15, 13, 1247, 4, 22, 17, 515, 17, 12, 16, 626, 18, 2, 5, 62, 386, 12, 8, 316, 8, 106, 5, 4, 2223, 5244, 16, 480, 66, 3785, 33, 4, 130, 12, 16, 38, 619, 5, 25, 124, 51, 36, 135, 48, 25, 1415, 33, 6, 22, 12, 215, 28, 77, 52, 5, 14, 407, 16, 82, 2, 8, 4, 107, 117, 5952, 15, 256, 4, 2, 7, 3766, 5, 723, 36, 71, 43, 530, 476, 26, 400, 317, 46, 7, 4, 2, 1029, 13, 104, 88, 4, 381, 15, 297, 98, 32, 2071, 56, 26, 141, 6, 194, 7486, 18, 4, 226, 22, 21, 134, 476, 26, 480, 5, 144, 30, 5535, 18, 51, 36, 28, 224, 92, 25, 104, 4, 226, 65, 16, 38, 1334, 88, 12, 16, 283, 5, 16, 4472, 113, 103, 32, 15, 16, 5345, 19, 178, 32]),
...
````

````python
train_labels

array([1, 0, 0, ..., 0, 1, 0])
````

````python
train_data.shape, train_labels.shape
((25000,), (25000,))

test_data.shape, test_labels.shape
((25000,), (25000,))
````

````python
pmovie_df.
(25000, 2)

movie_df.dtypes
train_data      object
train_labels    object
dtype: object
  
  movie_df.info()
````

````python
# 데이테프레임으로 변환
data = train_data, train_labels

df = pd.DataFrame(data, index = ['train_data','train_labels'])

movie_df = df.T
movie_df.head()
````

```python
# 첫번째 열 데이터 뽑는 방법 3가지

movie_df.iloc[:,0]

movie_df['train_data']

movie_df.loc[:]['train_data']
```

````python
# null 값 확인하기
movie_df.isnull().sum()
````

````python
max([max(sequence) for sequence in train_data])
9999
````

````python
len([max(sequence) for sequence in train_data])
25000
````

````python
# 리스트 풀기
for i in train_data[1]:
    print(i)
````

```python
# get_word_index() 함수는 인코딩된 인덱스를 딕셔너리 형태로 가져올 수 있음
word_index = imdb.get_word_index() # 인코딩된 인덱스를 가져올 수 있음
word_index
```

````python
# key, value 값 위치 변경
reverse_word_index = dict([(v,k) for k,v in word_index.items()])
reverse_word_index
````

````python
# key 값을 기준으로 내림차순 정렬
sorted(reverse_word_index.items())
````

````python
# 0은 패딩, 1은 문서 시작, 2는 사전에 없음을 위한 인덱스이므로 3을 뻅니다.
#get(x, 디폴트값) : 딕셔너리 안에 찾으려는 key값이 없을때, 미리 정해둔 디폴트 값을 가져오고 싶을때
decoded_review = ' '.join([reverse_word_index.get(i-3,'?') for i in train_data[17]])
decoded_review
````





### 데이터 준비하기

````python
import numpy as np

def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences),dimension)) # 0으로 바꾸기
    for i, sequence in enumerate(sequences): # sequences를 for문을 돌리기
        results[i, sequence] = 1. # 리스트 값들을 모두 1.(실수)으로 바꾸기?
    return results

x_train = vectorize_sequences(train_data).astype('float32') # 함수 사용, float 32로 변경
x_test = vectorize_sequences(test_data).astype('float32')
````

````python
# 레이블을 벡터로 변환
y_train = np.asarray(train_labels).astype('float32')
y_test = np.asarray(test_labels).astype('float32')
````





### 신경망 모델 만들기

```python
from tensorflow.keras import models
from tensorflow.keras import layers

# 모델 만들기 
model = models.Sequential()
model.add(layers.Dense(16,activation='relu',input_shape=(10000,)))
model.add(layers.Dense(16,activation='relu'))
model.add(layers.Dense(1,activation='sigmoid'))
```

````python
# 컴파일 방법 1
model.compile(optimizer='rmsprop',
             loss='binary_crossentropy',
             metrics = ['accuracy'])
````

```python
# 컴파일 방법 2
from tensorflow.keras import optimizers

model.compile(optimizer=optimizers.RMSprop(learning_rate=0.001),
             loss='binary_crossentropy',
             metrics = ['accuracy'])
```

```python
# 컴파일 방법 3
from tensorflow.keras import losses
from tensorflow.keras import metrics

model.compile(optimizer=optimizers.RMSprop(learning_rate=0.001),
             loss=losses.binary_crossentropy,
             metrics = [metrics.binary_accuracy])
```





### 훈련검증

````python
# 검증 세트 준비
x_val = x_train[:10000].astype(float)
partial_x_train = x_train[10000:].astype(float)

y_val = y_train[:10000].astype(float)
partial_y_train = y_train[10000:].astype(float)
````

````python
# 모델 훈련
history = model.fit(partial_x_train,
                   partial_y_train,
                   epochs=20,
                   batch_size=512,
                   validation_data=(x_val, y_val))
# validation_data는 학습하기 위한 용도는 아니며 loss와 model의 metrics(보통 accuracy)를 평가하기위해 사용된다.
````

````python
#
loss = history.history['loss']
val_loss = history.history['val_loss']
acc = history.history['binary_accuracy']
val_acc = history.history['val_binary_accuracy']
````





### 시각화

````python
import matplotlib.pyplot as plt

acc = history.history['binary_accuracy']
val_acc = history.history['val_binary_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc)+1)

# ‘bo’는 파란색 점을 의미합니다
plt.plot(epochs, loss, 'bo',label ='Training loss')
# ‘b’는 파란색 실선을 의미합니다
plt.plot(epochs, val_loss, 'b',label ='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()
````

````python
# 그래프 초기화
plt.clf() 

plt.plot(epochs, acc, 'bo', label ='Training acc')
plt.plot(epochs, val_acc, 'b', label = 'Validation acc')
plt.title('Training and validaiton accuracy')
plt.xlabel('Epochs')
plt.ylabel('accuracy')
plt.legend()

plt.show()
````

