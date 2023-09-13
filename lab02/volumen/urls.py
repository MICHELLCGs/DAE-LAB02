from django.urls import path
from . import views
app_name = 'volumen'

urlpatterns = [
    path('', views.formulario_volumen, name='formulario_volumen'),
    path('calcular/', views.calcular_volumen, name='calcular_volumen'),
]
