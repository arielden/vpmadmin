from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required #permite retringir acceso a las págs.
from .models import Part, Level, Status, PnType
from .forms import PartCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

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
def partlist(request):

    #Tomar 'q' y 'u' de la url
    p = request.GET.get('p') if request.GET.get('p') != None else '0'
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    u = request.GET.get('u') if request.GET.get('u') != None else ''

    allstatus = Status.objects.all()

    # Traer las partes correspondientes a usuario pasado como parámetro
    # y aplicar también filtro por 'status' usando variable 'q'
    partnumbers = Part.objects.filter(
        # User método Q para multiples queries.
        Q(partnumber__startswith=p) &
        Q(status__name__icontains=q)&
        Q(resp__username__icontains=u) 
    )

    partnumbers_count = partnumbers.count()

    context = {'partnumbers':partnumbers,
               'partnumbers_count':partnumbers_count,
               'allstatus':allstatus,
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
        return render(request, 'partstr/partreadonly.html', context)
    
    if request.method == 'POST':
        form = PartCreateForm(request.POST, instance=part)
        if form.is_valid():
            form.save()
            msg = messages.success(request, f'{part.partnumber} se actualizó correctamente!')
            print(msg)
            return redirect('partstr:partlist')
    
    return render(request, 'partstr/partupdate.html', context)

@login_required(login_url='partstr:login')
def partdelete(request, pk):
    part = Part.objects.get(id=pk)
    if request.method == 'POST':
        part.delete()
        print("Parte eliminada")
        return redirect('partstr:partlist')
    return render(request, 'partstr/delete.html', {'obj':part})

def structure(request):
    assyparts = Part.objects.filter(pntype=2)
    rootnode = Part.objects.get(level=1)

    context = {'rootnode':rootnode}
    return render(request, 'partstr/structure.html', context)

@login_required(login_url='partstr:login')
def catiaload(request, pk):
    part = Part.objects.get(id=pk)

    partType = part.pntype

    context = {'part':part, 'partType':partType}
    return render(request, 'partstr/catiaload.html', context)