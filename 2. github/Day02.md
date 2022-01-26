# GitHud 2일차 특강

---



## 1. .gitignore

### (1) 의미

- 특정 파일 혹은 폴더에 대해 Git이 버전 관리를 하지 못하도록 지정하는 것



### (2) .gitignore에 작성하는 목록

- 민감한 정보가 담긴 개인정보(전화번호, 계좌전호, 각종 비밀번호 등)
- OS(운영체제)에서 활용되는 파일
- IDE(통합 개발 환경 - pycharm) 혹은 Text editor(vscode) 등에서 활용되는 파일
- 개발 언어(python) 혹은 프레임워크(django)에서 사용되는 파일



### (3) .gitignore 작성 시 주의사항

- 반드시 이름을 `.gitignore`로 작성합니다. 앞의 점(.)은 숨김 파일이라는 뜻입니다.
- `.gitignore` 파일은 `.git` 폴더와 동일한 위치에 생성합니다.
- 제외 하고 싶은 파일은 반드시 `git add` 전에 `.gitignore`에 작성합니다.
- `git add a.txt` 라고 작성하면, 이제 Git은 `a.txt`를 버전 관리의 대상으로 여깁니다. 따라서 반드시 `git add` 전에 `.gitignore`을 작성해야 합니다.



### (4) .gitignore 쉽게 작성하기

- [웹사이트-gitignore.io](https://www.toptal.com/developers/gitignore)
- [웹사이트-gitignore 저장소](https://github.com/github/gitignore)

---



## 2. clone, pull



### (1) 원격 저장소 가져오기

#### 1.  clone

- 원격 저장소의 커밋 내역을 모두 가져와서, 로컬 저장소를 생성하는 명령어
- "복제"라는 뜻으로, `git clone` 명령어를 통해 원격 저장소를 내 컴퓨터로 옮길 수 있습니다. 
- `git clone <원격 저장소 주소>`의 형태로 작성합니다.
- `git clone`= 폴더 만들고 -> `git init`-> `git remote` -> 데이터 가져오기
- `git clone` 처음 한번만 실행! Github에서 저장소를 복제해서 내 컴퓨터에 똑같은 복제본을 만드는 역할



#### 2. git pull

- 원격 저장소의 변경 사항을 가져와서, 로컬 저장소를 업데이트하는 명령어
- `git pull <저장소 이름> <브랜치 이름>`의 형태로 작성합니다. 
- Ex) `git pull origin master` -> git 명령어를 사용할건데, origin이라는 원격 저장소의 master 브랜치의 내용을 가져온다(pull).
- `git pull` git push처럼 로컬 저장소와 원격 저장소의 내용을 동기화하고 싶다면 언제든 사용!
- 로컬저장소 --`git push`--> 원격저장소(Github)
- 원격저장소(Github) --`git pull`--> 로컬저장소

---



- **내 컴퓨터에서 로컬 저장소 만들어져 있는 상황**

`git push`

내 컴퓨터 내용 변경

`git add .`

`git commit -m "~"`

`git push -u origin master`

 github 페이지 변경사항 확인!



- **다른 내 컴퓨터로 변경사항 받아서 수정할 때(로컬 저장소 없음)**

`git init` -> 로컬 저장소 만들어 주는 것

`git clone`-> 원격 저장소를 로컬 저장소로 옮기기 위한 것 (연결 다리까지 만들어줌)

다른 내 컴퓨터 내용 수정

`git add .`

`git commit -m "~"`

`git push -u origin master`

 github 페이지 변경사항 확인!



- **다시 내 컴퓨터에서 변경사항 확인하고 수정할 때**

`git pull` -> 원격저장소에 있는 수정사항 업로드 됨.

내 컴퓨터 내용 수정 

이후에는 위와 같음. 계속 반복



