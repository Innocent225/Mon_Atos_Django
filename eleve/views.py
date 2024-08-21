from django.shortcuts import render


# Create your views here.

def eleve_views(request):
    return render(request, 'eleve/eleve.html/')

def dashboad_views(request):
    return render(request, 'eleve/dashboad.html/')

def professeurs_views(request):
    return render(request, 'eleve/professeurs.html/')

def utilisateurs_views(request):
    return render(request, 'eleve/utilisateurs.html/')

def rapport_views(request):
    return render(request, 'eleve/rapport.html/')

def index_views(request):
    return render(request, 'eleve/index.html/')

def ajout_eleve_views(request):
    return render(request, 'eleve/ajout_eleve.html/')

def ajout_prof_views(request):
    return render(request, 'eleve/ajout_prof.html/')

def ajout_utilisateur_views(request):
    return render(request, 'eleve/ajout_utilisateur.html/')

def modifier_eleve_views(request):
    return render(request, 'eleve/modifier_eleve.html/')

def modifier_prof_views(request):
    return render(request, 'eleve/modifier_prof.html/')

def modifier_utilisateur_views(request):
    return render(request, 'eleve/modifier_utilisateur.html/')