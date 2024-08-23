from django.urls import path
from . import views

app_name="dashbord"
urlpatterns = [
    path('index/', views.index_views, name='index'),
    path('', views.dashboad_views, name='dashboad') ,
]