from django.db import models

# Create your models here.


class Developer(models.Model):
    name = models.CharField(max_length=200)

class Project(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    developers = models.ManyToManyField(Developer)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class WorkedHours(models.Model):
    hours = models.PositiveIntegerField()
    date = models.CharField(max_length=200)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

