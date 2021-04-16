from django.forms import ModelForm
from .models import Clientes

class ClientesForm(ModelForm):
	class Meta:
		model = Clientes
		fields = ("Nombre_y_Apellido", "Email", "Telefono", "Mensaje")