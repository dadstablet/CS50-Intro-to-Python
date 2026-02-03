from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.cell(30, 10, 'CS50 Shirtificate', align='C')

    def shirt(self):
        self.image('/workspaces/153245272/shirtificate/shirtificate.png', align='C')

pdf = PDF()
pdf.add_page()
pdf.
pdf.cell()
pdf.shirt()
pdf.output('test.pdf')
