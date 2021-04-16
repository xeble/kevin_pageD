from django.contrib import admin
from .models import *


class ClientesAdmin(admin.ModelAdmin):
    model = Clientes
    list_display = ("Nombre_y_Apellido", "Email" , "Telefono", "Atendido")

admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Modalidade)