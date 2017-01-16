from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from django.http import HttpResponseRedirect
from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
	CHOICES = (('Dogs', 'Dogs'),('Cats', 'Cats'),)
	animal = forms.ChoiceField(choices=CHOICES, required=True )
	class Meta:
		model = Person
		fields = ['name', 'favorite_color','animal']
		widgets ={
		'name': forms.TextInput(attrs={'placeholder': 'name'}),
		'favorite_color': forms.TextInput(attrs={'placeholder': 'Favorite color'}),
		}

def person_list(request, template_name='ormuco/modelman_list.html'):
	Persons = Person.objects.all()
	data = {}
	data['object_list'] = Persons
	return render(request, template_name, data)

def person_create(request, template_name='ormuco/modelman_form.html'):
	form = PersonForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/ormuco")
	return render(request, template_name, {'form':form})

# class Meta:
#         model = Person
#         CHOICES = (('Cats', 'Dogs'),('Cats', 'Dogs'),)
#         fields = ['name', 'favorite_color','animal']