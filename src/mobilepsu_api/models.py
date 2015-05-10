#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

class Field(models.Model):
    FIELDS = (
        (0, 'Matemática'),
        (1, 'Lenguaje y Comunicación'),
        (2, 'Biología'),
        (3, 'Física'),
        (4, 'Química'),
        (5, 'Historia y Ciencias Sociales'),
    )
    name = models.SmallIntegerField(choices = FIELDS)

class Test(models.Model):
    field = models.ForeignKey(Field)
    
class Question(models.Model):
    test = models.ForeignKey(Test)
    statement = models.CharField(max_length = 500)
    
class Alternative(models.Model):
    ALTERNATIVES = (
        (0, 'A'),
        (1, 'B'),
        (2, 'C'),
        (3, 'D'),
        (4, 'E'),
    )
    question = models.ForeignKey(Question)
    description = models.CharField(max_length = 500)
    index = models.SmallIntegerField(choices = ALTERNATIVES)

class CorrectAnswer(models.Model):
    question = models.ForeignKey(Question)
    alternative = models.ForeignKey(Alternative)

class User(models.Model):
    username = models.CharField(max_length = 200)

class UserAnswer(models.Model):
    user = models.ForeignKey(User)
    alternative = models.ForeignKey(Alternative)