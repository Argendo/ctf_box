# Generated by Django 2.1 on 2019-06-30 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=30)),
                ('slug', models.SlugField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True)),
                ('body', models.TextField(blank=True, db_index=True)),
                ('files_link', models.URLField(blank=True, default='127.0.0.1:8000')),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('flag', models.CharField(blank=True, db_index=True, max_length=100)),
                ('categories', models.ManyToManyField(blank=True, related_name='tasks', to='board.Category')),
            ],
            options={
                'ordering': ['-date_pub'],
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
