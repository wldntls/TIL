# HTML 시작하기



## 1. HTML이란?

- HyperTextMarkup Language의 약자
- 웹 사이트를 만들기 위해 사용하는 프로그래밍 언어



## 2. HTML태그의 구성 요소와 HTML 문서의 기본 구조

- HTML 태그는 열린 태그와 닫힌 태그, 속성, 속성 값으로 구성됨

- <열린태그 속성 = 속성값;> 콘텐츠 </닫힌태그>

  - 기본 구조

  - ```html
    <!DOCTYPE html>
    <html>
      <head>
        <title> 빅데이터 분석가 과정입니다. </title>
      </head>
    
      <body> 
        안녕하세요.
        좋은 오후입니다.
        ^^
        <br><br>
        <a href="https://www.naver.com/" target="_blank" title="네이버로 이동">네이버</a>
      </body>
    </html>
    ```

    - a - 사이안에 있는 글씨를 클릭하면 사이트로 들어갈 수 있도록 해주는 명령어 

      Href - 연결할 주소

      Title - 들어가기 전에 미리 정보를 알려줌 

      Target - 새탭으로 들어가서 열어줌 (_self라고 쓰면 그냥 자기자신이 있는 탭에서 열림, 생략된 것이랑 똑같음)

- <img> 태그

  - ````html
    <img src="dog1.png" width="300px" height="300px" alt="키즈가오 회사 로고">
    ````

- <p>
    
  </p>

- 