from django.urls import path
from .views import IndexPageView, menuView, boardsform_view, mostrar, logout_view, login_view, registro_view

urlpatterns = [ 
path('', IndexPageView.as_view(), name='index'), 
path('menu/',  menuView, name='menu'),
path('listar/',  mostrar, name='mostrar'), 
path('add/', boardsform_view, name='addform'), 
path('logout/', logout_view, name="logout"), 
path('login/', login_view, name="login"), 
path('registro/', registro_view, name="registro"),
]


