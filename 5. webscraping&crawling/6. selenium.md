# 03.4. 웹스크래핑크롤링을 활용한 데이터 수집_입문

## selenium

## 1. 설치

- Mac
  - 터미널 실행 -> pip install selenium
- 크롬 버전 확인
- 크롬드라이브 다운로드(버전과 운영체제가 일치하는 드라이브 다운로드)



## 2. 크롬브러우저 실행

- ````python
  from selenium import webdriver
  
  url = "https://www.naver.com/"
  driver = webdriver.Chrome(r"/Users/shinjiwoo/chromedriver") # chromedriver가 있는 폴더 경로
  
  driver.get(url)
  ````



## 3. 명령어

- Key event

  - ````python
    from selenium import webdriver
    
    url = "https://www.naver.com/"
    driver = webdriver.Chrome(r"/Users/shinjiwoo/chromedriver") # chromedriver가 있는 폴더 경로
    driver.get(url)
    
    element = driver.find_element_by_class_name("link_login") #네이버 사이트 로그인 버튼 class name으로 찾아오기
    print(element)
    element.click() # 클릭
    element.back() # 뒤로가기
    element.forward() # 앞으로 가기
    element.refresh() # 
    element.back() # 클릭
    ````

- query

  - ````python
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time # 로딩시간을 맞추기 위한 time 라이브러리
    
    url = "https://www.naver.com/"
    driver = webdriver.Chrome(r"/Users/shinjiwoo/chromedriver") # chromedriver가 있는 폴더 경로
    driver.get(url)
    
    element = driver.find_element_by_id("query") # 네이버 검색창 id로 찾아오기
    element.send_keys("컴퓨터") # '컴퓨터' 검색창에 입력
    element.send_keys(Keys.ENTER) # 엔터
    ````

- 파싱(Parsing)

  - ````python
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    
    url = "https://www.naver.com/"
    driver = webdriver.Chrome(r"/Users/shinjiwoo/chromedriver") # chromedriver가 있는 폴더 경로
    driver.get(url)
    
    element = driver.find_element_by_tag_name("a")
    elements = driver.find_element_by_tag_name("a")
    
    for idx,e in enumerate(elements):
      ele = e.get_attribute('href')
      print(ele)
    ````

- XPATH

  - ````python
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    
    url ="https://www.daum.net/"
    driver = webdriver.Chrome(r"/Users/shinjiwoo/chromedriver") # chromedriver가 있는 폴더 경로
    driver.get(url)
    
    element = driver.find_element_by_id("q")
    element.send_keys("인기영화")
    element = driver.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]") # f12 -> 검색 돋보기  클릭 -> copy -> copy xpath로 복사
    element.click() # 클릭
    ````

- 종료

  - ````python
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    
    url ="https://www.daum.net/"
    driver = webdriver.Chrome(r"/Users/shinjiwoo/chromedriver") # chromedriver가 있는 폴더 경로
    driver.get(url)
    
    driver.close() # 현재 탭만 종료
    driver.quit() # 브라우저 자체를 종료
    ````

- 네이버 로그인 - error

  - ````python
    from selenium import webdriver
    import time 
    from selenium.webdriver.common.keys import Keys
    
    url = "https://www.naver.com/"
    driver = webdriver.Chrome(r"/Users/shinjiwoo/chromedriver") 
    
    try:
        driver.get(url)
        element = driver.find_element_by_class_name("link_login") # 로그인 버튼 클릭
        element.click()
        element=driver.find_element_by_id("id").send_keys("sddyy1004") # 아이디 입력
        element=driver.find_element_by_id("pw").send_keys("ekdnstls741!") # 비밀번호 입력
        driver.find_element_by_id("log.login").click() # 로그인 버튼 클릭
        
    except Exception as e:
        print(e)
    ````

- 네이버 로그인 - success

  - ````python
    from selenium import webdriver
    import time 
    from selenium.webdriver.common.keys import Keys
    import pyperclip
    
    url = "https://www.naver.com/"
    driver = webdriver.Chrome(r"/Users/shinjiwoo/chromedriver") 
    
    try:
        driver.get(url)
        element = driver.find_element_by_class_name("link_login")
        element.click()
        
        # 네이버 로그인 우회해서 성공하는 법
        pyperclip.copy("sddyy1004") # 아이디 입력
        driver.find_element_by_id("id").send_keys(Keys.COMMAND,'v') # 복사 붙여넣기
        pyperclip.copy("ekdnslts741!") # 비번 입력
        driver.find_element_by_id("pw").send_keys(Keys.COMMAND,'v') # 복사 붙여넣기
        driver.find_element_by_id("pw").send_keys(Keys.ENTER) # 엔터
    #    driver.find_element_by_id("log.login").click()
    except Exception as e:
        print(e)
    finally:
        print("성공")
    ````



- 네이버 항공권 프로젝트

  - ````python
    # 완성한 코드
    import time
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.common.by import By #이건 어떤 의미?
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC # 이건 어떤 의미?
    
    url = "https://flight.naver.com/"
    driver = webdriver.Chrome(r"/Users/shinjiwoo/student/project 1/selenium/chromedriver")
    # 크롬을 업데이트 버전을 알아서 맞춰줌
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # 창 확대
    driver.maximize_window()
    
    driver.get(url)
    time.sleep(0.5)
    
    # 가는날 클릭
    element = driver.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]")
    element.click()
    time.sleep(0.5)
    
    # 가는날 날짜 선택 (28일)
    element = driver.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[6]/button")
    element.click()
    time.sleep(0.5)
    
    # 오는날 날짜 선택 (31일)
    element = driver.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[6]/td[2]/button")
    element.click()
    time.sleep(0.5)
    
    # 도착지 선택 클릭
    element = driver.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]")
    element.click()
    time.sleep(0.5)
    
    # 도착지 '파리' 검색
    element = driver.find_element_by_class_name("autocomplete_input__1vVkF")
    element.send_keys("파리")
    time.sleep(0.5)
    
    # 첫번째 공항 선택
    element = driver.find_element_by_class_name("autocomplete_search_item__2WRSw")
    element.click()
    time.sleep(0.5)
    
    # 인원 선택
    element = driver.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[3]/button[1]")
    element.click()
    time.sleep(0.5)
    
    # 성인 2명 선택
    element = driver.find_element_by_class_name("searchBox_outer__9n6IB")
    element.click()
    time.sleep(0.5)
    
    # 항공권 검색 두번 클릭
    element = driver.find_element_by_class_name("searchBox_search__2KFn3")
    element.click()
    time.sleep(1)
    
    element = driver.find_element_by_class_name("searchBox_search__2KFn3")
    element.click()
    #time.sleep(11) # 항공권 검색 로딩을 위해 11초 기다리기
    
    # 검색 로딩이 완료 되었을때 화면의 정보를 가져오기 위해 WebDriverWait 사용
    # 50초 전에 page가 로딩 되고 element가 실행된다면 EC는 True를 반환 
    # 로딩 중인 페이지와 다른 부분을 셀렉해서 CSS_SELECTOR copy해서 붙여넣기
    WebDriverWait(driver, 50).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'#__next > div > div.container > div.List_top > div > div.inlineFilter_FilterWrapper__1Icm4 > div > button:nth-child(2) > span')))
    #스크롤을 맨밑으로 내려줌
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)") 
    
    # 가장 저렴한 항공권 정보 출력
    price = driver.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div[3]/div[1]/div")
    print(price.text)
    time.sleep(1)
    ````

    