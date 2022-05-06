from flask import Flask, render_template, request, json, jsonify, make_response, redirect
import xml.etree.ElementTree as ET
import xmltodict
import pandas as pd 
import matplotlib.pyplot as plt 
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

@app.route('/reset/', methods=['GET', 'POST'], strict_slashes=False)
def reset():
    n = db.DB()
    n.reset()
    escribir.delete()
    return {'exito':''}

@app.route('/doc/', methods=['GET', 'POST'], strict_slashes=False)
def doc():
    pfd.makePDF()
    wb.open_new('C:/Users/gujho/OneDrive/Documentos/1SEM2022/IPC2/LAB/IPC2_Proyecto3_201700900/DOC/IPC2_Proyecto3_201700900.pdf')   
    return {'exito':''}

@app.route('/reportes/', methods=['GET', 'POST'], strict_slashes=False)
def reportes():
    escribir.cargar_fechas()
    fecha = request.args.get('date')
    print(fecha)
    empresas=[]
    sentimientos={
        "Positivo":[],
        "Negativo":[],
        "Neutro":[],
    }
    for f in escribir.ListaFechas():
        if f.fecha == fecha:
            for s in f.d_empresas:
                empresas.append(s['servicio'])
                sentimientos['Positivo'].append(s['pos'])
                sentimientos['Negativo'].append(s['neg'])
                sentimientos['Neutro'].append(s['neut'])



    # data=[["Rudra",23,156,70],
    #     ["Nayan",20,136,60],
    #     ["Alok",15,100,35],
    #     ["Prince",30,150,85]
    #     ]

    df=pd.DataFrame(sentimientos,index=empresas)

    df.plot(kind="bar",stacked=True,figsize=(10,8))
    plt.legend(loc="lower left",bbox_to_anchor=(0.8,1.0))
    # plt.show()
    # plt.ylabel('Datos')
    plt.savefig("C:/Users/gujho/OneDrive/Documentos/1SEM2022/IPC2/LAB/IPC2_Proyecto3_201700900/webapp/index/static/img/grafica.jpg")
    return {"fechas": ''}


if __name__ == '__main__':
    app.run(debug=True)

#Inicializar application
#python app.py

