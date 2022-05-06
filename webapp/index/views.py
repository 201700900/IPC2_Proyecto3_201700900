import imp
from django.shortcuts import render, redirect
import requests
from django.http import HttpResponse
# Create your views here.
from django.http import HttpResponse
import xml.etree.ElementTree as ET


# def index (request):
#     return HttpResponse("Hello World")


def index(request):
    return render(request, 'index/index.html')


def generate_request(url, params={}):
    response = requests.post(url, params=params)

    if response.status_code == 200:
        return response.json()


def cargar(request):
    response = generate_request('http://127.0.0.1:5000/path/')
    if response:
        # print(response['entrada'])
        return render(request, 'index/index.html', {
            'entrada': response['entrada'],
            'respuesta': response['respuesta'],
            'exito': '¡CARGADO CON EXITO!'

        })

    return render(request, 'index/index.html', {'error': '¡ARCHIVO NO FUE CARGADO!'})


def getXML(request):
    text = ''
    if request.POST['entrada']:
        text = request.POST['entrada']
        root = ET.fromstring(text)

        # ET.indent(root)
        mydata = ET.tostring(root, encoding='UTF-8', method='html')
        myfile = open("carga.xml", "w", encoding='UTF-8')
        myfile.write(mydata.decode('UTF-8'))
        myfile.close()
        response = generate_request('http://127.0.0.1:5000/cargar/',  text)

        print(text)
        if response:
            # print(response['respuesta'])
            return render(request, 'index/index.html', {
                'entrada': text,
                'respuesta': response['respuesta'],
                'exito': '¡CARGADO CON EXITO!'

            })

    return render(request, 'index/index.html', {'error': '¡ARCHIVO NO FUE CARGADO!', 'entrada': text, })


def p(request):
    return render(request, 'index/prueba.html')


def prueba(request):
    text = ''
    if request.POST['entrada']:
        text = request.POST['entrada']
        root = ET.fromstring(text)

        # ET.indent(root)
        mydata = ET.tostring(root, encoding='UTF-8', method='html')
        myfile = open("carga.xml", "w", encoding='UTF-8')
        myfile.write(mydata.decode('UTF-8'))
        myfile.close()
        response = generate_request(
            'http://127.0.0.1:5000/prueba/',  text)

        print(text)
        if response:
            # print(response['respuesta'])
            return render(request, 'index/prueba.html', {
                'entrada': text,
                'respuesta': response['respuesta'],
                'exito': '¡MENSAJE CON EXITO!'

            })

    return render(request, 'index/prueba.html', {'error': '¡MENSAJE NO FUE CARGADO!', 'entrada': text, })

def pdf(request):
    response = generate_request('http://127.0.0.1:5000/pdf/')
    if response:
        # print(response['entrada'])
        return render(request, 'index/index.html', {'exito': '¡PDF CREADO CON EXITO!'})

    return render(request, 'index/index.html', {'error': '¡PDF NO CREADO!'})

def reset(request):
    response = generate_request('http://127.0.0.1:5000/reset/')
    if response:
        # print(response['entrada'])
        return render(request, 'index/index.html', {'exito': '¡DATABASE ELIMINADA CON EXITO!'})

    return render(request, 'index/index.html', {'error': '¡ERROR EN RESET DATABASE!'})


def perfil(request):
    return render(request, 'index/perfil.html')

def doc(request):
    response = generate_request('http://127.0.0.1:5000/doc/')
    if response:
        # print(response['entrada'])
        return render(request, 'index/index.html', {'exito': '¡PDF CREADO CON EXITO!'})

    return render(request, 'index/index.html', {'error': '¡PDF NO CREADO!'})



def reportes(request):
    if request.method == 'GET':
        # response = generate_request('http://127.0.0.1:5000/reportes/by_date')
        # print(type(response['fechas']))
       
        date = request.GET.get('date', None)
        empresa = request.GET.get('empresa', None)
        
        if date != None:
            n = date.split('-')
            fecha = n[2]+'/'+n[1]+'/'+n[0]
            response = generate_request('http://127.0.0.1:5000/reportes/by_date', {'fecha': fecha})

        # if date != None:
        #     response = generate_request('http://127.0.0.1:5000/reportes/by_empresa')

        

    return render(request, 'index/reportes.html',  {'exito': 'exito'})
# def reports(request):
#     if request.method == 'GET':
#         date = request.GET.get('date', None)
#         error = request.GET.get('error', None)

#         context: dict = {}
#         if date != None:
#             users_by_date = requests.get('http://localhost:5000/stats/by_date',
#                                          {
#                                              'date': date
#                                          }).json()

#             context['date_results']: list = []
#             for user in users_by_date['data']:
#                 percentage = int((user['cant'] / users_by_date['total']) * 100)
#                 context['date_results'].append({
#                     'percentage': percentage,
#                     'user': user['user'],
#                     'cant': user['cant'],
#                     'total': users_by_date['total']
#                 })
#         if error != None:
#             errors_by_date = requests.get(
#                 'http://localhost:5000/stats/by_error', {
#                     'error': error
#                 }).json()

#             context['error_results']: list = []
#             for date in errors_by_date['data']:
#                 percentage = int(
#                     (date['cant'] / errors_by_date['total']) * 100)
#                 context['error_results'].append({
#                     'percentage':
#                     percentage,
#                     'date':
#                     date['date'],
#                     'cant':
#                     date['cant'],
#                     'total':
#                     errors_by_date['total']
#                 })
#         return render(request, 'reports.html', context)