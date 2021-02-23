
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


#make a copy of pdf wih a grid drawn on
def grid_pdf(_pdf):
    horizontal_line ="____________________________________________________________________________________________________"
    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)

    #draws horizontal lines
    for y in (i*30 for i in range(50)):
        can.drawString(0,y,str(y)+horizontal_line)
    
    #draws vertical lines
    for x in (i*30 for i in range(21)):
        can.drawString(x,y,"_"+str(x))
        for y in range(1,765):
            can.drawString(x,y,"|")

    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open(_pdf, "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open("grid_"+_pdf, "wb")
    output.write(outputStream)




def export_player_to_pdf(template_pdf,output_pdf,positions):
    
    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)

    #positions=[(70,715,"NAME")]
    for position in positions:
        can.drawString(position[0],position[1],position[2])
    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("character_sheet.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open("prova.pdf", "wb")
    output.write(outputStream)
    outputStream.close()


#TEST EXAMPLE
'''
positions=[(70,715,"NAME")]
input_pdf="character_sheet.pdf"
output_pdf="player1.pdf"
grid_pdf("character_sheet.pdf")
'''

