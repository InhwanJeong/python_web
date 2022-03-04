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

    question_item = Question.objects.get(id=2)
    res_text = str(question_item) + str(question_item.content)

    return HttpResponse(res_text)