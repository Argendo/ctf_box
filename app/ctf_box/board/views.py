from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from urllib.parse import unquote
from django.http import HttpResponse

from .models import Task, Category
from .utils import  *
from .forms import CategoryForm, TaskForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.db.models import Q

def main_page(request):
    return render(request, 'board/main.html', context = {'username': auth.get_user(request).username})

def task_board(request):

    tasks = Task.objects.all()

    paginator = Paginator(tasks, 5)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url=''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url=''

    context = {'page_object': page, 'is_paginated': is_paginated, 'next_url': next_url, 'prev_url': prev_url, 'username': auth.get_user(request).username}

    return render(request, 'board/index.html', context=context)


def TaskDetail(request, slug):
    task = Task.objects.get(slug__iexact=slug)
    solvers = task.solvers.all()
    context = {'solvers': solvers}
    if request.user in solvers:
        return render(request, 'board/task_details.html', context = {'task': task, 'admin_object': task, 'detail': True, 'username': auth.get_user(request).username, 'solved': True, 'attempt': True})
    elif 'flag' in request.GET:
        flag = request.GET['flag']
        if unquote(flag) == task.flag:
            task.solvers.add(User.objects.get(username=str(request.user.username)))
            task.save()
            return render(request, 'board/task_details.html', context = {'task': task, 'admin_object': task, 'detail': True, 'username': auth.get_user(request).username, 'solved': True, 'attempt': True})
        else:
            return render(request, 'board/task_details.html', context = {'task': task, 'admin_object': task, 'detail': True, 'username': auth.get_user(request).username, 'solved': False, 'attempt': True})
    else:
        return render(request, 'board/task_details.html', context = {'task': task, 'admin_object': task, 'detail': True, 'username': auth.get_user(request).username})


class TaskCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TaskForm
    template = 'board/task_create_form.html'
    raise_exception = True

class TaskUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Task
    form_model = TaskForm
    template = 'board/task_update_form.html'
    raise_exception = True

class TaskDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Task
    template = 'board/task_delete_form.html'
    redirect_url = 'task_board_url'
    raise_exception = True

class CategoryDetail(ObjectDetailMixin, View):
    model = Category
    template = 'board/category_details.html'


class CategoryCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = CategoryForm
    template = 'board/category_create.html'
    raise_exception = True

class CategoryUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Category
    form_model = CategoryForm
    template = 'board/category_update_form.html'
    raise_exception = True

class CategoryDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Category
    template = 'board/category_delete_form.html'
    redirect_url = 'categories_list_url'
    raise_exception = True


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'board/categories_list.html', context = {'categories': categories, 'username': auth.get_user(request).username})


def bbp(request):
    return render(request, 'board/bbp.html', context = {'username': auth.get_user(request).username})
