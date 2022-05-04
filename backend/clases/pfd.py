from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter#(612.0, 792.0) alto, ancho
from clases import escribir






def makePDF():
    c = canvas.Canvas("reporte.pdf", pagesize=A4)
    c.setTitle('REPORTE')

    w, h = A4

    
    text = c.beginText(50, h - 50)
    text.setFont("Times-Roman", 12)

   
    for f in escribir.ListaFechas:

        

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

      
        text.textLine("--------------------------------------------------------------------------------------------------------------------------------")

        text.textLine("FECHA: " + f.fecha)
        # tot_mensajes(respuesta, len(f.mensajes), tot_pos, tot_neg, tot_neut)
        text.textLine('Cantidad total de mensajes recibidos: '+ str(len(f.mensajes)))
        text.textLine('Cantidad total de mensajes positivos: '+ str(tot_pos))
        text.textLine('Cantidad total de mensajes negativos: '+ str(tot_neg))
        text.textLine('Cantidad total de mensajes neutros: '+ str(tot_neut))


        for empresa in f.empresas:
            text.textLine("--------------------------------------------------------------------------------------------------------------------------------")
            text.textLine("Empresa: " + empresa[0].nombre)

            total_e = empresa[1] + empresa[2] + empresa[3]

            ( total_e, empresa[1], empresa[2], empresa[3])
            text.textLine('\tNúmero total de mensajes que mencionan a ' + empresa[0].nombre+ ': ' + str(total_e))
            text.textLine('\tMensajes positivos: '+ str(empresa[1]))
            text.textLine('\tMensajes negativos:  '+ str(empresa[2]))
            text.textLine('\tMensajes neutros: '+ str(empresa[3]))

        for servicio in f.servicios:
            text.textLine("--------------------------------------------------------------------------------------------------------------------------------")

            text.textLine("Servicio: " + servicio[0].nombre)

            total_s = servicio[1] + servicio[2] + servicio[3]
            text.textLine('\tNúmero total de mensajes que mencionan al servicio ' + servicio[0].nombre+ ': ' + str(total_s))
            text.textLine('\tMensajes positivos: '+ str(empresa[1]))
            text.textLine('\tMensajes negativos:  '+ str(empresa[2]))
            text.textLine('\tMensajes neutros: '+ str(empresa[3]))
    c.drawText(text)
    c.save()