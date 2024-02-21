from fpdf import FPDF


# name = input("Name: ")
pdf = FPDF(orientation="P", unit="A4")
pdf.add_page()
pdf.set_font("helvetica", size=12)
# add center text for header
pdf.image("shirtificate.png")
pdf.output("shirtificate.pdf")
