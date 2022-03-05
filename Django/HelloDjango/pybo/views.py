from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.utils import timezone


# Create your views here.
def index(requset):
    # question_list = Question.objects.order_by('-create_date')
    # context = {'question_list': question_list}
    # return render(request, 'pybo/question_list.html', context)
    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")

    q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=timezone.now())
    q.save()

    question_queryset = Question.objects.get(id=2)
    res_text = str(question_queryset) + str(question_queryset.content)

    return HttpResponse(res_text)

def orm_cook_book(request):
    # 1. 장고 ORM이 실행하는 실제 SQL 질의문을 확인

    # SELECT "pybo_question"."id", "pybo_question"."subject",
    # "pybo_question"."content", "pybo_question"."create_date" FROM "pybo_question"
    question_queryset = Question.objects.all()

    query = str(question_queryset.query)

    # SELECT "pybo_question"."id", "pybo_question"."subject", "pybo_question"
    # ."content", "pybo_question"."create_date" FROM "pybo_question" WHERE "pybo_question"."id" = 5
    question_queryset = Question.objects.filter(id=5)
    query = str(question_queryset.query)

    return HttpResponse(query)