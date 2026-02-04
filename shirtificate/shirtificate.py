from fpdf import FPDF

class PDF(FPDF):
#     # def __init__(self):
#     #     self.add_page()
    def header(self):
        self.set_font('Times', size=12)
        self.cell(80)
        self.cell(30, 10, 'CS50 Shirtificate', align='C')
        self.image("/workspaces/153245272/shirtificate/shirtificate.png", x=0, y=0,h=pdf.eph/2, w=pdf.epw/2)


pdf = PDF()
pdf.add_page()
pdf.output('test.pdf')
