from django.contrib import admin
from .models import ingresos, ahorros, gastos
# Register your models here.
admin.site.register(ingresos)
admin.site.register(ahorros)
admin.site.register(gastos)