# Swagger, API 명세


### swagger editor 설치
- URL https://github.com/swagger-api/swagger-editor
```bash
docker pull swaggerapi/swagger-editor
docker run -d -p 80:8080 swaggerapi/swagger-editor
```

### swagger editor 접속 및 작성
- http://localhost/

### swagger 명세서 배포
1.Generate Server - python-flask -> 압축파일 다운로드

2.압축해제 및 폴더 접속

3.requirements.txt 수정

```bash
connexion == 1.1.15
python_dateutil == 2.6.0
setuptools >= 21.0.0
werkzeug==0.16.1
markupsafe==2.0.1
```

4. docker build -t swagger_server .

5. docker run -p 8080:8080 swagger_server


