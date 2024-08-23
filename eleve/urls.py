from django.urls import path
from . import views

app_name="eleve"
urlpatterns = [
    path('', views.eleve_views, name='eleve1'),
    path('ajout_eleve/', views.ajout_eleve_views, name='ajout_eleve'),
    path('modifier_eleve/', views.modifier_eleve_views, name='modifier_eleve'),
]