from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required #permite retringir acceso a las págs.
from .models import Part, Level, Status, PnType
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

    if user_id == request.user.id:
        partnumbers = Part.objects.filter(resp=user_id)
        user = User.objects.get(id=user_id)
    elif user_id == 0:
        partnumbers = Part.objects.all()
        user = user_id
    else:
        partnumbers = None
        user = None

    partnumbers_count = partnumbers.count()

    context = {'partnumbers':partnumbers,
               'user':user,
               'partnumbers_count':partnumbers_count,
               }

    return render(request,
                  'partstr/partlist.html',
                  context)

def home(request):
    return render(request,
                  'partstr/home.html', {})

@login_required(login_url='partstr:login')
def partcreate(request):
    form = PartCreateForm()
    if request.method == 'POST':
        form = PartCreateForm(request.POST)
        if form.is_valid():
            part = form.save(commit=False)
            part.resp = request.user
            part.save()
            return redirect('home')
        print(form.errors) #Si hay errores, los imprime en la terminal.

    levels = Level.objects.all()
    status = Status.objects.all()
    pntypes = PnType.objects.all()
    assemblies = Part.objects.filter(pntype=2) #Devuelve conjuntos solamente. (filtra por id de conjunto)

    context = {'form':form, 'levels':levels,
               'status':status, 'pntypes':pntypes,
               'assemblies':assemblies}

    return render(request, 'partstr/partcreate.html', context) 

@login_required(login_url='partstr:login')
def partupdate(request, pk):
    part = Part.objects.get(id=pk) #Asignamos una parte (mediante su id) a la variable "part"
    form = PartCreateForm(instance=part) # Al usar instance, llenamos el form con el objeto part

    levels = Level.objects.all()
    status = Status.objects.all()
    pntypes = PnType.objects.all()
    assemblies = Part.objects.filter(pntype=2) #Devuelve conjuntos solamente. (filtra por id de conjunto)

    context = {'form': form, 'part':part,
               'levels':levels, 'status':status,
               'pntypes':pntypes, 'assemblies':assemblies}
    
    #Si no es el propietario de la parte, muestra el form "readonly".
    if request.user != part.resp:
        # return HttpResponse('Acceso no permitido')
        return render(request, 'partstr/partreadonly.html', context)
    
    if request.method == 'POST':
        form = PartCreateForm(request.POST, instance=part)
        if form.is_valid():
            form.save()
            return redirect('partstr:partlist', user_id=request.user.id)
        
    
    return render(request, 'partstr/partupdate.html', context)

@login_required(login_url='partstr:login')
def partdelete(request, pk):
    print(f"Entrando a partdelete con pk={pk}")
    part = Part.objects.get(id=pk)
    print(f"Parte a eliminar: {part}")
    if request.method == 'POST':
        part.delete()
        print("Parte eliminada")
        return redirect('partstr:partlist', user_id=request.user.id)
    return render(request, 'partstr/delete.html', {'obj':part})