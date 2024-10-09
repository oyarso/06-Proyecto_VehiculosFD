from django import forms 
from .models import BoardsModel 
from django.core.validators import MaxValueValidator


class WidgetForm(forms.Form): 
    marca = forms.CharField() 
    modelo = forms.CharField(max_length = 100) 
    serialCarroceria = forms.IntegerField(validators = [MaxValueValidator(50)])
    
    serialMotor = forms.IntegerField(validators = [MaxValueValidator(50)])  
    categoria = forms.CharField()
    precio = forms.FloatField() 




class BoardsForm(forms.ModelForm): 
# specify the name of model to use 
    class Meta: 
        model = BoardsModel 
        fields = "__all__" 

