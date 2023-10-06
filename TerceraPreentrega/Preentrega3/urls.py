from django.urls import path
from Preentrega3 import views

urlpatterns = [
    path('', views.inicio),
    path('ahorros', views.ahorros, name='ahorros'),
    path('ingresos', views.ingresos, name='ingresos'),
    path('gastos', views.gastos, name='gastos'),
    path('gastos', views.gastosFormulario, ),
    path('ingresos', views.ahorrosFormulario, ),
    path('ahorros', views.ingresosFormulario ),

]
