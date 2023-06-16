from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Part
from .forms import PartCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def loginPage(request):

    # Recibe username y password del formulario
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #Chequea que el usuario exista
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'El usuario no existe!')

        #Verifica que las credenciales sean correctas
        user = authenticate(request, username=username, password=password)

        #Si existe lo enviamos al home
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'password incorrecto!')

    context = {}
    return render(request, 'partstr/login_register.html', context)

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

def partdelete(request, pk):
    part = Part.objects.get(id=pk)
    if request.method == 'POST':
        part.delete()
        return redirect('home')
    return render(request, 'partstr/delete.html', {'obj':part})