from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_joueurs, name='liste_joueurs'),
]
