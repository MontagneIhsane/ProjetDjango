from django.shortcuts import render
from .models import Carte

def liste_joueurs(request):

    carte = Carte.objects.all()
    return render(request, 'carte/home.html', {'joueurs': carte})
