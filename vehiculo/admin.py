from django.contrib import admin 
from .models import BoardsModel 
admin.site.site_header = 'Curso Django' 
admin.site.index_title = 'Panel de control Proyecto Django' 
admin.site.site_title = 'Administrador Django' 


class BoardsAdmin(admin.ModelAdmin): 
    readonly_fields = ('creado', 'modificado') 
    list_display = ('marca', 'modelo') 
    search_fields = ('marca', 'modelo') 
    ordering = ('marca', 'modelo') 
    list_filter = ('marca', 'modelo') 
 
admin.site.register(BoardsModel, BoardsAdmin)   