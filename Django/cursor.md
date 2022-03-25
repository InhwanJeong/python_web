# django raw 쿼리

```python
from django.db import connection

with connection.cursor() as cursor:
    selectSQL = f'SELECT item FROM table'
    cursor.execute(selectSQL)
    # data = cursor.fetchall()
    data = cursor.fetchone() 

    # 데이터 직렬화 필요
```
