from django.http import HttpResponseRedirect 
from django.contrib.contenttypes.models import ContentType 
from tokenize import PseudoExtras 
from django.views.generic import TemplateView 
from django.shortcuts import render  
from .forms import WidgetForm, BoardsForm

from .models import BoardsModel

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

