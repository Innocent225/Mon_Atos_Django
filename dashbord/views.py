from django.shortcuts import render


# Create your views here.
def index_views(request):
    return render(request, 'dashbord/index.html/')

def dashboad_views(request):
    return render(request, 'dashbord/dashboad.html/')