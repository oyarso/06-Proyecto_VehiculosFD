from django.http import HttpResponseRedirect 
from tokenize import PseudoExtras 
from django.views.generic import TemplateView 
from django.shortcuts import render  
from .forms import WidgetForm, BoardsForm
from django.contrib import messages 
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import permission_required
from .models import BoardsModel
from .forms import WidgetForm, BoardsForm, RegistroUsuarioForm 
class IndexPageView(TemplateView): 
    template_name = "index.html"

def menuView(request): 
    template_name = 'menu.html' 
    return render(request, template_name) 

def mostrar(request):
    
    vehiculos = BoardsModel.objects.all()
    return render(request, 'mostrar.html', {'vehiculos': vehiculos}) 


def datosform_view(request): 
    context ={} 
    return render(request, "datosform.html", context) 


def boardsform_view(request): 
    context ={}  
    form = BoardsForm(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        form.save() 
        return HttpResponseRedirect('/')  
    context['form']= form 
    return render(request, "datosform.html", context) 

def widget_view(request): 
    context = {} 
    form = WidgetForm(request.POST or None) 
    context['form'] = form 
    return render(request, "widget_home.html", context) 

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}.")
                return HttpResponseRedirect('/menu')
            else:
                messages.error(request, "Invalido username o password.")
        else:
            messages.error(request, "Invalido username o password.")
    else:
        form = AuthenticationForm()
    
    return render(request=request, template_name="registration/login.html", context={"login_form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect('/menu')

def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrado Satisfactoriamente.")
            return HttpResponseRedirect('/menu')
        else:
            messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos.")
    else:
        form = RegistroUsuarioForm()
        
    return render(request=request, template_name="registration/registro.html", context={"register_form": form})
