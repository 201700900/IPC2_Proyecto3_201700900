from operator import neg
from clases import linkedList as lista
class Fecha:

    def __init__(self, fecha):
        self.fecha = fecha
        self.mensajes = lista.LinkedList()
        self.empresas = lista.LinkedList()
        self.servicios = lista.LinkedList()
        self.d_empresas = []
        self.total_mensajes = {'tot':0,'pos': 0, 'neg': 0, 'neut':0}
    
    def set_total_mensajes(self, tot, pos, neg, neut):
        self.total_mensajes['tot'] = tot
        self.total_mensajes['pos'] = pos
        self.total_mensajes['neg'] = neg
        self.total_mensajes['neut'] = neut

    def in_dictlist(self, key, value, my_dictlist): 
        for entry in my_dictlist: 
            if entry[key] == value: 
                return True
        return False 

    def  new_d_empresa(self, empresa,tot=0, pos=0, neg=0, neut=0):
        nuevo = {'empresa':empresa, 'tot':tot, 'pos':pos, 'neg':neg, 'neut': neut, 'servicios':[]}
        if not self.in_dictlist('empresa', empresa, self.d_empresas):
            self.d_empresas.append(nuevo)

    def new_servicio(self, empresa, servicio, tot=0, pos=0, neg=0, neut=0):
        for d in self.d_empresas:
            if d['empresa'] == empresa:
                if not self.in_dictlist('servicio',servicio, d['servicios'] ):
                    d["servicios"].append({'servicio':servicio, 'tot':tot, 'pos':pos, 'neg':neg, 'neut': neut})

    def e_nuevo(self, empresa):
        nuevo= lista.LinkedList()
        nuevo.Append(empresa)
        nuevo.Append(0)
        nuevo.Append(0)
        nuevo.Append(0)
        self.empresas.Append(nuevo)

    def sentimiento_empresa(self, empresa, sentimiento):
        self.new_d_empresa(empresa)
        for e in self.d_empresas:
            if empresa == e['empresa']: 

                if sentimiento == 'positivo':
                    e['pos'] +=1
                    e['tot'] +=1
                    
                if sentimiento == 'negativo':
                    e['neg'] +=1
                    e['tot'] +=1

                if sentimiento == 'neutro':
                    e['neut'] +=1
                    e['tot'] +=1

    def sentimiento_servicio(self, empresa, servicio, sentimiento):
        self.new_servicio(empresa, servicio)
        for e in self.d_empresas:
            if empresa == e['empresa']: 
                for s in e['servicios']:
                    if s['servicio'] == servicio:

                        if sentimiento == 'positivo':
                            s['pos'] +=1
                            s['tot'] +=1
                        if sentimiento == 'negativo':
                            s['neg'] +=1
                            s['tot'] +=1
                        if sentimiento == 'neutro':
                            s['neut'] +=1
                            s['tot'] +=1

                        
    def empresa(self, empresa, sentimiento):
        # if not self.empresas.Buscar(empresa):
        #     self.e_nuevo(empresa)
        match = 0
        for d in self.empresas:
            if d[0].nombre == empresa.nombre:
                match+=1
        if match == 0:
            self.e_nuevo(empresa)

        for e in self.empresas:
            if empresa.nombre == e[0].nombre: 

                if sentimiento == 'positivo':
                    e[1] +=1
                if sentimiento == 'negativo':
                    e[2] +=1
                if sentimiento == 'neutro':
                    e[3] +=1
                break

    def s_nuevo(self, servicio):
        nuevo= lista.LinkedList()
        nuevo.Append(servicio)
        nuevo.Append(0)
        nuevo.Append(0)
        nuevo.Append(0)
        self.servicios.Append(nuevo)


    def servicio(self, servicio, sentimiento):
        
        # if not self.servicios.Buscar(servicio):
        #     self.e_nuevo(servicio)
        match = 0
        for a in self.servicios:
            if a[0].nombre == servicio.nombre:
                match+=1
        if match == 0:
            self.s_nuevo(servicio)

        for s in self.servicios:
            if servicio.nombre == s[0].nombre: 

                if sentimiento == 'positivo':
                    s[1] +=1
                if sentimiento == 'negativo':
                    s[2] +=1
                if sentimiento == 'neutro':
                    s[3] +=1
                break

    
        

    