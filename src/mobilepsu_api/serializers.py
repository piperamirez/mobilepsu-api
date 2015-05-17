from rest_framework import serializers
from mobilepsu_api.models import Field, Question

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ('id', 'name')
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'field', 'statement', 'choice_a', 'choice_b', 'choice_c', 'choice_d', 'choice_e', 'correct_answer')