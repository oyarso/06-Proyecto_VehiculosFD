from django.db import models 

class BoardsModel(models.Model): 
    FIAT = 'Fiat'
    CHEVROLET = 'Chevrolet'
    FORD = 'Ford' 
    TOYOTA = 'Toyota'

    PARTICULAR = 'Particular'
    TRANSPORTE = 'Transporte'
    CARGA = 'Carga'

    ChoicesMarca=(
        (FIAT,'Fiat'),
        (CHEVROLET,'Chevrolet'),
        (FORD,'Ford'),
        (TOYOTA,'Toyota'),
    )
    ChoicesCategoria=(
        (PARTICULAR,'Particular'),
        (TRANSPORTE,'Transporte'),
        (CARGA,'Carga'),
    )
    marca  = models.CharField(max_length = 20, choices=ChoicesMarca, default="FIAT")
    modelo = models.CharField(max_length = 100)      
    serialCarroceria = models.CharField(max_length = 50)   
    serialMotor = models.CharField(max_length = 50)  
    categoria = models.CharField(max_length = 20, choices=ChoicesCategoria, default="PARTICULAR")
    precio = models.FloatField() 
    creado = models.DateTimeField(auto_now_add=True) 
    modificado = models.DateTimeField(auto_now = True)  

    class Meta: 
        verbose_name = "vehiculo" 
        verbose_name_plural = "vehiculos" 
        ordering = ["-creado"]         
        permissions = ( 
            ("es_miembro_1", "Es miembro con prioridad 1"), 
        )             

def __str__(self): 
    return self.autor 

