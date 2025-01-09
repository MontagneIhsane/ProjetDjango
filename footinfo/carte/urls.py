from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.liste_joueurs, name='liste_joueurs'),
    path('resigter/', views.register, name='register'),
    path('rechercher/', views.search_joueurs, name='search_joueurs'),
    path('login/', LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


]
