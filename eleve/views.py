from django.shortcuts import render
from .forms import StudentForm


# Create your views here.

def eleve_views(request):
    context = {
        'nom':"IRIE",
        'prenom':"Innocent",
    }
    return render(request, 'eleve/eleve1.html/', context)

def ajout_eleve_views(request):
    form = StudentForm()
    context = {'form':form}
    return render(request, 'eleve/ajout_eleve.html/', context)

def modifier_eleve_views(request):
    form = StudentForm()
    context = {'form':form}
    return render(request, 'eleve/modifier_eleve.html/', context)
