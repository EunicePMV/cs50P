from fpdf import FPDF


# name = input("Name: ")
pdf = FPDF(orientation="P", format="A4")
pdf.add_page()
pdf.set_title("CS50 Shirtificate")
# pdf.set_font("helvetica", size=12)
# # add center text for header
# pdf.image("shirtificate.png")
pdf.output("shirtificate.pdf")
