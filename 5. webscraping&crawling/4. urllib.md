# 03.4 웹스크래핑크롤링을 활용한 데이터 수집_입문



## urllib 

- 설치

  - mac 
    - 터미널 실행 -> pip install urllib or conda install urllib

- 네이버 첫 페이지 받아오기(urlopen)

  - ````python
    from urllib.request import urlopen # requests 패키지랑 받아오는 코드가 다름 
    
    url = "https://www.naver.com" # 링크 적고
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

