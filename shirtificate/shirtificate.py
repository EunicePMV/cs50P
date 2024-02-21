from fpdf import FPDF


name = input("Name: ")
pdf = FPDF(orientation="P", unit="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
