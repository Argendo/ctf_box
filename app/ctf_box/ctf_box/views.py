from django.http import HttpResponse
from django.shortcuts import redirect

def redirect_board(request):
    return redirect('board/', permanent=True)

