# 뉴스 기사 분류: 다중 분류 문제

### 46개의 토픽

### 토픽은 훈련 세트에 최소한 10개의 샘플

## 로이터 데이터셋



### 데이터 살펴보기

````python
from tensorflow.keras.datasets import reuters

(train_data, train_labels), (test_data, test_labels) = reuters.load_data(num_words=10000)
````

````python
train_data
array([list([1, 2, 2, 8, 43, 10, 447, 5, 25, 207, 270, 5, 3095, 111, 16, 369, 186, 90, 67, 7, 89, 5, 19, 102, 6, 19, 124, 15, 90, 67, 84, 22, 482, 26, 7, 48, 4, 49, 8, 864, 39, 209, 154, 6, 151, 6, 83, 11, 15, 22, 155, 11, 15, 7, 48, 9, 4579, 1005, 504, 6, 258, 6, 272, 11, 15, 22, 134, 44, 11, 15, 16, 8, 197, 1245, 90, 67, 52, 29, 209, 30, 32, 132, 6, 109, 15, 17, 12]),
````

````python
train_labels
array([ 3,  4,  3, ..., 25,  3, 25])
````

````python
train_data.shape, train_labels.shape
((8982,), (8982,))

test_data.shape, test_labels.shape
((2246,), (2246,))
````

````python
type(train_data)
numpy.ndarray
````

````python
# 데이터 프레임으로 변환
import pandas as pd

data = train_data, train_labels
df = pd.DataFrame(data, index = ['train_data','train_labels'])

news_df = df.T
news_df
````

````python
news_df.shape
(8982, 2)

news_df.dtypes
train_data      object
train_labels    object
dtype: object

news_df.info()
````

````python
# null 값 확인
news_df.isnull().sum()
````

````python
max([max(sequence) for sequence in train_data])
````

```python
# get_word_index() 함수는 인코딩된 인덱스를 딕셔너리 형태로 가져올 수 있음
word_index = reuters.get_word_index() # 인코딩된 인덱스를 가져올 수 있음
word_index
```

````python
# key, value 값 위치 변경
reverse_word_index = dict([(v,k) for k,v in word_index.items()])
reverse_word_index
````

````python
# 0은 패딩, 1은 문서 시작, 2는 사전에 없음을 위한 인덱스이므로 3을 뻅니다.
#get(x, 디폴트값) : 딕셔너리 안에 찾으려는 key값이 없을때, 미리 정해둔 디폴트 값을 가져오고 싶을때
decoded_review = ' '.join([reverse_word_index.get(i-3,'?') for i in train_data[0]])
decoded_review
````



### 데이터 준비

````python
import numpy as np

def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences),dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results

x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)
````

````python
# labels encoding 1
# labels도 원-핫 인코딩 해줘야함
def to_one_hot(sequences, dimension=46): # 토픽타입이 46개이기 때문에 46으로 맞춰줌
    results = np.zeros((len(sequences),dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results

one_hot_train_labels = to_one_hot(train_labels)
one_hot_test_labels = to_one_hot(test_labels)
````

````python
# labels encoding 2

from keras.utils.np_utils import to_categorical

one_hot_train_labels=to_categorical(train_labels)
one_hot_test_labels=to_categorical(test_labels)
````



### 신경망 모델 만들기

````python
from tensorflow.keras import models
from tensorflow.keras import layers

model = models.Sequential()
model.add(layers.Dense(6,activation='relu',input_shape=(10000,)))
model.add(layers.Dense(64,activation='relu'))
model.add(layers.Dense(46,activation='softmax')) # 다중 분류 함수
````



### 훈련 검증 1: categorical_crossentropy

````python
model.compile(optimizer='rmsprop',
             loss='categorical_crossentropy',
             metrics = ['accuracy'])
````

````python
x_val = x_train[:1000].astype(float) # 주의 : 1000으로 설정
partial_x_train = x_train[1000:].astype(float)

y_val = y_train[:1000].astype(float)
partial_y_train = y_train[1000:].astype(float)
````

````python
history = model.fit(partial_x_train,
                   partial_y_train,
                   epochs=20,
                   batch_size= 512,
                   validation_data=(x_val, y_val))
````



### 훈련 검증 2 : sparse_categorocal_crossentropy

````python
model.compile(optimizer='rmsprop',
             loss='sparse_categorical_crossentropy',
             metrics = ['accuracy'])
````

````python
x_val = x_train[:1000].astype(float) # 주의 : 1000으로 설정
partial_x_train = x_train[1000:].astype(float)

y_val = y_train[:1000].astype(float)
partial_y_train = y_train[1000:].astype(float)
````

````python
history = model.fit(partial_x_train,
                   partial_y_train,
                   epochs=20,
                   batch_size= 512,
                   validation_data=(x_val, y_val))
````



### 시각화

````python
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(loss) + 1)

plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

plt.show()
````

````python
plt.clf()   # 그래프를 초기화합니다

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

plt.plot(epochs, acc, 'bo', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()
````

````python
# fix model

model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(10000,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(46, activation='softmax'))

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(partial_x_train,
          partial_y_train,
          epochs=9,
          batch_size=512,
          validation_data=(x_val, y_val))
results = model.evaluate(x_test, one_hot_test_labels)
````



### 훈련된 모델로 새로운 데이터 예측

````python
predictions = model.predict(x_test) # 각 토픽의 확률이 %로 나옴
predictions
````

````python
# 0번째 기사는 3번 인덱스가 확률이 높아서 3번을 뽑아주는 것임, 3번 토픽일 확률이 높다는 것
np.argmax(predictions[0])

3
````

````python
np.sum(predictions[0])

1.0000001
````







