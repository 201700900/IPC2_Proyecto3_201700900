from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter#(612.0, 792.0) alto, ancho
from clases import escribir






def makePDF():
    escribir.cargar_fechas()
    c = canvas.Canvas("reporte.pdf", pagesize=A4)
    c.setTitle('REPORTE')

    w, h = A4

   
    for f in escribir.ListaFechas:

        

        
        text = c.beginText(50, h - 50)
        text.setFont("Times-Roman", 12)


       

      
        text.textLine(" 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨 🟨")

        text.textLine("FECHA: " + f.fecha)
        # tot_mensajes(respuesta, len(f.mensajes), tot_pos, tot_neg, tot_neut)
        text.textLine('Cantidad total de mensajes recibidos: '+ str(f.total_mensajes['tot']))
        text.textLine('Cantidad total de mensajes positivos: '+ str(f.total_mensajes['pos']))
        text.textLine('Cantidad total de mensajes negativos: '+ str(f.total_mensajes['neg']))
        text.textLine('Cantidad total de mensajes neutros: '  + str(f.total_mensajes['neut']))
        # print(f.d_empresas)

        for empresa in f.d_empresas:
            text.textLine("--------------------------------------------------------------------------------------------------------------------------------")
            text.textLine("Empresa: " + empresa['empresa'])

            text.textLine('\tNúmero total de mensajes que mencionan a ' + empresa['empresa']+ ': ' + str(empresa['tot']))
            text.textLine('\tMensajes positivos: '+ str(empresa['pos']))
            text.textLine('\tMensajes negativos:  '+ str(empresa['neg']))
            text.textLine('\tMensajes neutros: '+ str(empresa['neut']))

            for servicio in empresa['servicios']:
                text.textLine("--------------------------------------------------------------------------------------------------------------------------------")

                text.textLine("Servicio: " + servicio['servicio'])

                text.textLine('\tNúmero total de mensajes que mencionan al servicio ' + servicio['servicio']+ ': ' + str(servicio['tot']))
                text.textLine('\tMensajes positivos: '+ str(empresa['pos']))
                text.textLine('\tMensajes negativos:  '+ str(empresa['neg']))
                text.textLine('\tMensajes neutros: '+ str(empresa['neut']))
            
        c.drawText(text)
        c.showPage()
    c.save()