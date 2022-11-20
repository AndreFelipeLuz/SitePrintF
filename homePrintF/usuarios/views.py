from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == "GET":
        return render(request,'cadastro.html')
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.get(nome=nome)

        if user:
            return HttpResponse('Já existe um usuário com esse nome')
        return HttpResponse(nome)

def login(request):
    return render(request, 'login.html')
# Create your views here.
