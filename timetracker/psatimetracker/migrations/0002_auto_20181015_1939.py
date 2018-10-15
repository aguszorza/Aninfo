# Generated by Django 2.1.2 on 2018-10-15 17:57

from django.db import migrations, models

def default_developers(apps, schema_editor):

    names = ['Pepe Perez', 'Jose Juarez', 'Fernando Fernandez', 'Rodrigo Rodriguez']

    Developer = apps.get_model("psatimetracker", "Developer")
    for person in names:
        dev = Developer(name = person)
        dev.save()

def delete_developers(apps, schema_editor):
    Developer = apps.get_model("psatimetracker", "Developer")
    Developer.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('psatimetracker', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(default_developers, delete_developers),
    ]