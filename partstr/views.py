from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required #permite retringir acceso a las págs.
from .models import Part
from .forms import PartCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def loginPage(request):

    # Si el usuario está logueado, redirecciona al home
    if request.user.is_authenticated: 
        return redirect('partstr:home')

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
            messages.error(request, "Revise sus credenciales")

    context = {}
    return render(request, 'partstr/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='partstr:login') #el decorator restringe el acceso si no encuentra usuario autenticado
def partlist(request, user_id):
    # partnumbers = Part.objects.all()

    """
    Le voy a agregar un condicional para filtrar las partes del usuario,
    o si se ingresa -1, muestra todas las partes creadas.
    """

    if user_id != -1:
        partnumbers = Part.objects.filter(resp=user_id)
        user = -1
    else:
        partnumbers = Part.objects.all()
        user = User.objects(id=user_id)

    context = {'partnumbers':partnumbers, 'user':user}

    return render(request,
                  'partstr/partlist.html',
                  {'partnumbers':partnumbers})

def home(request):
    return render(request,
                  'partstr/home.html', {})

@login_required(login_url='partstr:login')
def partcreate(request):
    form = PartCreateForm()
    if request.method == 'POST':
        form = PartCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'partstr/partcreate.html', context) 

@login_required(login_url='partstr:login')
def partupdate(request, pk):
    part = Part.objects.get(id=pk) #Asignamos una parte (mediante su id) a la variable "part"
    form = PartCreateForm(instance=part) # Al usar instance, llenamos el form con el objeto part

    #Se encarga de validar que el usuario que accede a esta vista sea quien creó el contenido.
    if request.user != part.resp:
        return HttpResponse('Acceso no permitido')
    
    if request.method == 'POST':
        form = PartCreateForm(request.POST, instance=part)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'partstr/partcreate.html', context)

@login_required(login_url='partstr:login')
def partdelete(request, pk):
    part = Part.objects.get(id=pk)
    if request.method == 'POST':
        part.delete()
        return redirect('home')
    return render(request, 'partstr/delete.html', {'obj':part})