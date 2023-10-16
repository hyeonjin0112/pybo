#from django.http import HttpResponse
from .models import Question
from django.shortcuts import render, get_object_or_404

def index(request):
    #return HttpResponse("안녕하세요 encore에 오신 것을 환영합니다!")
    question_list = Question.objects.order_by('-create_date')
    # - 역순 정렬
    context = {'question_list': question_list}
    return render(request, 'encore/question_list.html', context)
    #render: context에 있는 Question 모델 데이터 question_list 를 pybo/question_list.html 파일에 적용하여 html코드로 변환

def detail(request, question_id):
    #question = Question.objects.get(id = question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'encore/question_detail.html', context)