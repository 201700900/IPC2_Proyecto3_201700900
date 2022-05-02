import imp
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def index (request):
#     return HttpResponse("Hello World")

def index(request):



	return render(request, 'index/index.html')
