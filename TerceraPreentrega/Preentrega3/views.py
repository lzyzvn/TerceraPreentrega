from django.shortcuts import render
from Preentrega3.models import ingresos, ahorros, gastos
from django.http import HttpResponse
def inicio(request):
    return render(request,'Preentrega3/index.html')
def ingresos(request):
    return render(request,'Preentrega3/ingresos.html')
def ahorros(request):
    return render(request,'Preentrega3/ahorros.html')
def gastos(request):
    return render(request,'Preentrega3/gastos.html')
def ingresosFormulario(request):
    if request.method=='POST':
        cantidad= ingresos(request.post['ingresos',(request.post['ingresos'])])
        cantidad.save()
        return render(request, "Preentrega3/ingresos.html")
    return render(request, "Preentrega3/ingresosformulario.html")
def ahorrosFormulario(request):
    if request.method=='POST':
        cantidad= ahorros(request.post['ahorros',(request.post['ahorros'])])
        cantidad.save()
        return render(request, "Preentrega3/ahorros.html")
    return render(request, "Preentrega3/ahorrosformulario.html")
def gastosFormulario(request):
    if request.method=='POST':
        cantidad= ingresos(request.post['gastos',(request.post['gastos'])])
        cantidad.save()
        return render(request, "Preentrega3/gastos.html")
    return render(request, "Preentrega3/gastosformulario.html")