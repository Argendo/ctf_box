from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from .forms import RegistrationForm

def redirect_board(request):
    return redirect('board/', permanent=True)

@csrf_protect
def login(request):
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        args = {'username': username}
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/', args)
        else:
            args['login_error'] = "Пользователь не найден"
            return render(request, 'reg/login.html', args)
    else:
        return render(request, 'reg/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@csrf_protect
def register(request):
    args={}
    args['form']=RegistrationForm()
    if request.POST:
        new_user_form=RegistrationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            new_user = auth.authenticate(username=new_user_form.cleaned_data['username'], password=new_user_form.cleaned_data['password2'])
            auth.login(request, new_user)
            return redirect('/')
        else:
            args['form'] = new_user_form
    return render(request, 'reg/register.html', args)
