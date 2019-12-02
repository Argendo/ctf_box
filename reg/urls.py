from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login, name='login_url'),
    path('logout/', logout, name='logout_url'),
    path('register/', register)
    ]
