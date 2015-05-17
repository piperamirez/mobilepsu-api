#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

FIELDS = (
    (0, 'Matemática'),
    (1, 'Lenguaje y Comunicación'),
    (2, 'Biología'),
    (3, 'Física'),
    (4, 'Química'),
    (5, 'Historia y Ciencias Sociales'),
)

CHOICES = (
    (0, 'A'),
    (1, 'B'),
    (2, 'C'),
    (3, 'D'),
    (4, 'E'),
)

class Field(models.Model):
    name = models.SmallIntegerField(choices = FIELDS)
    def __str__(self):
            return '%s' % (self.get_name_display())

class Question(models.Model):
    field = models.ForeignKey(Field)
    statement = models.CharField(max_length = 500)
    choice_a = models.CharField(max_length = 100)
    choice_b = models.CharField(max_length = 100)
    choice_c = models.CharField(max_length = 100)
    choice_d = models.CharField(max_length = 100)
    choice_e = models.CharField(max_length = 100)
    correct_answer = models.SmallIntegerField(choices = CHOICES)
    
class Test(models.Model):
    field = models.ForeignKey(Field)
    questions = models.ManyToManyField(Question)

class User(models.Model):
    username = models.CharField(max_length = 200)

class UserAnswer(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    answer = models.SmallIntegerField(choices = CHOICES)