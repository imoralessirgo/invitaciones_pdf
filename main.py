import csv
from json.tool import main
from fpdf import FPDF
import io
from PyPDF2 import PdfReader, PdfWriter



mapa_invitados = {
    "1" : "BOLETO PERSONAL",
    "2" : "DOS INVITADOS",
    "3" : "TRES INVITADOS",
    "4" : "CUATRO INVITADOS",
    "5" : "CINCO INVITADOS"
}

boletos = ""
invitados = ""

path = "./inv_per/"
#path = "../../../mnt/i/My\ Drive/PROYECTOS\ 2022/XIMENA\ Y\ HONORE/INVITACIÓN\ DIGITAL\ XH/INVITACIONES\ PERSONALIZADAS/"

font_boletos = "SafiraMarch-gxeKY"
font_invitados = "Assistant-Light"

# font_boletos = "Arial"
# font_invitados = "Arial"

lista_1 = "Xime.csv"
lista_2 = "Hono.csv"

def nuevo_pdf(txt_boletos, txt_invitado):
    pdf = FPDF("P","mm", [502.356,770.114])
    pdf.add_font(font_invitados,'','./' + font_invitados + '.ttf', False)
    pdf.add_font(font_boletos, '', './' + font_boletos + '.otf', False)
    pdf.add_page()
    pdf.set_font(font_boletos, "", 11)
    pdf.set_xy(100.65, 492.77)    
    pdf.set_char_spacing(5)
    pdf.cell(108, 20, txt = txt_boletos, align = 'C')
    pdf.set_font(font_invitados, "", 24)
    pdf.set_xy(120.65, 466.37)
    pdf.set_char_spacing(7)
    with pdf.rotation(90):
        pdf.cell(385, 20, txt = txt_invitado, align = 'C')

    pdf.set_xy(180, 350)
    pdf.cell(100, 100, link="https://goo.gl/maps/RLUk1SSV2RCDx1tV8")
    pdf.set_xy(121, 650)
    pdf.cell(100, 100, link="https://www.zepika.com/giftr/registry/view/uid/ximeyhono/")
    return pdf.output()
#    pdf.output(path + txt_invitado + ".pdf")  


def pdfs_para_lista(lista):
    with open(lista) as f:
        rdr = csv.reader(f, delimiter=",")
        for row in rdr:
            nombre = row[3].upper()
            boletos = mapa_invitados[row[1]]
            nuevo_pdf(boletos, nombre)


def main():
    
    reader = PdfReader("./base.pdf")
    page_overlay = PdfReader(io.BytesIO(nuevo_pdf("DOS INVITADOS", "CAROLINA MIJARES Y SEBASTIAN DE NYS"))).getPage(0)
    reader.getPage(0).merge_page(page2=page_overlay)

    writer = PdfWriter()
    writer.append_pages_from_reader(reader)
    writer.write(path + "test" + ".pdf")


    # writer = PdfWriter(trailer=PdfReader("./INVITACION\ XIME\ Y\ HONO\ EDITABLEpdf.pdf"))
    # PageMerge(writer.pagearray[1]).add(nuevo_pdf("Dos Invitados", "Isabel Morales Sirgo"), prepend=False).render()
    # writer.write(path + "test" + ".pdf")

if __name__=="__main__":
    main()