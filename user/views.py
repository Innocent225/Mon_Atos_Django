from django.shortcuts import render
from .forms import UserForm
from .forms import UserAdd

# Create your views here.

def utilisateurs_views(request):
    return render(request, 'user/utilisateurs.html/')


def ajout_utilisateur_views(request):
    form = UserAdd()
    context = {'form':form}
    return render(request, 'user/ajout_utilisateur.html/', context)


def modifier_utilisateur_views(request):
    form = UserForm()
    context = {'form':form}
    return render(request, 'user/modifier_utilisateur.html/', context)