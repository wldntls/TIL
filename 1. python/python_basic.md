# 1-2 파이썬 기초_ 자료형



## (1) 숫자형 

- 종류

  - 정수, 실수, 8진수, 16진수

- 산술 연산자

- 비교 연산자

- 논리 연산자

  - and : 좌항과 우항이 모두 True일 경우 True
  - or : 좌항과 우항 중 하나라도 True일 경우 True
  - not : True는 False로 Fales는 True로 반전

  

## (2) 문자열

- 이스케이프 코드 
  - `\n` : 문자열 안에서 줄을 바꿀 때 사용
  - `\t` : 문자열 사이에 탭 간격을 줄 때 사용
  - `\\` : 문자 \를 그대로 표현할 때 사용
  -  `\'` : 작은 따옴표를 그대로 표현할 때 사용
  - `\"` : 큰따옴표를 그대로 표현할 때 사용
  - `\r` : 캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
  - `\f` : 폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
  - `\a` : 벨 소리(출력할 때 PC 스피커에서 '삑'소리가 난다)
  - `\b` : 백 스페이스
  - `\000` : 널 문자
  
- 문자열 길이 
  - `len()`
  
- 문자열의 요소는 바꿀 수 없음. 하지만 슬라이싱을 이용해서 바꿀 수 있음

- 문자열 포매팅
  - `%`
    - `%s` - 문자열
    - `%c` - 문자 1개
    - `%d` - 정수
    - `%f` - 부동소수
    - `%o` - 8진수
    - `%x` - 16진수
    - `%%` - Literl %(문자%자체)
  
  - `"".format()`
  
    - 소수점 표현하기
  
      - ````python
        y = 3.42134234
        "{0:0.4f}".format(y)
        결과
        '3.4213'
        ````
  
      - ````python
        "{0:10.4f}".format(y)
        결과
        '    3.4213'
        ````
  
    - 정렬과 공백
      - `"%10s" % "hi"` : hi가 끝에 오게함
    - 소수점 표현하기
      - `"%0.4f" % 3.42134234` : `'3.4213'` -> 0은 자리수, 4는 소수점 뒤에 자르는 숫자
    - 왼쪽 정렬
      - `"{0:<10}".format("hi")`
    - 오른쪽 정렬
      - `"{0:>10}".format("hi")`
    - 가운데 정렬
      - `"{0:^10}".format("hi")`
    - 공백 채우기
      - `"{0:=^10}".format("hi")`
  
  - `f""`
  
    - 정렬과 공백
  
      - `"%10s" % "hi"` : hi가 끝에 오게함
  
    - 소수점 표현하기
  
      - ```python
        y = 3.42134234
        f'{y:0.4f}'
        결과 
        '3.4213'
        
        f'{y:10.4f}'
        결과
        '    3.4213'
        ```
  
    - 왼쪽 정렬
  
      - `f'{"hi":<10}'`
  
    - 오른쪽 정렬
  
      - `f'{"hi":>10}'`
  
    - 가운데 정렬
  
      - `f'{"hi":^10}'`
  
    - 공백 채우기
  
      - `f'{"hi":=^10}'`
  
- 문자열 관련 함수들
  - 문자 개수 세기 : `count()`
  - 위치 알려주기 
    - `find()` -> 인덱스 위치 출력해줌, 찾는 문자가 없으면 -1 또는 None 값이라고 출력
    - `index()` -> 인덱스 위치 출력해줌, 찾는 문자가 없으면 에러를 출력
  - 문자열 삽입 : `join()`
  - 소문자를 대문자로 : `upper()`
  - 대문자를 소문자로 : `lower()`
  - 왼쪽 공백 지우기 : `lstrip()`
  - 오른쪽 공백 지우기 : `rstrip()`
  - 양쪽 공백 지우기 : `strip()`
  - 문자열 바꾸기 : `replace("기존 문자", "바꿀 문자")`
  - 문자열 나누기 : `split("구분할 문자")`



## (3) 리스트 자료형 

> 값을 바꿀 수 있음
>
> 딕셔너리 key 값으로 불가능

- 리스트에 요소 추가: `append()` -> 리스트 자체로 추가
- 리스트 오름차순 정렬 : `sort()`
- 리스트 뒤집기 :`reverse()`
- 리스트 요소에 삽입 : `insert(위치, 삽입할 요소)`
- 리스트 요소 제거 : `remove()`
- 리스트 요소 끄집어내기 : `pop()` -> 공백으로 두면 제일 위, 숫자를 넣으면 넣은 숫자 위치에 있는 요소 끄집어냄
- 리스트 확장 : `extend()` -> 리스트의 요소로 추가



## (4) 튜플 자료형

> 값 자체를 바꿀 수 없음, 삭제 불가
>
> 딕셔너리 key 값으로 가능





## (5) 딕셔너리 자료형

- 딕셔너리 구조 
  - `{Key1:Value1,Key2:Value,...}`

- 딕셔너리 만들 때 주의 사항
  - 중복 허용 x -> 하나만 처리 
  - list는 변경 가능하기 때문에 Error 발생 
  - Tuple은 변경 불가하기 때문에 Key 값으로 가능 
- Key 리스트 만들기
  - `a.keys()` -> key 값 리스트 형태로 출력됨
  - `for k in a.keys(): pritn(k)` -> 키값 줄바꿈 형태로 출력
- values 리스트 만들기
  - `a.values()`
- Key, value 쌍 얻기
  - `a.item()`
- Key, value 쌍 모두 지우기
  - `a.clear()`
- key로 value 얻기
  - `a.get(키값)` -> 없는 키값을 넣으면 None이 출력됨
- `'name' in a` -> a 딕셔너리에 name이 있으면 True 없으며 False



## (6) 집합 자료형

> set 자료형

- 특징
  - 중복을 허용하지 않음
  - 순서가 없음
- 교집합(and)
  - &
  - `s1.intersection(s2)`
- 합집합(or)
  - |
  - `s1.union(s2)`
- 차집합
  - -
  - `s1.difference(s2)`
- 값 추가 하기
  - `add()` -> 1개 추가
  - `updata()` -> 여러개 추가



## (7) 불 자료형

> True / False

- 값이 있으면 True
- 값이 없으면 False
  

## (8) 변수 구조

- 변수 이름 = 변수에 저장할 값



---



# 1-3. 파이썬 기초_흐름제어



### 1. if문

- ````python
  money = True
  if money:
    print("택시를 타고 가라")
  else:
    print("걸어 가라")
  ...
  택시를 타고 가라
  ````

- ````python
  pocket = ['paper','cellphon']
  card = True
  if 'money' in pocket:
    print("택시를 타고 가라")
  elif card:
    print("택시를 타고 가라")
  else:
    print("걸어가라")
  ...
  택시를 타고 가라
  ````

  



### 2. for 문

- ```python
  for x in a: print(x, end="")
   # end="" 는 가로로 찍히게 해줌. 없으면 한글자씩 세로로 찍힘
  ```

- ````python
  a={'apple':3,'banana':5,'mango':7}
  for x in a:
  	print(x)
  ...
  apple
  banana
  mango
  # for문에서 딕셔너리 값을 담은 변수를 출력하면 key값만 출력됨
  ````

- `continue`

  - 조건문에 일치하면 다시 for문으로 돌아감. 
  - 만약 충족하지 못하면 다음으로 넘어감.

  

### 3. while 문

- `break`
  - 조건이 성립하면 강제로 while 문을 빠져나가게 함



### 4. random

- import random 써줘야함

- 0~1 미만의 실수를 난수로 생성

  - ```python
    for x in range(5):
      print(random.random())
    ```

- 특정 범위의 실수를 난수로 생성

  - ````python
    for x in range(5):
      print(random.uniform(1,100))
    ````

- 특정 범위의 정수를 난수로 생성

  - ```python
    for x in range(5):
      print(random.randint(1,100))
    ```

- 0~1 미만의 실수를 난수로 생성

  - ```python
    for x in range(5):
      print(random.randrange(1,100,10))
    ```



----



# 1-4. 파이썬 기초_함수(입출력 파일처리)



## 1. 함수

- 함수의 구조

  - ````python
    def 함수명(매개변수):
      <수행할 문장>
      <수행할 문장>
    ````



- 일반적인 함수

  - ````python
    def add(a,b):
      result = a+b
      return reuslt
    
    a = add(3,4)
    print(a)
    ````



- 입력값이 없는 함수

  - ````python
    def say():
      return 'Hi'
    
    a = say()
    print(a)
    ````



- 결괏값이 없는 함수

  - ````python
    def add(a,b):
      print("%d, %d의 합은 %d입니다." % (a,b,a+b))
      
    add(3,4)
    ````



- 입력값/결괏값이 없는 함수

  - ````python
    def say():
      print('Hi')
      
    say()
    ````



- 입력값이 몇 개가 될지 모를 때

  - ````python
    def add_many(*args):
      result = 0
      for i in args:
        result = reuslt + i
       return result 
    # * : 매개변수를 튜플로 만듦, args : arguments의 약자, 관례상으로 씀
    
    reuslt = add_many(1,2,3)
    print(reuslt)
    ````



- 키워드 파라미터 kwargs

  - ````python
    # **를 붙이면 딕셔너리가 되고 모든 key=value형태로 결괏값에 저장됨
    #kwargs : keyword arguments의 약자
    def print_kwargs(**kwargs): 
      print(kwargs)
      
    print_kwargs(a=1)
    {'a':1}
    print_kwargs(name:'foo',age=3)
    {'age':3,'name':'foo'}
    ````



- return의 또 다른 쓰임새

  - ````python
    def say_nick(nick):
      if nick == "바보":
        return
      print("나의 별명은 %s 입니다"%nick)
      
    say_nick('야호')
    나의 별명은 야호입니다. 
    say_nick('바보')
    결괏값 없음
    ````



- 매개변수에 초기값 미리 설정하기

  - ````python
    def say_myself(name,old,man=True): # 초기값 설정 가능, 생략 가능 -> man으로 자동 출력
      print("나의 이름은 %s 입니다."%name)
      print("나이는 %d살 입니다."% old)
      if man:
        print("남자입니다.")
       else:
        print("여자입니다.")
        
    say_myself("박응용",27)
    say_myself("박응용",27,True) # False로 설정하면 '여자입니다.' 출력
    나의 이름은 박응용입니다.
    나이는 27살 입니다. 
    남자입니다.
    ````



- 함수 안에서 선언한 변수의 효력 범위는 함수 안에 있는 변수만 해당, 함수 밖에 있는 변수는 해당 x

- 함수 안에서 함수 밖의 변수를 가져와서 사용하기 위한 방법

  - Return  사용하기

    - ````python
      a = 1
      def vartest(a):
        a = a+1
        return a
      
      a = vartest(a)
      print(a)
      ````

- Global 명령어 사용하기

  - ````python
    a = 1
    def vartest(a):
      global a
      a = a + 1
    
    vartest()
    print(a)
    ````



- lambda 

  - lambda 매개변수1, 매개변수2, ..: 매개변수를 이용한 표현식

    - ````python
      add = lambda a,b : a+b
      result = add(3,4)
      print(reuslt)
      ````



## 2. 파일 읽고 쓰기

- 파일 생성하기

  - ````python
    f = open("새파일.txt",'w')
    f.close()
    ````

  - r : 읽기 모드, w : 쓰기 모드, a : 추가 모드

- 파일 쓰기 모드로 열어 출력 값 적기

  - ````python
    f = opent("현재 파일 위치/파일 이름",'w')
    for i in range(1,11):
      data = "%d번째 줄입니다.\n" % i
      f.write(data)
    f.close()
    ````

- 프로그램의 외부에 저장된 파일을 읽는 방법

  - readline() 함수 이용하기

    - ```` python
      f = opent("현재 파일 위치/파일 이름",'r')
      line = f.readline()
      print(line)
      f.close()
      ````

    - ````python
      f = opent("현재 파일 위치/파일 이름",'r')
      while True:
        line = f.readline()
        if not line: break
        print(line)
      f.close()
      ````

  - readlines 함수 사용하기

    - ````python
      f = opent("현재 파일 위치/파일 이름",'r')
      lines = f.readlines()
      for line in lines:
      	print(line)
      f.close()
      ````

  - Read 함수 사용하기

    - ````python
      f = opent("현재 파일 위치/파일 이름",'r')
      data = f. read()
      print(data)
      f.close()
      ````

- 파일에 새로운 내용 추가하기

  - ````python
    f = opent("현재 파일 위치/파일 이름",'a')
    for i in range(11,20):
      data = "%d번째 줄입니다. \n" % i
      f.write(data)
    f.close()
    ````

  - ````python
    # with문과 함께 사용하기
    with open("foo.txt","w") as f:
      f.write("Life if too short, you need python")
    ````



---



# 1-5. 파이썬 기초_클래스 모듈



## 1. 클래스

- 클래스란 

  - ```python
    class Calculator:
      def __init__(self): # __inti__(self) 생성자 
        self.result = 0 # result라는 변수를 하나 선언함?
        
      def add(self,num): # self -> cal1,cal2가 됨
        self.result += num
        return self.result
    
    cal1 = Calculator() # 자동으로 __init__함수는 불려짐, add는 따로 불러야함 
    cal2 = Calculator()
    
    print(cal1.add(3))
    print(cal1.add(4))
    print(cal2.add(3))
    print(cal2.add(7))
    ```

    

- 객체에 숫자 지정할 수 있게 만들고 더하기 기능 만들기

  - ````python
    class FourCal:
      def setdata(self,first,second):
        self.first = first
        self.second = second
      def add(self):
        result = self.first + self.second
        return reuslt
    
    a = FourCal()
    a.setdata(4,2)
    
    print(a.add())
    ````

- 클래스의 상속

  - ````python
    class MoreFourCal(FourCal): # class 클래스 이름(상속할 클래스 이름)
      pass
    ````

- 메서트 오버라이팅

  - 자식의 기능이 부모의 기능보다 먼저 실행



## 2. 모듈

- 



## 3. 예외처리

- try, except만 쓰는 방법

  - ````python
    try:
      ...
    except:
      ...
    ````

- 발생 오류만 포함한 except문

  - ````python
    try:
      ...
    except 발생 오류:
      ...
    ````

- 발생 오류와 오류 메시지 변수까지 포함한 except문

  - ````python
    try:
      ...
    except 발생 오류 as 오류 메시지 변수:
      ...
    ````

  - ````python
    try:
      4/0
    except:
      ZeroDivisionError as e:
        print(e)
    ````

- finally

  - ````python
    try:
      # 무언가를 수행한다.
    finally: # 무조건 실행하는 구문
      ...
    ````

  - ````python
    try:
      age = int(input('나이를 입력하세요 : '))
    except: # 오류가 발생하면 except를 실행 (오류)
      print('입력이 정확하지 않습니다.')
    else: # 오류가 발생하지 않으면 else를 실행 (정상)
      if age <= 18:
        print('미성년자는 출입금지입니다.')
      else:
        print('환영합니다.')
    ````

- raise 

  - ````python
    class Bird:
      def fly(self):
        raise NotImplementedError # raise : 미리정의된 에러를 강제로 발생시키는 명령어
        
    class Eagle(Bird):
      pass
    
    eagle = Eagle()
    eagle.fly()
    -> error 발생!
    ````

## 4. 내장함수

- `ads()` : 절댓값

- `all()` : 하나라도 True인게 있으면 True

- `any()`: 모두 True여야 True 반환

- `chr()`: 하나의 정수를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환

- `dir()`: 어떤 객체를 인자로 넣어주면 해당 객체가 어떤 변수와 메소드(method)를 가지고 있는지 나열

- `divmod()`: 몫과 나머지를 같이 출력

- `enumerate()`: 인덱스와 값을 같이 출력 가능

  - ````python
    for i, name in enumerate(['body','foo','bar']):
      print(i, name)
    ````

- `eval()` : 매개변수로 받은 String형식의 expression을 실행결과로 반환해주는 함수
- `filter()`: 여러 개의 데이터로 부터 일부의 데이터만 추려낼 때 사용
- `hex()`: 해당 함수는 **매개변수 x에 정수 값을 입력** 받아서 **16진수로 변환하여**, 변환한 값을 반환하는 함수
- `id()`: 주소값을 출력해주는 함수

