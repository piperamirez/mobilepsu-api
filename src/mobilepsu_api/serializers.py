from rest_framework import serializers
from mobilepsu_api.models import Field, Topic, Question, Test

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ('id', 'name')

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'field', 'name')

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('id', 'field', 'questions')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'topic', 'statement', 'choice_a', 'choice_b', 'choice_c', 'choice_d', 'choice_e', 'difficulty', 'correct_answer')