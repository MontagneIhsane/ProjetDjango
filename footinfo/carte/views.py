from django.shortcuts import render, redirect
from django.db.models import Q 
from .models import Carte

def liste_joueurs(request):
    carte = Carte.objects.all()
    return render(request, 'carte/home.html', {'joueurs': carte})

from django.contrib.auth.models import User
from django.contrib.auth import login
from .form import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Crée l'utilisateur
            login(request, user)  # Connecte l'utilisateur automatiquement après l'inscription
            return redirect('liste_joueurs')  # Redirige vers la page souhaitée
    else:
        form = UserRegistrationForm()

    return render(request, 'register/register.html', {'form': form})

from django.shortcuts import render
from .models import Carte

def search_joueurs(request):
    query = request.GET.get('q', '')  # Récupérer la requête de recherche (vide par défaut)
    
    # Vérifier si une requête de recherche a été fournie
    if query:
        joueurs = Carte.objects.filter(nom__icontains=query)  # Recherche par nom
    else:
        joueurs = Carte.objects.all()  # Afficher tous les joueurs par défaut
    
    return render(request, 'search/result.html', {'joueurs': joueurs, 'query': query})


