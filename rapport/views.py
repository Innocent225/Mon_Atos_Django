from django.shortcuts import render

# Create your views here.

def rapport_views(request):
    return render(request, 'rapport/rapport1.html/')