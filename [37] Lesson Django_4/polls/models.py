from django.db import models
from django.utils import timezone
from datetime import timedelta

# One To Many

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self) -> str:
        return self.question_text


def was_published_recently(self):
    return self.pub_date >= timezone.now() - timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text

# # One To One
# class Profile(models.Model):
#     description = models.TextField()

# class User(models.Model):
#     username = models.CharField(max_length=50)
#     profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

# # Many To Many

# class Course(models.Model):
#     title = models.CharField(max_length=200)
#     students = models.ManyToManyField('Student')

# class Student(models.Model):
#     name = models.CharField(max_length=50)



# # Create your models here.
