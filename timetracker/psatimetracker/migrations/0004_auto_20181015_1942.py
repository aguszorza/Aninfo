# Generated by Django 2.1.2 on 2018-10-15 19:42

from django.db import migrations

def default_tasks(apps, schema_editor):

    Developer = apps.get_model("psatimetracker", "Developer")
    Project = apps.get_model("psatimetracker", "Project")
    Task = apps.get_model("psatimetracker", "Task")
    for project in Project.objects.all():
        task = Task(name = "Tarea para todos", project=project)
        task.save()
        for dev in Developer.objects.all():
            task.developers.add(dev)
            for i in range (1,4):
                dev.task_set.create(name = "Tarea " + str(i) + ": " + dev.name, project=project)




def delete_tasks(apps, schema_editor):
    Task = apps.get_model("psatimetracker", "Task")
    Task.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('psatimetracker', '0003_auto_20181015_1940'),
    ]

    operations = [
        migrations.RunPython(default_tasks, delete_tasks),
    ]
