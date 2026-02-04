from fpdf import FPDF

# class PDF(FPDF):
#     # def __init__(self):
#     #     self.add_page()
#     # def header(self):
#     #     self.set_font('Times', size=12)
#     #     self.cell(80)
#     #     self.cell(30, 10, 'CS50 Shirtificate', align='C')

#     def shirt(self):
#         self.image('/workspaces/153245272/shirtificate/shirtificate.png', x=20, y=60)

# pdf = PDF()
# pdf.add_page()
# pdf.output('test.pdf')


pdf = FPDF()
pdf.add_page()
pdf.image("/workspaces/153245272/shirtificate/shirtificate.png.1", x=20, y=60)
pdf.output("pdf-with-image.pdf")
