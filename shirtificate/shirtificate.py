from fpdf import FPDF


# name = input("Name: ")
pdf = FPDF(orientation="P", format="A4")
pdf.add_page()
pdf.set_font("helvetica", size=12)
pdf.cell(text="CS50 Shirtificate", center=True)
# # add center text for header
# pdf.image("shirtificate.png")
pdf.output("shirtificate.pdf")
