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

def detail(request, question_id):
    """
    A view that displays a single question and its choices.
    """
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    print(question.answered_by.all())
    
    if question.answered_by.filter(pk=request.user.pk).exists():
        print("User has already voted")
        
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    """
    Not a view, but a backend route for voting.
    """
    question = get_object_or_404(Question, pk=question_id)
    if question.answered_by.filter(pk=request.user.pk).exists():
        print("User has already voted")
        print(question.answered_by.all())
        
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        question.answered_by.add(request.user)
        selected_choice.votes += 1
        selected_choice.save()
        print(question.answered_by.all())
        
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def _clear_votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answered_by.clear()
    print("Votes cleared")
    print(question.answered_by.all())
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
