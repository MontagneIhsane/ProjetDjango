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
            user = form.save()
            login(request, user)  
            return redirect('liste_joueurs')  
    else:
        form = UserRegistrationForm()

    return render(request, 'register/register.html', {'form': form})

def search_joueurs(request):
    query = request.GET.get('q', '')  

    if query:
        joueurs = Carte.objects.filter(
            Q(nom__icontains=query) | Q(poste__icontains=query)  
        )
    else:
        joueurs = Carte.objects.all()  

    return render(request, 'search/result.html', {'joueurs': joueurs, 'query': query})

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
