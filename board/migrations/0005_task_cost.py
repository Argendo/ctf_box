# Generated by Django 2.1 on 2019-08-30 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_task_solvers'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='cost',
            field=models.IntegerField(default=50),
        ),
    ]
