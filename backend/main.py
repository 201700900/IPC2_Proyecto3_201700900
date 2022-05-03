from flask import Flask, render_template, request, json, jsonify, make_response, redirect
import xml.etree.ElementTree as ET
import xmltodict
from markupsafe import escape
from clases import escribir, cargar
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    user_ip = request.remote_addr
    return f"Hola Mundo flask hellos, la IP es: {user_ip}"


@app.route('/cargar', methods=['GET', 'POST'], strict_slashes=False)
def carga():
    path = xmltodict.parse(request.get_data())
    b = request.get_data()
    s = b.decode('UTF-8')
    # print(type(b))
    # print(type(s))
    root = ET.fromstring(s)
    # print(root)
    # print(type(root))
    cargar.leer(root)
    # cargar.leer()
    # print()
    return escribir.respuesta()


@app.route('/path/', methods=['GET', 'POST'], strict_slashes=False)
def path():
    cargar.getPath()
    return escribir.respuesta()


@app.route('/posting' , methods=['POST'])
def add_pub():
    #parametros
    nombre = request.json['nombre']
    curso = request.json['curso']
    lista = request.json['lista']
    print(lista)
    msg = 'Hola mi nombre es ' + nombre +', bienvenido al curso de ' + curso
    print(msg)
    return jsonify(Name = 'POST', Mensaje= msg, Status=True),200



if __name__ == '__main__':
    app.run(debug=True)

#Inicializar application
#python app.py