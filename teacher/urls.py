from django.urls import path
from . import views

app_name="teacher"
urlpatterns = [
    path('', views.professeurs_views, name='professeurs'),
    path('modifier_prof/', views.modifier_prof_views, name='modifier_prof'),
    path('ajout_prof/', views.ajout_prof_views, name='ajout_prof'),
]