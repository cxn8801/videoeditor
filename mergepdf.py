from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["1.pdf", "2.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()