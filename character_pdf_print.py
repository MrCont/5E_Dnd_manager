
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def export_player_to_pdf(template_pdf,output_pdf,positions)
    
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
outtput_pdf=""
'''
