# Generated by Django 3.1.3 on 2020-11-27 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_task_files_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['-score']},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_ack',
            field=models.DateTimeField(default=None),
        ),
    ]
