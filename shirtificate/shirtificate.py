from fpdf import FPDF

class PDF(FPDF):
    # def __init__(self):
    #     self.add_page()
    def header(self):
        self.set_font('Times', size=12)
        self.cell(80)
        self.cell(30, 10, 'CS50 Shirtificate', align='C')

    def shirt(self):
        self.image('/workspaces/153245272/shirtificate/shirtificate.png', 10, 8, 33)
        self.set_font('Times', size=12)

pdf = PDF()
pdf.add_page()
pdf.output('test.pdf')
