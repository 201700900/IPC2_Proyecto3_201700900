from flask import Flask, render_template, request, json, jsonify, make_response, redirect
import xmltodict
from markupsafe import escape
from clases import escribir, cargar
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    user_ip = request.remote_addr
    return f"Hola Mundo flask hellos, la IP es: {user_ip}"

def do_the_login():
    return('login')

def show_the_login_form():
    return('show')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


@app.route('/cargar/<path>', methods=['GET', 'POST'])
def carga(path):
    cargar.leer()
    print(path)
    return escribir.respuesta()


@app.route('/pro/', methods=['GET', 'POST'])
def projects():
    nombre = request.json['path']
    msg= 'El archivo esta en ' +  nombre
    print(msg)
    cargar.leer()
    return escribir.respuesta()

@app.route('/about')
def about():
    return 'The about page'

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