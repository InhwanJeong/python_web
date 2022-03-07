### 1. 장고 ORM이 실행하는 실제 SQL 질의문을 확인

```python
# SELECT "pybo_question"."id", "pybo_question"."subject",
# "pybo_question"."content", "pybo_question"."create_date" FROM "pybo_question"
question_queryset = Question.objects.all()
query = str(question_queryset.query)

# SELECT "pybo_question"."id", "pybo_question"."subject", "pybo_question"
# ."content", "pybo_question"."create_date" FROM "pybo_question" WHERE "pybo_question"."id" = 5
question_queryset = Question.objects.filter(id=5)
query = str(question_queryset.query)
```

### 2. ORM OR 연산으로 일부 조건을 하나라도 만족하는 항목을 구하기
```python
    # 2. OR 연산으로 일부 조건을 하나라도 만족하는 항목을 구하기
    # SELECT "pybo_question"."id", "pybo_question"."subject", "pybo_question"."content",
    # "pybo_question"."create_date" FROM "pybo_question" WHERE ("pybo_question"."subject" LIKE q% ESCAPE '\' OR "pybo_question"."subject" LIKE w% ESCAPE '\')
    question_queryset = Question.objects.filter(subject__startswith='q') | Question.objects.filter(subject__startswith='w')
    query = str(question_queryset)
    queryDataAll = [i for i in question_queryset]

    question_queryset = Question.objects.filter(Q(subject__startswith='q') | Q(subject__startswith='w'))
    query = str(question_queryset)
    queryDataAll = [i for i in question_queryset]
```