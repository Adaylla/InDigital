from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def reserva(request):
    return render(request, "reserva.html")

def login(request):
    return render(request, "login.html")

def esqueceuasenha(request):
    return render(request, "esqueceuasenha.html")

def cadastro(request):
    return render(request, "cadastro.html")

def perfil(request):
    return render(request, "perfil.html")