from django.http import HttpResponse, HttpResponseRedirect
from ..models import Choice, Question
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.contrib import auth

def index(request):
    """
    Home of the polls app. It shows a list of all the polls.
    """
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('polls:login'))
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list, 'user_name': user.username}
    return render(request, 'polls/index.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def _clear_votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answered_by.clear()
    print("Votes cleared")
    print(question.answered_by.all())
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
