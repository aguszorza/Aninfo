from django.db import models

# Create your models here.


class Developer(models.Model):
    name = models.CharField(max_length=200)

class Project(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    completedTime = models.PositiveIntegerField(default=0)

