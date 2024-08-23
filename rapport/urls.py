from django.urls import path
from . import views

app_name="rapport"
urlpatterns = [
    path('', views.rapport_views, name='rapport1'),
] 