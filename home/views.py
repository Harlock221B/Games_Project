from django.shortcuts import render
from .models import Games

def index(request):
    dados = Games.objects.all().filter(
        mostrar=True
    )
    return render(request,'home/index.html',{'dados':dados})

def mostrar(request, idbusca):
    dados = Games.objects.get(id=idbusca)
    return render(request, 'home/detailGame.html',{'dados':dados})

