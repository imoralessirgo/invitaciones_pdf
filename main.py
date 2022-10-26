import csv
from json.tool import main
from fpdf import FPDF


mapa_invitados = {
    "1" : "BOLETO PERSONAL",
    "2" : "DOS INVITADOS",
    "3" : "TRES INVITADOS",
    "4" : "CUATRO INVITADOS",
    "5" : "CINCO INVITADOS"
}

boletos = ""
invitados = ""

path = "../../../mnt/i/My\ Drive/PROYECTOS\ 2022/XIMENA\ Y\ HONORE/INVITACIÓN\ DIGITAL\ XH/INVITACIONES\ PERSONALIZADAS/"

font_boletos = "SafiraMarch-gxeKY"
font_invitados = "Assistant-Lite"

# font_boletos = "Arial"
# font_invitados = "Arial"

lista_1 = "Xime.csv"
lista_2 = "Hono.csv"

def nuevo_pdf(txt_boletos, txt_invitado):
    pdf = FPDF("P","mm", [376.76666667,577.58541667])
    pdf.add_font('./Assistantant-Lite.ttf')
    #pdf.add_font('./SafiraMarch-gxeKY.otf')
    pdf.add_page()
    pdf.set_font(font_boletos, "", 11)
    pdf.set_xy(90.4875, 374.65)
    pdf.set_char_spacing(5)
    pdf.cell(108, 20, txt = txt_boletos, align = 'C')
    pdf.set_font(font_invitados, "", 22)
    pdf.set_xy(89.958333333, 350.30833333)
    pdf.set_char_spacing(5)
    with pdf.rotation(90):
        pdf.cell(295, 20, txt = txt_invitado, align = 'C')
    pdf.output(path + txt_invitado + ".pdf")  


def pdfs_para_lista(lista):
    with open(lista) as f:
        rdr = csv.reader(f, delimiter=",")
        for row in rdr:
            nombre = row[3].upper()
            boletos = mapa_invitados[row[1]]
            nuevo_pdf(boletos, nombre)


def main():
    nuevo_pdf("Dos Invitados", "Isabel Morales Sirgo")

if __name__=="__main__":
    main()