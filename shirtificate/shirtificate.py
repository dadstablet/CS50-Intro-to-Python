from fpdf import FPDF

class PDF(FPDF):
    # def __init__(self):
    #     self.add_page()
    def header(self):
        pdf.set_font('Times', size=12)
        self.cell(30, 10, 'hello', align='C')

    # def shirt(self):
    #     pdf.set_font('Times', size=12)
    #     self.image('/workspaces/153245272/shirtificate/shirtificate.png', align='C')

pdf = PDF()
pdf.add_page()
pdf.output('test.pdf')
