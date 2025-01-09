from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q 
from .models import Carte, Note

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

def search_joueurs(request):
    query = request.GET.get('q', '')  # Récupérer la requête de recherche (vide par défaut)

    # Vérifier si une requête de recherche a été fournie
    if query:
        joueurs = Carte.objects.filter(
            Q(nom__icontains=query) | Q(poste__icontains=query)  # Recherche par nom ou par poste
        )
    else:
        joueurs = Carte.objects.all()  # Afficher tous les joueurs par défaut

    return render(request, 'search/result.html', {'joueurs': joueurs, 'query': query})

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
