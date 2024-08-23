from django.urls import path
from . import views


app_name="user"
urlpatterns = [
     path('', views.utilisateurs_views, name='utilisateurs'),
    path('ajout_utilisateur/', views.ajout_utilisateur_views, name='ajout_utilisateur'),
    path('modifier_utilisateur/', views.modifier_utilisateur_views, name='modifier_utilisateur'),
]