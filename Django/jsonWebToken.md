# Simple JWT

https://django-rest-framework-simplejwt.readthedocs.io/en/latest/

- 요약
    - simple jwt는 admin 계정 정보를 이용한다.
    - username과 password를 전송하면 코인을 획득한다.
    - 코인 사용은 Authorization: Bearer Token을 이용한다.

### 설치

- Requirements
```bash
Python (3.7, 3.8, 3.9, 3.10)
Django (2.2, 3.1, 3.2)
Django REST Framework (3.10, 3.11, 3.12)
```

- Installation
```bash
pip install djangorestframework-simplejwt
```

### 토큰 환경 설정

- setting.py

```python
REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        ...
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    ...        
}

INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt',
    ...
]

```

### 토큰 발급
- urls.py
```python
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ...
]
```