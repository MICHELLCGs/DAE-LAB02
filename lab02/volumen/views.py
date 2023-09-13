from django.shortcuts import render
import math
def formulario_volumen(request):
    return render(request, 'volumen/formulario.html')
def calcular_volumen(request):
    volumen = None

    if request.method == 'POST':
        altura = float(request.POST['altura'])
        diametro = float(request.POST['diametro'])
        radio = diametro / 2
        volumen = math.pi * (radio ** 2) * altura

    return render(request, 'volumen/calculo.html', {'volumen': volumen})

