from flask import Flask, render_template, request, json, jsonify, make_response, redirect
import xml.etree.ElementTree as ET
import xmltodict
from markupsafe import escape
import webbrowser as wb
from clases import escribir, cargar, pfd, db

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
    
    return {'respuesta':escribir.respuesta()}


@app.route('/path/', methods=['GET', 'POST'], strict_slashes=False)
def path():
    cargar.getPath()
    return {"respuesta": escribir.respuesta(), "entrada": cargar.text}

@app.route('/pdf/', methods=['GET', 'POST'], strict_slashes=False)
def pdf():
    pfd.makePDF()
    wb.open_new('C:/Users/gujho/OneDrive/Documentos/1SEM2022/IPC2/LAB/IPC2_Proyecto3_201700900/backend/reporte.pdf')   
    return {'exito':''}

@app.route('/prueba' , methods=['GET','POST'], strict_slashes=False)
def prueba():
    path = 'C:/Users/gujho/OneDrive/Documentos/1SEM2022/IPC2/LAB/IPC2_Proyecto3_201700900/webapp/carga.xml'
    tree = ET.parse(path)
    root = tree.getroot()
    
    return {'respuesta':escribir.prueba_mensaje(root)}



if __name__ == '__main__':
    app.run(debug=True)

#Inicializar application
#python app.py

@app.route('/reset/', methods=['GET', 'POST'], strict_slashes=False)
def reset():
    n = db.DB()
    n.reset()
    return {'exito':''}