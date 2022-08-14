from ..models import Choice, Question
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

def detail(request, question_id):
    """
    A view that displays a single question and its choices.
    """
    user = request.user
    if not user.is_authenticated:
        return HttpResponseRedirect(reverse('polls:login'))
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    print(question.answered_by.all())
    
    if question.answered_by.filter(pk=request.user.pk).exists():
        print("User has already voted")
        
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    return render(request, 'polls/detail.html', {'question': question})
