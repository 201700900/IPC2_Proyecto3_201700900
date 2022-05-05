import xml.etree.ElementTree as ET


class DB:

    def __init__(self) -> None:
        self.id = 1
        self.path = "backend\DB\DATABASE.xml"

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
                s.set('nombre', servicio[0].text)
                for alias in servicio:
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
                tot_m = tot + int(respuesta[1][0].text)
                tot_pos = pos + int(respuesta[1][1].text)
                tot_neg = neg + int(respuesta[1][2].text)
                tot_neut = neu + int(respuesta[1][3].text)
                respuesta[1][0].text = str(tot_m)
                respuesta[1][1].text = str(tot_pos)
                respuesta[1][2].text = str(tot_neg)
                respuesta[1][3].text = str(tot_neut)
                ET.indent(root)
                tree.write(self.path)

    def existe_empresa_analisis(self, valor, compara):
        for empresa in compara:

            if valor == empresa.attrib['nombre'].strip():
                return True

    def guardar_analisis_empresa(self, fecha, new, lista):
        tree = ET.parse(self.path)
        root = tree.getroot()
        for respuesta in root[1]:
            print(respuesta)
            if fecha == respuesta.find('fecha').text:
                if not self.existe_empresa_analisis(new, respuesta[2]):
                    empresa = ET.SubElement(respuesta[2], 'empresa')
                    empresa.set('nombre', new)
                    mensajes = ET.SubElement(empresa, 'mensajes')
                    tot_mensajes = ET.SubElement(mensajes, 'total')
                    tot_positivos = ET.SubElement(mensajes, 'positivos')
                    tot_negativos = ET.SubElement(mensajes, 'negativos')
                    tot_neutros = ET.SubElement(mensajes, 'neutros')
                    tot_mensajes.text = str(0)
                    tot_positivos.text = str(0)
                    tot_negativos.text = str(0)
                    tot_neutros.text = str(0)
                    servicios = ET.SubElement(empresa, 'servicios')
                    for servicio in lista:
                        self.nuevo_servicio(servicios, servicio)
                else:
                    for empresa in respuesta[2]:

                        for servicio in lista:
                            if not self.existe_servicio_analisis(servicio, empresa[1]):
                                self.nuevo_servicio(empresa[1], servicio)
                            if new == empresa.attrib['nombre'].strip():

                                for a in empresa[1]:

                                    if servicio[0] == servicio.attrib['nombre'].strip():
                                        total_s = servicio[1] + \
                                            servicio[2] + servicio[3]

                                        tot_m = total_s + \
                                            int(respuesta[1][0].text)
                                        tot_pos = servicio[1] + \
                                            int(respuesta[1][1].text)
                                        tot_neg = servicio[2] + \
                                            int(respuesta[1][2].text)
                                        tot_neut = servicio[3] + \
                                            int(respuesta[1][3].text)
                                        a[0].text = str(tot_m)
                                        a[1].text = str(tot_pos)
                                        a[2].text = str(tot_neg)
                                        a[3].text = str(tot_neut)

            ET.indent(root)
            tree.write(self.path)

    def existe_servicio_analisis(self, valor, compara):
        for servicio in compara:

            if valor == servicio.attrib['nombre'].strip():
                return True

    def nuevo_servicio(self, servicios, servicio):
        s = ET.SubElement(servicios, 'servicio')
        s.set('nombre', servicio[0])
        total_s = servicio[1] + servicio[2] + servicio[3]
        mensajes = ET.SubElement(s, 'mensajes')
        tot_mensajes = ET.SubElement(mensajes, 'total')
        tot_positivos = ET.SubElement(mensajes, 'positivos')
        tot_negativos = ET.SubElement(mensajes, 'negativos')
        tot_neutros = ET.SubElement(mensajes, 'neutros')
        tot_mensajes.text = str(total_s)
        tot_positivos.text = str(servicio[1])
        tot_negativos.text = str(servicio[2])
        tot_neutros.text = str(servicio[3])


    # tree.write(self.path)
n = DB()

# n.guardar_empresa('USAC', [ "a"].text)
# n.guardar_positivo('fantastico')
# alias1 = ['llamar', 'llamado', 'llame', 'llamo', 'llamare']
# alias = ['mensajes', 'mensajeo', 'mensaje', 'sms']
# n.guardar_empresa('CLARO', [alias1, alias].text)
# n.guardar_fecha('10/04/2022')
# n.guardar_tot_mensajes('01/04/2022', 1, 1, 1, 1)
# n.guardar_analisis_empresa('10/04/2022')
ser1 = ['comprar', 10, 2, 4, 4]
ser = ['alquilar', 15, 7, 4, 4]
n.guardar_analisis_empresa('01/04/2022', 'TIGO', [ser, ser1])
