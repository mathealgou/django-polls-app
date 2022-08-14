from polls.models import Question, Choice
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        
        # fields = ('id', 'question_text', 'pub_date')
  
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'
        # fields = ('id', 'question', 'choice_text', 'votes')