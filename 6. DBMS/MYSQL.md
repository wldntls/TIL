# 데이터베이스&SQL



## 1. 데이터베이스 구조

- 테이블

- 데이터베이스(스키마)

- 데이터베이스 서버 (MYSQL Server)

  

## 2. 데이터베이스의 정의와 특징

- 정의
  - DBMS에 사용자와 응용프로그램이 동시 접속하고 데이터를 공유할 수 있음
- 특징
  - 데이터의 무결성
  - 데이터의 독립성
  - 보안
  - 데이터 중복의 최소화
  - 응용 프로그램 제작 및 수정이 쉬어짐
  - 데이터의 안전성 향상
- DBMS 분류
  - 계층형 DBMS
  - 망형 DBMS
  - 관계형 DBMS



## 3. SQL 소개

- DBMS 제작 회사와 독립적이다.
- 다른 시스템으로 이식성이 좋다.
- 표준이 계속 발전한다.
- 대화식 언어이다.
- 분산형 클라이언트/서버구조이다.



## 4. MYSQL 설치

- Mac

  - homebrew 설치

  - ```zsh
    brew install mysql
    mysql -V # 버전 확인
    mysql.server start # 서버 켜기
    비밀번호 설정
    초기 설정 # 재설정 하기 : mysql_secure_installation
    mysql -u root -p # MYSQL 접속
    ```

  - MYSQL Workbench 설치 (사이트 들어가서 )

- 샘플데이터 가져오기

  - ````zsh
    # 해당 과정에서 샘플데이터 employees
    cd 샘플데이터있는 경로 
    파일 경로 확인
    mysql -u root -p
    source 파일이름.sql
    show databases;
    exit 
    ````



## 5. DML - SELECT 문

- 구문 형식 - 기본

  - ````mysql
    SELECT 열 이름
    FROM 테이블 이름
    WHERE 조건
    ````

- USE 구문 형식

  - ````mysql
    USE 데이터베이스_이름;
    USE employees;
    ````

- 기본조회

  - ````mysql
    use mysql;
    select * from employees;
    /* 오류남 */
    ````

  - ````mysql
    select * from titles(테이블명)
    ````

  - ````mysql
    # dept_emp 테이블을 조회하여 다음 출력 결과를 만족하는 SQL을 작성하시오.
    select * from dept_emp;
    
    # departments 테이블을 조회하여 다음 출력 결과를 만족하는 SQL을 작성하시오.
    select * from departments;
    
    # 다른 데이터베이스에 클릭이 되어 있을 때
    select * from employees.titles;
    
    # employees 테이블의 first_name 컬럼을 출력
    select first_name, last_name, gender from employees;
    
    # slaries 테이블의 salary, to_date만 출력해서 다음의 결과를 만족하는 SQL을 작성하시오.
    select salary, to_date from salaries;
    
    /* 블록 주석
    연습*/
    
    # 현재 데이터 베이스에 있는 테이블의 정보 조회
    show table status;
    show tables # 테이블 이름만 조회
    
    # 테이블의 열이 무엇이 있는지
    describe employees; 
    desc employees;
    ````

  - AS 별칭

    - ```mysql
      # first_name은 이름으로 gender은 성별로, hire_date은 회사 입사일 컬럼명으로 결과 출력
      select first_name as 이름, gender 성별, hire_date '회사 입사일'
      from employees;
      
      # employees 테이블을 조회하여 번호, 생일의 컬럼명을 만족하는 SQL을 작성하시오.
      select emp_no as '번호', birth_date '생일' from employees;



## 6. 데이터 베이스 생성

- 정보시스템 구축 절차
  - 계획
  - 분석
  - 설계
  - 개발
  - 시행
- 데이터베이스 모델링과 필수 용어
  - 데이터 베이스(DB) : 테이블이 저장되는 장소
  - DBMS : DataBase Management System의 약자. 데이터베이스를 관리하는 시스템 혹은 소프트웨어 (MYSQL)
  - 열(= 컬럼=필드) : 각 테이블은 열로 구성됨, 아이디, 회원이름, 주소
  - 열 이름 : 각 열을 구분하기 위한 이름
  - 데이터 형식 : 열의 데이터 형식
  - 행 (=로우=레코드) : 실질적인 데이터, 한사람에 대한 데이터
  - 기본키(Primary Key) : 각 행을 구분하는 유일한 열
  - 외래키(Foreign Key) : 두 테이블의 관계를 맺어주는 키
  - SQL(Structured Query Language) : 구조화된 질의 언어, DBMS을 조작하는 언어

- 데이터 베이스 생성
  - Schema 창에서 오른쪽 클릭 
  - Create schema 클릭 
  - schema 명 정해주고 apply
  - 생성한 스키마서 왼쪽 클릭 
  - Create Table 클릭
  - Table 명 입력 (memberTBL, productTBL)
  - Colum name, Datatype 등을 정해주고 apply
  - table에서 왼쪽 클릭 
  - Select Rows - Limit 1000
  - 데이터 입력하고 apply

