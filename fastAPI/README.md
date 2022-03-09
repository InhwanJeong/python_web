# fastAPI
- 빠름((Starlette과 Pydantic 덕분에) NodeJS 및 Go와 대등할 정도로 매우 높은 성능)
- 빠른 코드 작성: 약 200%에서 300%까지 기능 개발 속도 증가
- 적은 버그: 사람(개발자)에 의한 에러 약 40% 감소
- 직관적: 훌륭한 편집기 지원. 모든 곳에서 자동완성. 적은 디버깅 시간.
- 쉬움: 쉽게 사용하고 배우도록 설계. 적은 문서 읽기 시간.
- 짧음: 코드 중복 최소화. 각 매개변수 선언의 여러 기능. 적은 버그.
- 견고함: 자동 대화형 문서와 함께 준비된 프로덕션 용 코드를 얻을 수 있음
- 표준 기반: API에 대한 (완전히 호환되는) 개방형 표준 기반: OpenAPI (이전에 Swagger로 알려졌던) 및 JSON 스키마

### 설치
```bash
pip install fastapi uvicorn[standard]
```

### 서버 실행
```bash
uvicorn main:app --reload
```

### swagger 확인
- localhost:8000/docs