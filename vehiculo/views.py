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


# def registro_view(request): 
#     if request.method == "POST": 
#         form = RegistroUsuarioForm(request.POST) 
#         if form.is_valid(): 
#             user = form.save() 
#             content_type = ContentType.objects.get_for_model(BoardsModel) 
            
#             es_miembro_1 = Permission.objects.get( 
#                 codename='es_miembro_1', 
#                 content_type=content_type 
#             )                  
            
#             add_boards = Permission.objects.get( 
#                 codename='add_boardsmodel', 
#                 content_type=content_type 
#             ) 
            
#             view_boards = Permission.objects.get( 
#                 codename='view_boardsmodel', 
#                 content_type=content_type 
#             ) 
            
#            # Agregamos el permisos al usuario 
#             user.user_permissions.add(es_miembro_1, add_boards, view_boards) 
#             user.is_staff = True 
#             user.save() 
#             login(request, user) 
#             messages.success(request, "Registrado Satisfactoriamente.") 
#             return HttpResponseRedirect ('/menu') 
#         messages.error(request, "Registro invalido. Algunos datos son incorrectos.") 
#     form = RegistroUsuarioForm() 
#     return render (request= request, template_name="registration/registro.html", context={"register_form":form}) 
