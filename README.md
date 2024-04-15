# TODO App

FastAPI를 사용하여 서비스를 개발하여 FastAPI와 Python의 기능을 익히고자 합니다. 간단한 TODO 애플리케이션을 개발하고자 합니다.

## 설치

```bash
pip install -r requirements.txt
```

## 실행

```bash
uvicorn main:app --reload
# or
uvicorn main:app --reload --host 0.0.0.0 --port=8000
```

접속: <http://localhost:8000/>

## branches

### 01.join_member

DB 접속을 설정 하고 회원가입을 구현합니다.

### 02.auth_login

로그인을 구현합니다. JWT 토큰을 발급합니다.

### 03.auth_currentuser

JWT 토큰에 의해 현재 사용자를 확인합니다.

### 04.todo_crud

TODO의 CRUD를 구현합니다.

### 05.exception

예외 처리를 구현합니다.

### 06.config_logging

config와 logging을 구현합니다.
