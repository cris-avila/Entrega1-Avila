from django import forms

class FormBodys(forms.Form):
    marca=forms.CharField(max_length=30)
    modelo=forms.CharField(max_length=30)
    color=forms.CharField(max_length=30)
    talle=forms.CharField(max_length=30)
    precio=forms.IntegerField()
    
class FormPantalones(forms.Form):
    marca=forms.CharField(max_length=30)
    modelo=forms.CharField(max_length=30)
    color=forms.CharField(max_length=30)
    talle=forms.CharField(max_length=30)
    precio=forms.IntegerField()
    
class FormRemeras(forms.Form):
    marca=forms.CharField(max_length=30)
    modelo=forms.CharField(max_length=30)
    color=forms.CharField(max_length=30)
    talle=forms.CharField(max_length=30)
    precio=forms.IntegerField()