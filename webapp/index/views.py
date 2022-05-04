import imp
from django.shortcuts import render
import requests

# Create your views here.
from django.http import HttpResponse

# def index (request):
#     return HttpResponse("Hello World")

def index(request):
	return render(request, 'index/index.html')

def getXML(params={}):
	response = requests.get('http://127.0.0.1:5000/path/', auth=('user', 'pass'))#generate_request('http://127.0.0.1:5000/path/', params)
	if response:
		user = response.get('results')[0]
		return user.get('name').get('first')
		
	return

def cargar(request):
	return