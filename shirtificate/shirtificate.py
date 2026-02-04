from fpdf import FPDF

class PDF(FPDF):
#     # def __init__(self):
#     #     self.add_page()
    def header(self):
        self.set_font('Times', size=12)
        self.cell(80)
        self.cell(30, 10, 'CS50 Shirtificate', align='C')
        self.ln(20)

    def shirt_name(self, name):
        self.set_font('Times', size =12)
        self.image("/workspaces/153245272/shirtificate/shirtificate.png", x=(210-100)/2, y=30, w=100, h=0) #center = page_width - image_width /2
        self.cell(30, 10, f'{name} took CS50', align='C')

pdf = PDF()
pdf.add_page()
pdf.shirt_name(name="Noah")
pdf.output('test.pdf')
