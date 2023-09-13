from django.shortcuts import render, redirect
from .models import Operacion

def calcular(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operacion = request.POST['operacion']
        resultado = None

        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        elif operacion == 'multiplicacion':
            resultado = num1 * num2

        operacion_obj = Operacion(num1=num1, num2=num2, operacion=operacion, resultado=resultado)
        operacion_obj.save()
        return redirect('resultado')
    else:
        return render(request, 'operaciones/calcular.html')

def resultado(request):
    operaciones = Operacion.objects.all()
    return render(request, 'operaciones/resultado.html', {'operaciones': operaciones})
