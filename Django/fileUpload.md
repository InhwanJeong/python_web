### 파일 업로드

https://docs.djangoproject.com/en/4.0/topics/http/file-uploads/
https://docs.djangoproject.com/en/4.0/ref/files/uploads/
https://docs.djangoproject.com/en/4.0/_modules/django/core/files/uploadedfile/#InMemoryUploadedFile

- UploadedFile
    - TemporaryUploadedFile
    - InMemoryUploadedFile(기본값)

### TemporaryUploadedFile로 기본값 바꾸기
- 메모리가 아닌 디스크에 임시 저장 파일을 생성하기 위함
    - S3 클라우드 스토리지에 저장할 경우 (upload_file)
    - 다른서버로 이미지를 전송할 경우
- setting.py
```python
FILE_UPLOAD_HANDLERS = (
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
)
```

- views.py
```python
for file in request.FILES.getlist('image'):
    file_name = str(file.name) # inan.png
    local_file_path = file.temporary_file_path() # C:\\Users\\inan\\AppData\\Local\\Temp\\0gy1uo7q.upload.png
```

