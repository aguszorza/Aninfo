# Generated by Django 2.1.2 on 2018-10-25 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('psatimetracker', '0005_auto_20181017_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='workedhours',
            name='developer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='psatimetracker.Developer'),
            preserve_default=False,
        ),
    ]
