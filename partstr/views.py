from django.shortcuts import render, redirect
from .models import Part
from .forms import PartCreateForm

def partlist(request, user_id):
    # partnumbers = Part.objects.all()
    partnumbers = Part.objects.filter(resp=user_id)

    return render(request,
                  'partstr/partlist.html',
                  {'partnumbers':partnumbers})

def home(request):
    return render(request,
                  'partstr/home.html', {})

def partcreate(request):
    form = PartCreateForm()
    if request.method == 'POST':
        form = PartCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'partstr/partcreate.html', context)

def partupdate(request, pk):
    part = Part.objects.get(id=pk) #Asignamos una parte (mediante su id) a la variable "part"
    form = PartCreateForm(instance=part) # Al usar instance, llenamos el form con el objeto part

    if request.method == 'POST':
        form = PartCreateForm(request.POST, instance=part)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'partstr/partcreate.html', context)