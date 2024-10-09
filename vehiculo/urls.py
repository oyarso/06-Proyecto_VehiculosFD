from django.urls import path
from django.urls import path
from .views import IndexPageView, menuView, boardsform_view, mostrar

urlpatterns = [ 
path('', IndexPageView.as_view(), name='index'), 
path('menu/',  menuView, name='menu'),
path('listar/',  mostrar, name='mostrar'), 
path('add/', boardsform_view, name='addform'), 
]


