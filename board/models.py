from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from time import time
from django.db.models.signals import post_save


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    last_ack = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score', 'last_ack']

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class Task(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    categories = models.ManyToManyField('Category', blank=True, related_name='tasks')
    solvers = models.ManyToManyField(User, blank=True, related_name='tasks')
    solvers_count = models.IntegerField(default=0)
    date_pub = models.DateTimeField(auto_now_add=True)
    flag = models.CharField(max_length=100, db_index=True)
    files_link = models.URLField(default='', blank=True)
    cost = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('task_details_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('task_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('task_delete_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


    class Meta:
        ordering = ['-date_pub']


class Category(models.Model):
    title = models.CharField(max_length=30, db_index=True)
    slug = models.SlugField(max_length=30, unique=True)

    def get_absolute_url(self):
        return reverse('category_details_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('category_update_url', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('category_delete_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)

    class Meta:
        ordering = ['title']
