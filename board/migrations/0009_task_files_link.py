# Generated by Django 2.1 on 2019-09-29 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_task_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='files_link',
            field=models.URLField(blank=True, default=''),
        ),
    ]
