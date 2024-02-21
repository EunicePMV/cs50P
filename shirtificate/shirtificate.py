from fpdf import FPDF


name = input("Name: ")
pdf = FPDF(orientation="P", format="A4")
pdf.add_page()
pdf.set_font("helvetica", style="B", size=34)
pdf.cell(h=50, text="CS50 Shirtificate", center=True)
pdf.image("shirtificate.png", w=190, x=10, y=60)
pdf.set_font("helvetica", style="B", size=20)
pdf.set_text_color(255, 255, 255)
pdf.cell(h=235, text=F"{name} took CS50", center=True)
pdf.output("shirtificate.pdf")

