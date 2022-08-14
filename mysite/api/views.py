from django.shortcuts import render
from polls.models import Question
from .serializers import QuestionSerializer
from rest_framework import viewsets

# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
	queryset = Question.objects.all()
	serializer_class = QuestionSerializer
    