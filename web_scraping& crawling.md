# 03.4 웹스크래핑크롤링을 활용한 데이터 수집_입문



## 1. 크롤링 

- 스크래핑
- 스크래퍼
- 크롤링 
  - 웹 페이지의 하이퍼링크를 순회하면서 웹페이지를 다운로드 하는 작업
  - F12 -> element -> 화살표 도구 -> 원하는 위치 클릭 -> copy -> copy Xpath, copy selector 을 많이 써서 해당 위치를 크롤링함(full은 너무 긺.)  

- 크롤러 : 크롤링하는 소프트웨어
- HTML Tag (명령어 도구)
- 크롬 개발자 도구
  - Elements Tab - CSS Selector, XPATH
  - Network Tab =Http 처리 과정

- Status Code: 200  -> 정상



## 2. 주의사항

- 대상 웹 페이지 조건 확인 : https://www.naver.com/robots.txt 
  - User-agent : 다음 규칙이 적용되는 로봇의 이름 ('*'은 전체를 의미)
  - Disallow : 차단할 URL 경로
  - Allow : 차단 된 상위 디렉토리의 하위 디렉토리에 있는 URL 경로이며 차단을 해제할 디렉토리
- Javascript 사용 유무를 알아야함 
- request 요청시 서버 부하를 고려해야함
- 콘텐츠 저작권
- 구조 변경 가능성 수정



## 3. requests 패키지

- 설치 
  - mac 
    - 터미널 실행 -> pip install requests or conda install requests

- 네이버 연결 확인 

  - ````python
    import requests
    
    res = requests.get("https://www.naver.com/") #  정상 사이트
    res = requests.get("https://yyy.tistory.com") # 오류 사이트 (번갈아서 주석을 달면서 오류와 정상 값 확인해보기)
    
    print("status_code : ", res.status_code) # 정상 : 200 
    
    if res.status_code == 200 :
        print("정상")
    else:
        print("오류", res.status_code) # 정상이면 '정상' 출력, 오류면 '오류'와 코드값 출력
    ````

  - ````python
    if res.status_code == requests.codes.ok : # 만약 res.status 값과 요청 코드 값이 같다면 
        print("정상")
    else:
        print("오류", res.status_code)
    ````

  - ````python
    import requests
    
    res = requests.get("https://www.naver.com/") 
    res = requests.get("https://yyy.tistory.com")
    
    res.raise_for_status() # 정상이라면 다음 단계로 넘어감
    print("정상입니다.")
    print(len(res.text)) # 스크래핑 문서 길이 출력
    print(res.text) # 스크래핑 문서 출력
    ````

    

## 4. urllib 

- 설치
  - mac 
    - 터미널 실행 -> pip install urllib or conda install urllib

- 네이버 첫 페이지 받아오기

  - ````python
    from urllib.request import urlopen # requests 패키지랑 받아오는 코드가 다름 
    
    url = "https://www.naver.com" # url 쓰고
    html = urlopen(url) # url open 해서 html에 담고 
    print(html.read()) # html 읽어서 프린트
    ````

- Error 처리

  - ````python
    from urllib.request import urlopen
    from urllib.request import HTTPError 
    
    try:
        html = urlopen("http://www.google.com/kim.html") # url은 접속 성공, 문서가 없음 
    except HTTPError as e:
        print(e) # 출력
    else:
      print("성공") # kim.html 없었으면 "성공"이 출력
    ````

  - ```python
    from urllib.request import urlopen
    from urllib.request import HTTPError
    from urllib.request import URLError
    
    try:
        html = urlopen("http://www.dddsdf.com/kim.html") # url 접속 없음
    except HTTPError as e:
        print(e)
    except URLError as e: 
        print('The server coult not be found!') # 출력
    else:
        print("성공")
    ```



## 5. BeautifulSoap

- 설치 
  - mac 
    - 터미널 실행 -> pip install bs4 or conda install bs4

- 크롤링 : 웹에서 데이터를 받아오는 것
- 파싱 : 필요한 내용만 추출하는 것 



- 파싱

  - ````python
    import bs4
    
    html_str = "<html><div>hello</div></html>" # 크롤링할 문서
    bs_obj = bs4.BeautifulSoup(html_str,"html.parser") # html.parser는 문서를 문단별로? 나눠서 저장해주는 라이브러리
    
    print(type(bs_obj) # type은 class
    print(bs_obj) 
    print(bs_obj.find("div")) # "div" 부분을 find 해서 출력
    ````



- `.find()`

  - ````python
    import bs4
    
    html_str = """
    <html>
        <body>
            <ul>
                <li>hello</li>
                <libye</li>
                <li>welcome</li>
            </ul>
        </body>
    </html>
    """
    
    bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
    ul = bs_obj.find("ul") # ul 부분만 찾아서 ul에 담기 
    
    print(ul) # ul 부분만 출력됨
    ````



- hello만 뽑아내기

  - ````python
    bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
    ul = bs_obj.find("ul") # ul 부분만 찾아서 ul에 담기 
    li = ul.find("li") # ul에서 li 부분 담아서 li에 담기
    
    print(li) # 첫번째 li 부분만 출력
    ````

  

- Hello 글자만 뽑아내기

  - ````python
    bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
    ul = bs_obj.find("ul")
    li = ul.find("li")
    
    print(li.text) # 첫번째 li 부분 텍스트만 출력
    ````



- `findAll()` or `find_all()`

  - ```python
    bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
    ul = bs_obj.find("ul")
    lis = ul.findAll("li") # findAll은 모든 li 부분을 리스트로 바꿔줌
    
    print(li.text) # li 모든 부분 출력
    ```



- bey 텍스트만 나오게 하기

  - ````python
    s_obj = bs4.BeautifulSoup(html_str, "html.parser")
    ul = bs_obj.find("ul")
    lis = ul.findAll("li")
    
    print(lis[1].text) # li 부분에서 bey 텍스트만 나오게 하는 코드 



- 데이터 뽑을 때 class 속성 이용하기

  - ````python
    import bs4
    
    html_str = """
    <html>
        <body>
            <ul class = "greet">
                <li>hello</li>
                <li>bye</li>
                <li>welcome</li>
            </ul>
            <ul class ="reply">
                <li>ok</li>
                <li>no</li>
                <li>sure</li> 
            </ul>
        </body>
    </html>
    """
    
    bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
    ul = bs_obj.find("ul")
    
    print(ul) # 첫번째 클래스인 <ul class = "greet">...</ul> 이부분만 출력됨
    ````

  - ````python
    # <ul class ="reply">...</ul> 이부분이 뽑고 싶을 때
    
    bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
    ul = bs_obj.find("ul",{"class":"reply"}) # ul 부분에서 class의 속성 값이 reply인 값
    
    print(ul)
    ````



- 속성값 뽑아내기

  - ````python
    import bs4
    
    html_str = """
    <html>
        <body>
            <ul class = "ko">
                <li>
                    <a href = "https://www.naver.com/">네이버</a>
                </li>
                <li>
                    <a href = "https://www.daum.net/">다음</a>
                </li>
            <ul class ="sns">
                <li>
                    <a href = "https://www.google.co.kr/">구글</a>
                </li>
                <li>
                    <a href = "https://www.facebook.com/">페이스</a>
                </li>
            </ul>
        </body>
    </html>
    """
    
    bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
    atag = bs_obj.find("a")
    
    print(atag) #  출력결과 : <a href = "https://www.naver.com/">네이버</a>
    print(atag['href']) # 출력결과 : https://www.naver.com/
    ````

  

- 이미지 다운로드 하기(2021 5개)

  - ````python
    import requests
    from bs4 import BeautifulSoup
    
    url = "https://search.daum.net/search?w=tot&q={0}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    res = requests.get(url)
    res.raise_for_status()
    
    # 1. 크롤링한 데이터를 bs4객체로 변환
    soup = BeautifulSoup(res.text,"html.parser") # res.text는 크롤링 하기 위해 텍스트 파일로 뽑아둔 것
    
    images = soup.findAll("img",attrs={"class":"thumb_img"}) # img에 있는 class의 속성이 thumb_img 것을 모두 가져와 images에 담기, attrs는 속성값을 정해주는 것?
    
    for idx,image in enumerate(images): # enumerate 인덱스와 결과 값을 같이 얻을 수 있음, idx는 인덱스 값을 얻기 위한 것
      img_url = image["src"] # 크롤링한 문서에서 src 소스를 img_url에 담기
      if img_url.startswith("//"): # 만약 처음 시작이 '//'이라면 
      	img_url = "http:" + img_url #http 합치기
    
        img_res = requests.get(img_url) # 이미지 사이트 크롤링 하는 것
        img_res.raise_for_status() 
        # image 저장, 파일 읽기 위해 텍스트 문서에는 'w'이지만 바이너리이기 떄문에 'wb'
        with open("movie{0}_{1}.jpg".format(idx+1, year),"wb") as f: # 인덱스는 0부터 시작하기 때문에 +1 해줌 
          f.write(img_res.content) # 속성이 text가 아니라 image이기 때문에 content
    
          if idx >= 4: 
            break; # 상위 다섯개의 이미지를 다운로드 해야하기 때문에 인덱스가 4와 같거나 작으면 멈추게 설정함
    ````

- 이미지 다운로드(2016~2020 : 5개 씩)

  - ````python
    import requests
    from bs4 import BeautifulSoup
    
    for year in range(2016, 2021): # for문을 이용해 2016~2021까지년도 돌리기 
        url = "https://search.daum.net/search?w=tot&q={0}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year) # formating을 통해 년도 입력 받기
        res = requests.get(url)
        res.raise_for_status()
    
        soup = BeautifulSoup(res.text,"html.parser") 
        images = soup.findAll("img",attrs={"class":"thumb_img"}) 
        
        for idx,image in enumerate(images): 
            img_url = image["src"] 
            if img_url.startswith("//"):
                img_url = "http:" + img_url
            img_res = requests.get(img_url)
            img_res.raise_for_status()
    
            with open("movie{0}_{1}.jpg".format(idx+1, year),"wb") as f: # "movie{인덱스}_{년도}"
                f.write(img_res.content)
            
            if idx >= 4:
                break;
    ````

    