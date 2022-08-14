from django.shortcuts import render
from polls.models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework import viewsets

# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
 
class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    