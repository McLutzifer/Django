from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)

"""
Question
___________
Question_text
Publish_date


Choices
________
Choice_text
Number_of_Votes
"""