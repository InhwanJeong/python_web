# Redis 연동 캐싱

### redis 설치
```bash
sudo docker pull redis
```

- redis-cli를 통해 캐쉬 및 데이터 확인(docker network 구성)
```bash
sudo docker network create redis-net

# 생성된 docker network 확인
docker network ls
```

- redis-server라는 컨테이너를 만들고 포트는 6379, redis-net이라는 브리지를 사용
```bash
sudo docker run --name redis-server -p 6379:6379 --network redis-net -d redis redis-server
```

- redis-cli로 실행한 redis-server 접속하기
    - --rm은 기존 컨테이너가 존재하면 삭제하고 다시 실행합니다.
```bash
sudo docker run -it --network redis-net --rm redis redis-cli -h redis-server
```

- redis 사용
```bash
$ set 1 "test"
OK
$ get 1
"test"
$ keys *
1) "backup4"
2) "backup1"
3) ":1:1"    # django cache로 생성한 key  
4) "1"       # redis-cli에서 생성한 key
5) "backup2"
6) "backup3"
$ get :1:1
"test" 
```

### django 설정
- https://github.com/jazzband/django-redis
- django-redis 프레임워크 설치
```bash
pip install django-redis
```

- setting.py
```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://118.67.153.---:6379',
    },
}
```
- 서버 측에서는 인바운드설정을 해주어야함.
    - 127.0.0.0:6379
    
- view.py
```python
cache_key = 1
cache_value = cache.get(cache_key, None)

if not cache_value:
    cache_value = civilNewRepair + roadNewRepair

    # 3600초 = 60분 = 1시간 * 3
    cache.set(cache_key, cache_value, 60 * 60 * 3)
```