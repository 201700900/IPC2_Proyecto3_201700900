from unittest import result
from clases import linkedList as lista, mensaje as m
import xml.etree.ElementTree as ET

ListaFechas = lista.LinkedList()
ListaMensajes = lista.LinkedList()
Positivos = lista.LinkedList()
Negativos = lista.LinkedList()
Empresas = lista.LinkedList()


def delete():
    global ListaFechas
    global ListaMensajes
    global Positivos
    global Negativos
    global Empresas

    ListaFechas = lista.LinkedList()
    ListaMensajes = lista.LinkedList()
    Positivos = lista.LinkedList()
    Negativos = lista.LinkedList()
    Empresas = lista.LinkedList()


def tot_mensajes(padre, tot, pos, neg, neu):

    mensajes = ET.SubElement(padre, 'mensajes')
    tot_mensajes = ET.SubElement(mensajes, 'total')
    tot_positivos = ET.SubElement(mensajes, 'positivos')
    tot_negativos = ET.SubElement(mensajes, 'negativos')
    tot_neutros = ET.SubElement(mensajes, 'neutros')

    tot_mensajes.text = str(tot)
    tot_positivos.text = str(pos)
    tot_negativos.text = str(neg)
    tot_neutros.text = str(neu)


def respuesta():
    global ListaFechas
    global ListaMensajes
    global Positivos
    global Negativos
    global Empresas

    root = ET.Element('lista_respuestas')
    for f in ListaFechas:

        tot_pos = 0
        tot_neg = 0
        tot_neut = 0

        for m in f.mensajes:
            if m.sentimiento == 'positivo':
                tot_pos += 1
            elif m.sentimiento == 'negativo':
                tot_neg += 1
            elif m.sentimiento == 'neutro':
                tot_neut += 1

        respuesta = ET.SubElement(root, 'respuesta')

        fecha = ET.SubElement(respuesta, 'fecha')
        fecha.text = f.fecha
        tot_mensajes(respuesta, len(f.mensajes), tot_pos, tot_neg, tot_neut)

        # analisis = ET.SubElement(respuesta, 'analisis')
        # for empresa in Empresas:
        #     e = ET.SubElement(analisis, 'empresa')
        #     e.set('nombre', empresa.nombre)
        #     total_e = empresa.positivo + empresa.negativo + empresa.neutro

        #     tot_mensajes(e, total_e, empresa.positivo, empresa.negativo, empresa.neutro)

        #     servicios = ET.SubElement(e, 'servicios')

        #     for servicio in empresa.servicios:
        #         s = ET.SubElement(servicios, 'servicio')
        #         s.set('nombre', servicio.nombre)
        #         total_s = servicio.positivo + servicio.negativo + servicio.neutro
        #         tot_mensajes(s, total_s, servicio.positivo, servicio.negativo, servicio.neutro)

        analisis = ET.SubElement(respuesta, 'analisis')
        for empresa in f.empresas:
            e = ET.SubElement(analisis, 'empresa')
            e.set('nombre', empresa[0].nombre)
            total_e = empresa[1] + empresa[2] + empresa[3]

            tot_mensajes(e, total_e, empresa[1], empresa[2], empresa[3])

            servicios = ET.SubElement(e, 'servicios')

        for servicio in f.servicios:
            s = ET.SubElement(servicios, 'servicio')
            s.set('nombre', servicio[0].nombre)
            total_s = servicio[1] + servicio[2] + servicio[3]
            tot_mensajes(s, total_s, servicio[1], servicio[2], servicio[3])

        # create a new XML file with the results
        ET.indent(root)
        mydata = ET.tostring(root, encoding='UTF-8', method='html')
        myfile = open("items.xml", "w", encoding='UTF-8')
        myfile.write(mydata.decode('UTF-8'))
        myfile.close()
        print(mydata.decode('UTF-8'))
    return mydata.decode('UTF-8')


def porcentaje(total, numero):
    if numero == 0:
        return 0
    else:
        num = float(numero)
        tot = float(total)
        res = (num*100)/tot
        return round(res, 2)


def prueba_mensaje(root):

    mensaje = root  # root es <lista_mensajes>
    # print(mensaje.text)
    text = mensaje.text.strip(' \t\n')
    separado = text.split(' ')
    # print(separado)
    ciudad = separado[3].strip(' ,\t\n')
    # print(ciudad)
    fecha = separado[4].strip(' ,\t\n')

    usuario = separado[7].strip(' ,\t\n')
    # print(usuario)

    red_social = separado[10].strip(' ,\t\n')
    # print(red_social)

    mensaje_final = " ".join(separado).strip(' ,\t\n')
    # for i in range(1, len(mensaje_red)-1):
    #     mensaje_final += mensaje_red[i].strip('\t\n')
    # print(mensaje_final)

    nuevo = m.Mensaje(fecha, ciudad, usuario, red_social,
                      mensaje_final.strip(), 'prueba')

    root = ET.Element('lista_respuestas')
    date = ET.SubElement(root, 'fecha')
    date.text = nuevo.fecha

    network = ET.SubElement(root, 'red_social')
    network.text = nuevo.red_social

    user = ET.SubElement(root, 'usuario')
    user.text = nuevo.usuario
    company = ET.SubElement(root, 'empresas')

    for empresa in nuevo.d_Empresas:
        e = ET.SubElement(company, 'empresa')
        e.set('nombre', empresa['empresa'])
        for servicio in empresa['servicios']:
            s = ET.SubElement(e, 'servicio')
            s.text = servicio

    positivo = ET.SubElement(root, 'palabras_positivas')
    positivo.text = str(nuevo.palabras_positivas)
    negativo = ET.SubElement(root, 'palabras_negativas')
    negativo.text = str(nuevo.palabras_negativas)
    total_palabras = nuevo.palabras_positivas + nuevo.palabras_negativas
    sen_positivo = ET.SubElement(root, 'sentimiento_positivo')
    sen_positivo.text = str(porcentaje(
        total_palabras, nuevo.palabras_positivas))+'%'
    sen_negativo = ET.SubElement(root, 'sentimiento_negaivo')
    sen_negativo.text = str(porcentaje(
        total_palabras, nuevo.palabras_negativas))+'%'
    analizado = ET.SubElement(root, 'sentimiento_analizado')
    analizado.text = nuevo.sentimiento
    ET.indent(root)
    mydata = ET.tostring(root, encoding='UTF-8', method='html')
    print(mydata.decode('UTF-8'))
    return mydata.decode('UTF-8')
