from django.shortcuts import get_object_or_404, render
from ..models import Question
def search(request):
    if request.method == 'POST':
        search_term = request.POST['search_term']
        
        questions = Question.objects.filter(question_text__icontains=search_term)
        # questions = Question.objects.filter(question_text__contains=search_term)
        context = {
            "search_term": search_term,
            "questions": questions,
        }
        
        return render(request, 'polls/search.html', context)
    
    return render(request, 'polls/search.html')