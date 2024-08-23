from django.shortcuts import render
from .forms import TeacherForm

# Create your views here.

def professeurs_views(request):
    return render(request, 'teacher/professeurs.html/')

def ajout_prof_views(request):
    form = TeacherForm()
    context = {'form':form}
    return render(request, 'teacher/ajout_prof.html/', context)


def modifier_prof_views(request):
    form = TeacherForm()
    context = {'form':form}
    return render(request, 'teacher/modifier_prof.html/', context)
