from django.shortcuts import render
from django.http import HttpResponse


def home (request):
	return HttpResponse('Lucas Lucarelli')


def cliente(request):
	data={}
	data['djangomoc']='vamos ver se da certo'
	return render (request, 'cliente.html', data)
