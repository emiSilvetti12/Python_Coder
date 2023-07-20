from django.shortcuts import render
from .forms import Clase1Form, Clase2Form, Clase3Form
from .models import Clase1, Clase2, Clase3

def insertar_datos(request):
    if request.method == 'POST':
        form1 = Clase1Form(request.POST)
        form2 = Clase2Form(request.POST)
        form3 = Clase3Form(request.POST)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            form1.save()
            form2.save()
            form3.save()
    else:
        form1 = Clase1Form()
        form2 = Clase2Form()
        form3 = Clase3Form()
    return render(request, 'insertar_datos.html', {'form1': form1, 'form2': form2, 'form3': form3})

def buscar_datos(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'buscar_datos.html')