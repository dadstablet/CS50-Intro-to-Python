from fpdf import FPDF

pdf = FPDF() #automatically Portrait, A4, millimeters
pdf.add_page()
pdf.set_font("helvetica", style="B", size=16)
pdf.cell(105, 10, "CS50 Shirtificate")
pdf.output("tuto1.pdf")
