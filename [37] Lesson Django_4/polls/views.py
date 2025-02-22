from django.shortcuts import render, get_list_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('polls/index.html')

    context = {'username': 'michael', 'password': 'admin1234'}

    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_list_or_404(Question, pk = question_id)
    choices = question.choice_set.all()

    # try:
    #     question = Question.objects.get(pk = question_id)
    #     choices = question.choice_set.all()
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exists")

    context = {'question': question, 'choices': choices}

    return render(request, 'polls/detail.html', context)

# def result(request, question_id):
#     return HttpResponse(f"<h1>Result: {question_id} </h1>")

# def vote(request, question_id):
#     return HttpResponse(f"<h1>Vote: {question_id} </h1>")