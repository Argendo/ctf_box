# Generated by Django 2.1 on 2019-08-03 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20190630_0618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='files_link',
        ),
        migrations.AlterField(
            model_name='task',
            name='flag',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]