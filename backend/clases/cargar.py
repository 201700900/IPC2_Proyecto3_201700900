import xml.etree.ElementTree as ET
import linkedList as lista
import tkinter, tkinter.filedialog, re
import empresa as company
import mensaje as m
import escribir

# ListaMensajes = lista.LinkedList()
# Positivos = lista.LinkedList()
# Negativos = lista.LinkedList()
# Empresas = lista.LinkedList()

def leer():
    global Positivos
    global Negativos
    global Empresas
    global ListaMensajes
    # root = tkinter.Tk() #esto se hace solo para eliminar la ventanita de Tkinter 
    # root.withdraw() #ahora se cierra 
    # path = tkinter.filedialog.askopenfilename() #abre el explorador de archivos y guarda la seleccion en la variable!


    # try:
    path = 'C:/Users/gujho/OneDrive/Documentos/1SEM2022/IPC2/LAB/IPC2_Proyecto3_201700900/backend/clases/entrada.xml'
    tree = ET.parse(path)
    root = tree.getroot()#<solicitud_clasificacion>
    ###################################################################################
    # for diccionario in root[0]:#root[0] es <diccionario>
    #     print(diccionario.tag)#obtener cada diccionario
    
    for positivo in root[0][0]: #<sentimientos_positivos> 
        # print(positivo.text)
        escribir.Positivos.Append(positivo.text.strip())
        

    for negattivo in root[0][1]: #<sentimientos_negativos> 
        # print(negattivo.text)
        escribir.Negativos.Append(negattivo.text.strip())

    for empresa in root[0][2]: #<empresas_analizar> 
        nombre = empresa.find('nombre').text.strip()
        # print(nombre)
        lista_servicios = lista.LinkedList()
        for servicio in empresa.iter('servicio'):#obtener cada servicio
            lista_alias = lista.LinkedList()
            lista_alias.Append(servicio.attrib['nombre'].strip())
            # print(servicio.attrib['nombre'])
            for alias in servicio:
                # print(alias.text)
                lista_alias.Append(alias.text.strip())
            lista_servicios.Append(lista_alias)
        escribir.Empresas.Append(company.Empresa(nombre, lista_servicios))


    for mensaje in root[1]:#root[0] es <lista_mensajes>
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

        escribir.ListaMensajes.Append(m.Mensaje(fecha, ciudad, usuario, red_social, mensaje_final))
        
        



        
            



    print("\t\033[;32m"+ path + " cargado con exito"+'\033[0;m')

    # except:
    #     print("\t\033[;31m"+ path, "no encontrado"+'\033[0;m')

leer()

