from django.shortcuts import render

# Views for partstr
# Create your views here.

from .models import Part

def partnumber_list(request):
    partnumbers = Part.objects.all()

    return render(request,
                  'partstr/pn_list.html',
                  {'partnumbers':partnumbers})