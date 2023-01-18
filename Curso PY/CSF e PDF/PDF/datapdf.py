import PyPDF2

# EXTRAINDO TEXTO PDF

f = open("Viagem.pdf", 'rb')

pdf_reader = PyPDF2.PdfReader(f)

pag_um = pdf_reader.pages[0]

text_pag_um = pag_um.extract_text()

f.close()

# ESCREVENDO TEXTO PDF

f = open("Viagem.pdf", 'rb')

pdf_reader = PyPDF2.PdfReader(f)

pag_um = pdf_reader.pages[0]

pdf_writer = PyPDF2.PdfWriter(f)

pdf_writer.add_page(pag_um)

pdf_output = open('um_novo_pdf.pdf', 'wb')

pdf_writer.write(pdf_output)

f.close()
pdf_output.close()

# FUNÇÃO COMPLETA

f = open("Viagem.pdf", 'rb')

pdf_text = []

pdf_reader = PyPDF2.PdfReader(f)

for num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[num]
    pdf_text.append(page.extract_text())

print(pdf_text[1])