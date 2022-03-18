### 장고 프로젝트 생성하기
- 다음 명령어는 manage.py와 config 폴더를 생성해준다.
```bash
# django-admin startproject HelloDjango
django-admin startproject config .
```

- 서버 구동 테스트
```bash
# python manage.py runserver 8080
# python manage.py runserver 0.0.0.0:8080
python manage.py runserver
```
- 프로젝트 앱 생성
```bash
python manage.py startapp api
```

- 슈퍼 유저 생성
```bash
python manage.py createsuperuser
```

- 모델 생성
```bash
python manage.py makemigrations
python manage.py migrate
```
