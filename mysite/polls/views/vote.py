from django.shortcuts import render, get_object_or_404
from ..models import Question
from ..models import Choice, Question
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

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
