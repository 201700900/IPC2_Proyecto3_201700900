import xml.etree.ElementTree as ET


class DB:

    initial= '''
        <database>
        <diccionario>
        <sentimientos_positivos></sentimientos_positivos>
        <sentimientos_negativos></sentimientos_negativos>
        <empresas_analizar></empresas_analizar>
        </diccionario>
        <lista_respuestas></lista_respuestas>
        </database>
    '''

    def __init__(self) -> None:
        self.id = 1
        self.path = "DATABASE.xml"

    def enlistar(self, l):
        lista = []
        for item in l:
            lista.append(item)
        return lista

    def existeSentimiento(self, valor, sentimiento):
        for s in sentimiento:
            if valor == s.text:
                return True

    def guardar_positivo(self, new):
        tree = ET.parse(self.path)
        root = tree.getroot()
        if not self.existeSentimiento(new, root[0][0]):
            nuevo = ET.SubElement(root[0][0], 'palabra')
            nuevo.text = new
            ET.indent(root)
            tree.write(self.path)

    def guardar_negativo(self, new):
        tree = ET.parse(self.path)
        root = tree.getroot()
        if not self.existeSentimiento(new, root[0][1]):
            nuevo = ET.SubElement(root[0][1], 'palabra')
            nuevo.text = new
            ET.indent(root)
            tree.write(self.path)

    def existeEmpresa(self, valor, empresas):
        for empresa in empresas:
            if valor == empresa.find('nombre').text:
                return True

    def guardar_empresa(self, new, lista):
        tree = ET.parse(self.path)
        root = tree.getroot()

        if not self.existeEmpresa(new, root[0][2]):
            nuevo = ET.SubElement(root[0][2], 'empresa')
            nombre = ET.SubElement(nuevo, 'nombre')
            nombre.text = new
            for servicio in lista:
                s = ET.SubElement(nuevo, 'servicio')
                s.set('nombre', servicio.nombre)
                for alias in servicio.alias:
                    a = ET.SubElement(s, 'alias')
                    a.text = alias
            ET.indent(root)
            tree.write(self.path)

        for empresa in root[0][2]:  # <empresas_analizar>
            print(empresa.find('nombre').text)
            if new == empresa.find('nombre').text:
                # obtener cada servicio
                for servicio in empresa.iter('servicio'):
                    s_nombre = servicio.attrib['nombre'].strip()

    def existeFecha(self, valor, compara):
        for respuesta in compara:

            if valor == respuesta.find('fecha').text:
                return True

    def guardar_fecha(self, new):
        tree = ET.parse(self.path)
        root = tree.getroot()
        if not self.existeFecha(new, root[1]):
            respuesta = ET.SubElement(root[1], 'respuesta')
            fecha = ET.SubElement(respuesta, 'fecha')
            fecha.text = new
            mensajes = ET.SubElement(respuesta, 'mensajes')
            tot_mensajes = ET.SubElement(mensajes, 'total')
            tot_positivos = ET.SubElement(mensajes, 'positivos')
            tot_negativos = ET.SubElement(mensajes, 'negativos')
            tot_neutros = ET.SubElement(mensajes, 'neutros')
            tot_mensajes.text = str(0)
            tot_positivos.text = str(0)
            tot_negativos.text = str(0)
            tot_neutros.text = str(0)
            analisis = ET.SubElement(respuesta, 'analisis')
            ET.indent(root)
            tree.write(self.path)

    def guardar_tot_mensajes(self, fecha, tot, pos, neg, neu):
        tree = ET.parse(self.path)
        root = tree.getroot()
        for respuesta in root[1]:
            if fecha == respuesta.find('fecha').text:
                tot_m = tot + int(respuesta[1][0].text.strip())
                tot_pos = pos + int(respuesta[1][1].text.strip())
                tot_neg = neg + int(respuesta[1][2].text.strip())
                tot_neut = neu + int(respuesta[1][3].text.strip())
                respuesta[1][0].text = str(tot_m)
                respuesta[1][1].text = str(tot_pos)
                respuesta[1][2].text = str(tot_neg)
                respuesta[1][3].text = str(tot_neut)
                ET.indent(root)
                tree.write(self.path)
    
    def guardar_tot_empresa(self, fecha, new, tot, pos, neg, neu):
        tree = ET.parse(self.path)
        root = tree.getroot()
        for respuesta in root[1]:
            if fecha == respuesta.find('fecha').text:
                for empresa in respuesta[2]:
                    if new == empresa.attrib['nombre'].strip():
                        print(tot + int(empresa[1][0].text.strip()))
                        print(tot)
                        print(int(empresa[1][0].text.strip()))
                        tot_e = tot + int(empresa[1][0].text.strip())
                        tot_pos = pos + int(empresa[1][1].text.strip())
                        tot_neg = neg + int(empresa[1][2].text.strip())
                        tot_neut = neu + int(empresa[1][3].text.strip())
                        empresa[0][0].text = str(tot_e)
                        empresa[0][1].text = str(tot_pos)
                        empresa[0][2].text = str(tot_neg)
                        empresa[0][3].text = str(tot_neut)
                        ET.indent(root)
                        tree.write(self.path)

    def existe_empresa_analisis(self, valor, compara):
        for empresa in compara:

            if valor == empresa.attrib['nombre'].strip():
                return True

    def guardar_analisis_empresa(self, fecha, new, lista):#{'servicio':servicio, 'pos': 0, 'neg': 0, 'neut':0}
        tree = ET.parse(self.path)
        root = tree.getroot()
        for respuesta in root[1]:
            if fecha == respuesta.find('fecha').text:
                if not self.existe_empresa_analisis(new, respuesta[2]):
                    e = ET.SubElement(respuesta[2], 'empresa')
                    e.set('nombre', new)
                    mensajes = ET.SubElement(e, 'mensajes')
                    print()
                    tot_mensajes = ET.SubElement(mensajes, 'total')
                    tot_positivos = ET.SubElement(mensajes, 'positivos')
                    tot_negativos = ET.SubElement(mensajes, 'negativos')
                    tot_neutros = ET.SubElement(mensajes, 'neutros')
                    tot_mensajes.text = str(0)
                    tot_positivos.text = str(0)
                    tot_negativos.text = str(0)
                    tot_neutros.text = str(0)
                    servicios = ET.SubElement(e, 'servicios')
                    for servicio in lista:
                        self.nuevo_servicio(servicios, servicio)
                for empresa in respuesta[2]:
                    if new == empresa.attrib['nombre'].strip():
                        for servicio in lista:
                            
                            if new == empresa.attrib['nombre'].strip():

                                for a in empresa[1]:
                                    if servicio['servicio'] == a.attrib['nombre'].strip():
                                        total_s = servicio['pos'] + \
                                            servicio['neg'] + servicio['neut']

                                        tot_m = total_s + \
                                            int(respuesta[1][0].text)
                                        tot_pos = servicio['pos'] + \
                                            int(respuesta[1][1].text)
                                        tot_neg = servicio['neg'] + \
                                            int(respuesta[1][2].text)
                                        tot_neut = servicio['neut'] + \
                                            int(respuesta[1][3].text)
                                        a[0][0].text = str(tot_m)
                                        a[0][1].text = str(tot_pos)
                                        a[0][2].text = str(tot_neg)
                                        a[0][3].text = str(tot_neut)
                            elif not self.existe_servicio_analisis(servicio, empresa[1]):
                                self.nuevo_servicio(empresa[1], servicio)

            ET.indent(root)
            tree.write(self.path)

    def existe_servicio_analisis(self, valor, compara):
        for servicio in compara:

            if valor == servicio.attrib['nombre'].strip():
                return True

    def nuevo_servicio(self, servicios, servicio):
        s = ET.SubElement(servicios, 'servicio')
        s.set('nombre', servicio['servicio'])
        total_s = servicio['pos'] + servicio['neg'] + servicio['neut']
        mensajes = ET.SubElement(s, 'mensajes')
        tot_mensajes = ET.SubElement(mensajes, 'total')
        tot_positivos = ET.SubElement(mensajes, 'positivos')
        tot_negativos = ET.SubElement(mensajes, 'negativos')
        tot_neutros = ET.SubElement(mensajes, 'neutros')
        tot_mensajes.text = str(total_s)
        tot_positivos.text = str(servicio['pos'])
        tot_negativos.text = str(servicio['neg'])
        tot_neutros.text = str(servicio['neut'])


    # tree.write(self.path)
# n = DB()

# n.guardar_positivo('fantastico')
# alias1 = ['llamar', 'llamado', 'llame', 'llamo', 'llamare']
# alias = ['mensajes', 'mensajeo', 'mensaje', 'sms']
# n.guardar_empresa('CLARO', [alias1, alias].text)
# n.guardar_fecha('10/04/2022')
# n.guardar_tot_mensajes('01/04/2022', 1, 1, 1, 1)
# n.guardar_analisis_empresa('10/04/2022')
# ser1 = ['comprar', 10, 2, 4, 4]
# ser = ['alquilar', 15, 7, 4, 4]
# n.guardar_analisis_empresa('01/04/2022', 'TIGO', [ser, ser1])
# n.guardar_tot_empresa('01/04/2022', 'USAC', 1, 1, 1, 1)