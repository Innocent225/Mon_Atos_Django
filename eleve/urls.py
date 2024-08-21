from django.urls import path
from . import views


urlpatterns = [
    path('dashboad/', views.dashboad_views, name='dashboad') ,
    path('eleve/', views.eleve_views, name='eleve'),
    path('professeurs/', views.professeurs_views, name='professeurs'),
    path('utilisateurs/', views.utilisateurs_views, name='utilisateurs'),
    path('rapport/', views.rapport_views, name='rapport'),
    path('index/', views.index_views, name='index'), # 
    path('ajout_eleve/', views.ajout_eleve_views, name='ajout_eleve'),
    path('modifier_eleve/', views.modifier_eleve_views, name='modifier_eleve'),
    path('modifier_prof/', views.modifier_prof_views, name='modifier_prof'),
    path('ajout_prof/', views.ajout_prof_views, name='ajout_prof'),
    path('ajout_utilisateur/', views.ajout_utilisateur_views, name='ajout_utilisateur'),
    path('modifier_utilisateur/', views.modifier_utilisateur_views, name='modifier_utilisateur'),
]