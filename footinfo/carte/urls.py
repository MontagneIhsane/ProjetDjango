from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_joueurs, name='liste_joueurs'),
    path('resigter/', views.register, name='register'),
    path('rechercher/', views.search_joueurs, name='search_joueurs'),

]
