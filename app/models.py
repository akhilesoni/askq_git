from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Topic(models.Model):
    name = models.CharField(max_length=50)

class Question(models.Model):
    content = models.CharField(max_length=200)
    asked = models.DateTimeField(auto_now_add=True)
    active = models.DateTimeField(auto_now=True)
    view = models.IntegerField()
    topicid = models.ForeignKey(Topic,on_delete=models.CASCADE)
    personid = models.ForeignKey(Person,on_delete=models.CASCADE)    

class Answer(models.Model):
    content = models.CharField(max_length=200)
    answered = models.DateTimeField(auto_now_add=True)
    vote = models.IntegerField()
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    person = models.ForeignKey(Person,on_delete=models.CASCADE)