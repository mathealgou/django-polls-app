from polls.models import Question
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Question
		fields = ('id', 'question_text', 'pub_date')