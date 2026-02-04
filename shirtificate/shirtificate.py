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
        self.set_font('Times', 'B', size =12)
        self.image("/workspaces/153245272/shirtificate/shirtificate.png", x=(210-100)/2, y=30, w=100, h=0) #center = page_width - image_width /2
        self.set_xy((210-100)/2, 30 + 30) #set cursor to atop the shirt
        self.cell(100, 10, f'{name} took CS50', align='C')

def main():
    usr_name = input('Name: ')
    pdf = PDF()
    pdf.add_page()
    pdf.shirt_name(name=usr_name)
    pdf.output('shirtificate.pdf')

main()
