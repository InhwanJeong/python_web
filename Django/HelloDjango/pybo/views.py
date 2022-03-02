from django.shortcuts import render
# from django.http import HttpResponse
from .models import Question


# Create your views here.
def index(requset):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)
    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")