# GitHud 1일차 특강

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



