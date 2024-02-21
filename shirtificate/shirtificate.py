from fpdf import FPDF


name = input("Name: ")
pdf = FPDF(orientation="P", format="A4")
pdf.add_page()
pdf.set_font("helvetica", style="B", size=34)
pdf.cell(h=50, text="CS50 Shirtificate", center=True)
pdf.image("shirtificate.png", w=190, x=10, y=60)
pdf.set_font("helvetica", size=24)
pdf.cell(h=175, text=name, center=True)
pdf.output("shirtificate.pdf")
