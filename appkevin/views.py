from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ClientesForm
from django.contrib import messages
 

def index(request):
    form = ClientesForm()
    if request.method == 'POST':
        form = ClientesForm(request.POST)
        subject=request.POST["Email"]
        message=request.POST["Mensaje"] + " " + request.POST["Nombre_y_Apellido"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["Correodepruba987@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensaje Enviado")
    
    context = {'form':form}
    return render(request, 'index.html', context)