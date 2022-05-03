from clases import linkedList as lista
import xml.etree.ElementTree as ET

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
                tot_neg +=1
            elif m.sentimiento == 'neutro':
                tot_neut +=1

      
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
            








        #create a new XML file with the results
        mydata = ET.tostring(root, encoding='UTF-8', method ='html')
        myfile = open("items.xml", "w", encoding='UTF-8')
        myfile.write(mydata.decode('UTF-8'))
        print(mydata.decode('UTF-8'))
    return mydata.decode('UTF-8')

