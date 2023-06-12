from django.shortcuts import render

# Views for partstr
# Create your views here.

from .models import Part

def pn_list(request, user_id):
    # partnumbers = Part.objects.all()
    partnumbers = Part.objects.filter(resp=user_id)

    return render(request,
                  'partstr/pn_list.html',
                  {'partnumbers':partnumbers})

def home(request):
    return render(request,
                  'partstr/home.html', {})