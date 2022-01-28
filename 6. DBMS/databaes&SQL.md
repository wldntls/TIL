



# 데이터베이스&SQL

## 1. SQL문의 분류

- DML(Data Manipulation Language: 데이터 조작 언어)
  - SELECT
  - INSERT
  - UPDATE
  - DELETE
- DDL(Date Definition Language : 데이터 정의 언어)
  - CREATE
  - DROP
  - ALTER
- DCL(Data Contriol Language : 데이터 제어 언어)
  - GRANT
  - REVOKE
  - DENY

## 2. 쇼핑몰 데이터 베이스

- 프로젝트 진행 단계와 폭포수 모델 개념 파악
  - 폭포수 모델
    - 프로젝트 계획
    - 업무 분석
    - 시스템 설계
    - 프로그램 구현
    - 테스트 
    - 유지보수

- 데이터 베이스 모델링 실습
  - 정의 : 현실세계에 있는 것들을 데이터베이스 모델링을 통해 데이터 베이스 안으로 넣어놓는 것?
  - 1단계 : 쇼핑몰 고객 명단을 기록하고 물건을 구매한 내역도 기록
  - 2단계 : 기록된 내용에서 물건을 구매한 적이 없는 고객을 위쪽으로 정렬
  - 3단계
    - L자형 테이블을 빈칸이 있는 곳과 없는 곳으로 분리 
    - 고객 방문 기록 -> 고객 테이블과 구매 테이블로 분리

  - 4단계 : 고객 테이블 중복 없앰
  - 5단계 : 고객 구매 내역에 고객 테이블의 고객 이름을 추가함
  - 6단계 : 1:N 관계 만들기

- 테이블 구조 정의



## 3. 데이터 베이스 만들기

- Workbench 사용법

  - 터미널 실행해서 `mysql.server start` 입력하고 `mysql -u root -p` 입력하고 비밀번호 입력하고 실행

    

- 데이터 베이스 생성

  - ````mysql
    -- 만약 sqldb가 존재하면 우선 삭제
    drop database if exists sqldb; 
    
    -- sqldb 데이터베이스 생성
    create database sqldb;
    
    -- sdldb 불러오기
    use sqldb;
    ````

  

- 테이블 생성

  - ````mysql
    -- 회원 테이블 만들기
    CREATE TABLE usertbl
    ( userID CHAR(8) NOT NULL PRIMARY KEY, -- 사용자아이디(PK)
    userName VARCHAR(10) NOT NULL, -- 이름
    birthYear INT NOT NULL, -- 출생년도
    addr CHAR(2) NOT NULL, -- 지역경기, 서울 경남 식으로 2글자만 입력
    mobile1 CHAR(3), -- 휴대폰의 국번011, 016, 017, 018, 019, 010 등
    mobile2 CHAR(8), -- 휴대폰의 나머지 전화번호(하이픈 제외)
    height SMALLINT, -- 키
    mDate DATE -- 회원 가입일 
    );
    
    -- 회원 구매 테이블(Buy Table의 약자)
    create table buytbl
    ( num int auto_increment not null primary key, -- 순번(PK)
    userID char(8) not null, -- 아이디(FK)
    prodName Char(6) not null, -- 물품명
    groupName char(4), -- 분류
    price int not null, -- 단가
    amount smallint not null, -- 수량
    foreign key (userID) references usertbl(userID)
    );
    ````

  

- 데이터 입력

  - ````mysql
    insert into usertbl values('LSG', '이승기', 1987, '서울','011','1111111', 182, '2008-8-8');
    .
    .
    .
    insert into buytbl values(null, 'BBK', '운동화', null, 30, 2);
    ````

  

- 데이터 검색 

  - ````mysql
    SELECT * FROM usertbl;
    SELECT * FROM buytbl;
    ````



- Select ~ from ~ where 데이터 조회

  - 기본적인 where절	

    - ````mysql
      use sqldb;
      select * from usertbl;
      ````

    - ````mysql
      select * from usertbl where userName = '김경호';
      
      -- 태어난 년도가 1970년 이후이고 키가 182 이상인 사람의 아이디와 이름을 출력
      select userID, userName from usertbl where birthYear >= 1970 and height >= 182;
      
      -- 1970년 이후에 출생했거나 키가 182 이상인 사람의 아이디와 이름을 출력
      select userID, userName from usertbl where birthYear >= 1970 or height >= 182;
      ````

  

- Where 뒤에 오는 것들

  - Between... and, in(), like()

  - ````mysql
    -- 키가 180 이상이고 183 이하의 이름과 키를 출력
    select userName, height from usertbl where height >= 180 and height <= 183;
    select userName, height from usertbl where height between 180 and 183;
    
    -- 주소가 경남, 전남, 경북인 회원의 이름 주소 출력
    select userName, addr from usertbl where addr='경남' or addr ='전남' or addr = '경북';
    select userName, addr from usertbl where addr in ('경남','전남','경북');
    
    -- 이름이 '김'씨인 사람의 이름과 키를 출력 
    select userName, height from usertbl where userName like '김%';
    
    -- usertbl에서 앞에 한글자는 아무글자나오고 뒤에 '종신'인 사람의 이름과 키를 출력
    select userName, height from usertbl where userName like '_종신';
    
    -- 두개 같이 쓰는 것도 가능
    select userName, height from usertbl where userName like '_용%';
    ````

  

  - Any/all/some 그리고 서브쿼리

    - ````mysql
      -- 키가 177보다 큰사람의 이름과 키를 출력
      select userName, height from usertbl where height > 177;
      
      select userName, height from usertbl -- 2. 김경호의 키보다 큰 키를 가진 사람의 이름과 키를 출력
      where height > (select height from usertbl where userName = '김경호'); -- 1. 김경호의 이름을 찾아서 키를 조회하고 
      
      -- 하지만 아래 쿼리는 경남인 사람의 키의 값이 2개가 나오기 때문에 오류가 생김
      select userName, height from usertbl -- 2. 이보다 크거나 같은 사람의 이름과 키를 출력
      where height >= (select height from usertbl where addr = '경남'); -- 1. 주소가 경남인 사람의 키를 조회하고
      
      -- 지역이 '경남'인 사람의 키보다 크거나 같은 사람을 출력
      select userName, height from usertbl
      where height >= any (select height from usertbl where addr = '경남'); -- 173보다 크거나 170보다 크거나 둘 다 출력 결국 170보다 큰사람을 출력 (any, some는 or 느낌 = 여러 결과 중 하나만 만족)
      
      -- 지역이 '경남'인 사람의 키보다 키가 크거나 같은 사람을 출력
      select userName, height from usertbl
      where height >= all(select height from usertbl where addr = '경남'); -- 173 그리고 170 보다 크거나 같은 사람을 출력 결국 173보다 크거나 같은 사람을 출력(all은 and 느낌 = 여러 결과 중 모두 만족)
      
      -- 지역이 '경남'인 사람의 키와 같은 사람만 출력
      select userName, height from usertbl
      where height in (select height from usertbl where addr = '경남'); -- =any는 in과 같음
      ````

      

    - Order by 

      - order by 절은 select, from, where, group by, having, order by 중 맨 뒤에 와야 한다.

      - order by절은 mysql의 성능을 상당히 떨어뜨릴 소지가 있으므로, 꼭 필요한 경우에만 사용한다.

      - ````mysql
        -- mDate를 기준으로 내림차순으로 정렬 (기본 셋팅은 오름차순)
        select usrName, mDate from usertbl order by mDate desc; 
        
        -- height를 기준으로 내림차순, 다음으로 userName으로 오름차순
        slect userName, height from usertbl order by height desc, userName asc;
        ````

    - distint

      - ````mysql
        -- 중복 제거
        select distinct addr from usertbl;
        ````

    - Limit 

      - ````mysql
        -- 출력 갯수 제한
        select emp_no, hire_date from employees 
        order by hire_date asc
        limit 5; (limit 0,5 = limit 5 offset 0)
        ````

  - Create table~ select 구문 테이블 복사해서 사용

    - 형식

      - ```mysql
        select table 새로운테이블 (select 복사할열 from 기존테이블)
        ```

    - ````mysql
      -- buytbl을 buytbl2로 복사
      use sqldb;
      create table buytbl2 (select * from buytbl);
      select * from buytbl2;
      
      -- buytbl을 buytbl3로 복사
      create table buytbl3 (select userID, prodName from buytbl);
      select * from buytbl3; 
      ````

  - Group by  및 having 그리고 집계 함수

    - ````mysql
      use sqldb;
      select userID, sum(amount) from buytbl group by userID;
      
      select userID as '사용자 아이디', sum(price*amount) as '총 구매 개수'
      from buytbl group by userID;
      ````

    - 

