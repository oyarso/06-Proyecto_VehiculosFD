from django import forms 
from .models import BoardsModel 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class WidgetForm(forms.Form): 
    marca = forms.CharField() 
    modelo = forms.CharField(max_length = 100) 
    serialCarroceria = forms.CharField(max_length = 50) 
    
    serialMotor = forms.CharField(max_length = 50) 
    categoria = forms.CharField()
    precio = forms.FloatField() 


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super(RegistroUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class BoardsForm(forms.ModelForm): 
# specify the name of model to use 
    class Meta: 
        model = BoardsModel 
        fields = "__all__" 

