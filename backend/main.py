from flask import Flask, render_template, request, json, jsonify, make_response, redirect
import xml.etree.ElementTree as ET
import xmltodict
from markupsafe import escape
from clases import escribir, cargar, pfd
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    user_ip = request.remote_addr
    return f"Hola Mundo flask hellos, la IP es: {user_ip}"


@app.route('/cargar', methods=['GET', 'POST'], strict_slashes=False)
def carga():
    # path = xmltodict.parse(request.get_data())
    path = 'C:/Users/gujho/OneDrive/Documentos/1SEM2022/IPC2/LAB/IPC2_Proyecto3_201700900/webapp/carga.xml'
    tree = ET.parse(path)
    root = tree.getroot()
    cargar.leer(root)
    pfd.makePDF()
    
    return {'respuesta':escribir.respuesta()}


@app.route('/path/', methods=['GET', 'POST'], strict_slashes=False)
def path():
    cargar.getPath()
    return {"respuesta": escribir.respuesta(), "entrada": cargar.text}


@app.route('/prueba' , methods=['GET','POST'], strict_slashes=False)
def prueba():
    b = request.get_data()
    s = b.decode('UTF-8')
 
    root = ET.fromstring(s)
    
    return {'respuesta':escribir.prueba_mensaje(root)}



if __name__ == '__main__':
    app.run(debug=True)

#Inicializar application
#python app.py