from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm")

pdf.add_page()

pdf.output("output.pdf")
