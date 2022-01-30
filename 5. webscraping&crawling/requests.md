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

    
