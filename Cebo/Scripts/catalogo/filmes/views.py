from django.shortcuts import render
from .models import Filmes;

# Create your views here.
def lista_filmes(req):
    filmes = Filmes.objects.all();
    return render(req, 'filmes/index.html', {'filmes': filmes})