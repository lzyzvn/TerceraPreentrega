from django import forms
class ingresosFormulario(forms.form):
    cantidad=forms.IntegerField()
class gastosFormulario(forms.form):
    cantidad=forms.IntegerField()
class ahorrosFormulario(forms.form):
    cantidad=forms.IntegerField()
