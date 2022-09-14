from django import forms
from .models import Student
from django.forms import ModelForm


class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ( 'name', 'gender', 'email', 'description', )

		labels = {
			'name': '',  
			'gender': '',    
			'email': '', 
			'description': '', 
			  
		}

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom et Prenom',}),  
			'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre',}), 
			'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Adresse Email',}),  
			'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description',}), 
			
		}