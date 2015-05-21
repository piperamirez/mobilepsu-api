from django.db import models

CHOICES = (
    (0, 'A'),
    (1, 'B'),
    (2, 'C'),
    (3, 'D'),
    (4, 'E'),
)
DIFFICULTIES = (
    (0, 'EASY'),
    (1, 'NORMAL'),
    (2, 'HARD'),
)

class Field(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return '%s' % (self.name)

class Topic(models.Model):
    field = models.ForeignKey('Field')
    name = models.CharField(max_length = 100)
    def __str__(self):
        return '%s - %s' % (self.field, self.name)

class Test(models.Model):
    field = models.ForeignKey('Field')
    questions = models.ManyToManyField('Question')

class Question(models.Model):
    topic = models.ForeignKey('Topic')
    statement = models.CharField(max_length = 500)
    choice_a = models.CharField(max_length = 100)
    choice_b = models.CharField(max_length = 100)
    choice_c = models.CharField(max_length = 100)
    choice_d = models.CharField(max_length = 100)
    choice_e = models.CharField(max_length = 100)
    difficulty = models.SmallIntegerField(choices = DIFFICULTIES)
    correct_answer = models.SmallIntegerField(choices = CHOICES)
    def __str__(self):
        return '%s: %s' % (self.field, self.statement)

class User(models.Model):
    username = models.CharField(max_length = 200)

class UserAnswer(models.Model):
    user = models.ForeignKey('User')
    question = models.ForeignKey('Question')
    answer = models.SmallIntegerField(choices = CHOICES)