import xml.etree.ElementTree as ET
from clases import linkedList as lista
import tkinter
import tkinter.filedialog
import re
from clases import empresa as company
from clases import mensaje as m
from clases import escribir, db
from clases import servicio as s
from clases import fecha as f
n = db.DB()
# ListaMensajes = lista.LinkedList()
# Positivos = lista.LinkedList()
# Negativos = lista.LinkedList()
# Empresas = lista.LinkedList()
text = ''


def getXMLasSTR(root):
    global text
    mydata = ET.tostring(root, encoding='UTF-8', method='html')
    # print(mydata.decode('UTF-8'))
    text = mydata.decode('UTF-8')


def getPath():
    global text
    text = ''
    # try:
    # root = tkinter.Tk()  # esto se hace solo para eliminar la ventanita de Tkinter
    # root.withdraw()  # ahora se cierra
    # abre el explorador de archivos y guarda la seleccion en la variable!
    path = tkinter.filedialog.askopenfilename()

    tree = ET.parse(path)
    root = tree.getroot()  # <solicitud_clasificacion>
    leer(root)
    getXMLasSTR(root)
    # except:
    #     print("\t\033[;31m"+"no encontrado"+'\033[0;m')


def leer(root):
    global Positivos
    global Negativos
    global Empresas
    global ListaMensajes
    # root = tkinter.Tk() #esto se hace solo para eliminar la ventanita de Tkinter
    # root.withdraw() #ahora se cierra
    # path = tkinter.filedialog.askopenfilename() #abre el explorador de archivos y guarda la seleccion en la variable!

    # try:
    # path = 'C:/Users/gujho/OneDrive/Documentos/1SEM2022/IPC2/LAB/IPC2_Proyecto3_201700900/backend/clases/entrada.xml'
    # tree = ET.parse(path)
    # root = tree.getroot()#<solicitud_clasificacion>
    ###################################################################################
    # for diccionario in root[0]:#root[0] es <diccionario>
    #     print(diccionario.tag)#obtener cada diccionario

    for positivo in root[0][0]:  # <sentimientos_positivos>
        # print(positivo.text)
        if not escribir.Positivos.Buscar(positivo):
            n.guardar_positivo(escribir.tilde(positivo.text.strip()))
            escribir.Positivos.Append(positivo.text.strip())

    for negattivo in root[0][1]:  # <sentimientos_negativos>
        # print(negattivo.text)
        if not escribir.Negativos.Buscar(negattivo):
            escribir.Negativos.Append(negattivo.text.strip())
            n.guardar_negativo(escribir.tilde(negattivo.text.strip()))


    for empresa in root[0][2]:  # <empresas_analizar>
        nombre = escribir.tilde(empresa.find('nombre').text.strip())
        # print(nombre)
        lista_servicios = lista.LinkedList()
        for servicio in empresa.iter('servicio'):  # obtener cada servicio
            lista_alias = lista.LinkedList()
            s_nombre = servicio.attrib['nombre'].strip()
            lista_alias.Append(escribir.tilde(s_nombre))
            # print(servicio.attrib['nombre'])
            for alias in servicio:
                # print(alias.text)
                lista_alias.Append(escribir.tilde(alias.text.strip()))
            lista_servicios.Append(s.Servicio(escribir.tilde(s_nombre), lista_alias))
        match = 0
        for e in escribir.Empresas:
            if e.nombre == nombre:
                match += 1
        if match == 0:
            escribir.Empresas.Append(company.Empresa(nombre, lista_servicios))
            n.guardar_empresa(escribir.tilde(nombre), lista_servicios)

    for mensaje in root[1]:  # root[0] es <lista_mensajes>
        # print(mensaje.text)
        separado = mensaje.text.split(':')
        # print(separado)
        temp = (separado[1].strip())
        ciudad_fecha = temp.split(' ')
        # print(ciudad_fecha)
        ciudad = ciudad_fecha[0].strip(' ,')
        # print(ciudad)
        fecha = ciudad_fecha[1]
        # print(fecha)
        nuevo = f.Fecha(fecha)
        # if not escribir.ListaFechas.Buscar(fecha):
        #     escribir.ListaFechas.Append(nuevo)
        match = 0
        for d in escribir.ListaFechas:
            if d.fecha == fecha:
                match += 1
        if match == 0:
            escribir.ListaFechas.Append(nuevo)

        usuario_red = separado[3].split('\n')
        usuario = usuario_red[0].strip()
        # print(usuario)

        mensaje_red = separado[4].split('\n')

        red_social = mensaje_red[0].strip()
        # print(red_social)

        mensaje_final = ''
        for i in range(1, len(mensaje_red)-1):
            mensaje_final += mensaje_red[i].strip('\t\n')
        # print(mensaje_final)
        existe = 0
        for x in escribir.ListaMensajes:
            if x.existe(fecha, ciudad, usuario, red_social, mensaje_final.strip()):
                existe += 1
        if existe == 0:
            nuevo_mensaje = m.Mensaje(
                fecha, ciudad, usuario, red_social, mensaje_final.strip())
            escribir.ListaMensajes.Append(nuevo_mensaje)
            for fe in escribir.ListaFechas:
                if fe.fecha == fecha:
                    fe.mensajes.Append(nuevo_mensaje)

    print("\t\033[;32m"+" cargado con exito"+'\033[0;m')

    # except:
    #     print("\t\033[;31m"+ path, "no encontrado"+'\033[0;m')

# leer()
# escribir.respuesta()
