#log/forms.py
# -*- coding: utf-8 -*- 

from django.contrib.auth.forms import AuthenticationForm
from .models import Perfil, Sexo, User
from django import forms

class LoginForm(AuthenticationForm):
	username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder':'Usuario', 'required':''}))
	password = forms.CharField(label="Password", max_length=30, widget=forms.TextInput(attrs={'type':'password','class': 'form-control', 'name': 'password', 'placeholder':'Contraseña', 'required':''}))

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'date_joined')
		labels = {
			'first_name': 'Nombres',
			'last_name': 'Apellidos',
			'email': 'Email',
		}
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control', 'id':'username', 'name': 'username', 'placeholder':'Nombre de Usuario'}),
			'first_name': forms.TextInput(attrs={'class': 'form-control', 'id':'first_name', 'name': 'first_name', 'placeholder':'Nombres'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control', 'id':'last_name', 'name': 'last_name', 'placeholder':'Apellidos'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', 'id':'email', 'name': 'email', 'placeholder':'Email'}),
			'date_joined': forms.DateInput(attrs={'class': 'form-control', 'id':'date_joined', 'name': 'date_joined', 'placeholder':'Fecha De Ingreso'}),
		}

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Perfil
		fields = ('emails', 'fecha_de_nac', 'image')
		labels = {
			'fecha_de_nac': 'Fecha de Nacimiento',
			'image': 'Imagen de Perfil'
		}
		widgets = {
			#'email': FormListField(),
			'fecha_de_nac': forms.TextInput(attrs={'class': 'date-picker form-control col-md-7 col-xs-12'}),
			'image': forms.FileInput(attrs={'class': 'form-control'})
		}

		
