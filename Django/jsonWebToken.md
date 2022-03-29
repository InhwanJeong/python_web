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

### 토큰 만료 시간 설정
- setting.py
```python
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=2),
}
```

### API 접근 권한 설정

- setting.py
```python
REST_FRAMEWORK = { # 권한 설정
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
    ]
}
```

### 토큰 커스텀
```python
# JWT custom class
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['index'] = user.index
        token['id'] = user.username

        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
```


### 토큰 사용

```python
from rest_framework.views import APIView
class Login(APIView):
    permission_classes = [AllowAny]
    def post(self, request, id):
        tokenString = str(request.META['HTTP_AUTHORIZATION']).split(' ')[-1]
        accessTokenObject = AccessToken(tokenString)
        accessTokenObject["index"]
```
