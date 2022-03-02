# Django란?
- 3세대 프레임워크
- MVC 패턴
  - model
  - view 
  - controller

### [django 더 자세히 알아보기](./django.md)
- 프로젝트 생성
  - 프로젝트 생성(startproject)
    - manage.py 
    - setting.py
    - urls.py 
    - wsgi.py 
    - asgi.py
  - 프로젝트 앱 생성(startapp)
    - models.py
    - admin.py
    - view.py
    - test.py
- 프로젝트 설정(setting.py)
  - DEBUG : 디버그 모드 설정
  
- manage.py
  - startapp - 앱 생성
  - runserver - 서버 실행 
  - createsuperuser - 관리자 생성
  - makemigrations app - app 모델 변경사항 체크
  - migrate - 변경사항을 DB에 저장
  - shell - 쉘을 통해 데이터 확인 
  - collectstatic - 정적파일을 한곳에 모음