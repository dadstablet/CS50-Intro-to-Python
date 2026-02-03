from fpdf import FPDF

class PDF(FPDF):
    # def __init__(self):
    #     self.add_page()
    def header(self):
        pdf.set_font('Times', size=12)
        self.cell(105, 5, 'CS50 Shirtificate', align='C')

    # def shirt(self):
    #     pdf.set_font('Times', size=12)
    #     self.image('/workspaces/153245272/shirtificate/shirtificate.png', align='C')

pdf = PDF()
pdf.add_page()
pdf.header()
pdf.output('test.pdf')
