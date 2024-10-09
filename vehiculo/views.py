from django.http import HttpResponseRedirect 
from django.contrib.contenttypes.models import ContentType 
from tokenize import PseudoExtras 
from django.views.generic import TemplateView 
from django.shortcuts import render  

class IndexPageView(TemplateView): 
    template_name = "index.html"

    
def menuView(request): 
    template_name = 'menu.html' 
    return render(request, template_name) 





