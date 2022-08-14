from datetime import datetime, timezone
from django.http import HttpResponse, HttpResponseRedirect
from ..models import Choice, Question
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.contrib import auth

def create_question(request):
    """
    Form view for creating questions.
    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('polls:login'))
    return render(request, 'polls/create_question.html')

def create_question_submit(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('polls:login'))
    
    question = Question(question_text=request.POST['question_text'], author=request.user, pub_date=datetime.now())
    question.save()
    
    for field in request.POST:
        if field.startswith('choice'):
            choice = Choice(question=question, choice_text=request.POST[field])
            choice.save()
            
    return HttpResponseRedirect(reverse('polls:index'))