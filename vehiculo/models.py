from django.db import models 
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import Permission, User

class BoardsModel(models.Model): 
    FORD = 'Ford' 
    FIAT = 'Fiat'
    CHEVROLET = 'Chevrolet'
    TOYOTA = 'Toyota'

    PARTICULAR = 'Particular'
    TRANSPORTE = 'Transporte'
    CARGA = 'Carga'

    ChoicesMarca=(        
        (FORD,'Ford'),
        (FIAT,'Fiat'),
        (CHEVROLET,'Chevrolet'),
        (TOYOTA,'Toyota'),
    )
    ChoicesCategoria=(
        (PARTICULAR,'Particular'),
        (TRANSPORTE,'Transporte'),
        (CARGA,'Carga'),
    )
    marca  = models.CharField(max_length = 20, choices=ChoicesMarca, default="FORD")
    modelo = models.CharField(max_length = 100)      
    serialCarroceria = models.IntegerField(validators = [MaxValueValidator(50)]) 
    serialMotor = models.IntegerField(validators = [MaxValueValidator(50)])  
    categoria = models.CharField(max_length = 20, choices=ChoicesCategoria, default="PARTICULAR")
    precio = models.FloatField() 
    creado = models.DateTimeField(auto_now_add=True) 
    modificado = models.DateTimeField(auto_now = True)  

    class Meta: 
        verbose_name = "vehiculo" 
        verbose_name_plural = "vehiculos" 
        ordering = ["-creado"]         
        permissions = ( 
            ("visualizar_catalogo", "Can view vehiculo"), 
            ("add_vehiculomodel", "Can view vehiculo"), 
        )             

def __str__(self): 
    return self.autor 

